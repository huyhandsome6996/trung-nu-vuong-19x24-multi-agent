"""Scope isolation and real two-clone main publication, without network or PATs."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import parallel_workflow as p
import workflow as w


class ParallelTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        old_root, old_wroot, old_state = p.ROOT, w.ROOT, w.STATE
        self.addCleanup(setattr, p, 'ROOT', old_root)
        self.addCleanup(setattr, w, 'ROOT', old_wroot)
        self.addCleanup(setattr, w, 'STATE', old_state)
        p.ROOT = w.ROOT = self.root
        w.STATE = p.GLOBAL_STATE
        self.manifest = {'coordinator': {'pages': list(range(1, 14))},
                         'lanes': {'agent_a': {'pages': list(range(14, 21))},
                                   'agent_b': {'pages': list(range(21, 29))}}}
        self.write_manifest(self.root)

    def write_manifest(self, root):
        path = root / p.ASSIGNMENTS
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.manifest))

    def run_git(self, cwd, *args):
        result = subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True)
        if result.returncode:
            self.fail(result.stderr)
        return result.stdout.strip()

    def fixture_clones(self):
        remote, seed = self.root / 'remote.git', self.root / 'seed'
        self.run_git(self.root, 'init', '--bare', '--initial-branch=main', str(remote))
        self.run_git(self.root, 'clone', str(remote), str(seed))
        self.write_manifest(seed)
        self.run_git(seed, 'config', 'user.name', 'Test')
        self.run_git(seed, 'config', 'user.email', 'test@example.invalid')
        self.run_git(seed, 'add', '--', p.ASSIGNMENTS)
        self.run_git(seed, 'commit', '-m', 'baseline')
        self.run_git(seed, 'push', 'origin', 'main')
        clones = []
        for name in ['a', 'b']:
            target = self.root / name
            self.run_git(self.root, 'clone', str(remote), str(target))
            self.run_git(target, 'config', 'user.name', 'Test')
            self.run_git(target, 'config', 'user.email', 'test@example.invalid')
            clones.append(target)
        return remote, *clones

    def test_page_boundary_and_lane_assets(self):
        for filename in ['assets_generated/raw_pages/PAGE14_v002.png',
                         'assets_generated/speech_clouds/PAGE20_SPEECH01_v001.request.json',
                         '10_agent_workflow/tasks/PAGE19_QA/report.v001.json',
                         '10_agent_workflow/parallel/agent_a/WORK_LOG.md']:
            self.assertTrue(p.allowed_path('agent_a', filename), filename)
            self.assertFalse(p.allowed_path('agent_b', filename), filename)
        self.assertTrue(p.allowed_path('agent_b', 'final_book_19x24/proofs/PAGE28_v001.pdf'))
        self.assertFalse(p.allowed_path('agent_a', 'assets_generated/raw_pages/PAGE140_v001.png'))

    def test_rejects_shared_files_and_traversal(self):
        for filename in [p.GLOBAL_STATE, p.ASSIGNMENTS, 'AGENTS.md',
                         '08_project_memory/WORK_LOG.md', 'scripts/render_page.py',
                         '09_design_system/SOURCE_DECISIONS.md',
                         'final_book_19x24/source/fonts/NotoSans-Regular.ttf',
                         '10_agent_workflow/parallel/agent_a/../../production_state.json']:
            with self.assertRaises(ValueError, msg=filename):
                p.guard_paths('agent_a', [filename])

    def test_preserves_old_versions(self):
        filename = 'assets_generated/raw_pages/PAGE14_v001.png'
        with self.assertRaisesRegex(ValueError, 'Preserve old versions'):
            p.guard_paths('agent_a', [filename], deleted=[filename])

    def test_global_queue_cannot_mutate_delegated_task(self):
        task = {'id': 'PAGE14_TEXT', 'page': 14, 'status': 'todo', 'depends_on': []}
        args = argparse.Namespace(command='start', owner='wrong', note='must reject')
        with self.assertRaisesRegex(ValueError, 'Delegated task'):
            w.mutate({'tasks': [task]}, task, args)
        self.assertEqual(task['status'], 'todo')

    def test_global_next_keeps_dependency_graph_when_skipping_lanes(self):
        state = {'tasks': [
            {'id': 'PAGE14_TEXT', 'page': 14, 'status': 'blocked', 'depends_on': []},
            {'id': 'ASSEMBLY', 'status': 'todo', 'depends_on': ['PAGE14_TEXT']},
            {'id': 'PAGE13_ART', 'page': 13, 'status': 'todo', 'depends_on': []}]}
        self.assertEqual(w.choose(state)['id'], 'PAGE13_ART')

    def test_two_clones_rebase_owned_commits_without_losing_either(self):
        remote, a, b = self.fixture_clones()
        file_a = '10_agent_workflow/parallel/agent_a/WORK_LOG.md'
        file_b = '10_agent_workflow/parallel/agent_b/WORK_LOG.md'
        for root, filename, content in [(a, file_a, 'A saved'), (b, file_b, 'B saved')]:
            path = root / filename;path.parent.mkdir(parents=True, exist_ok=True);path.write_text(content)
            self.run_git(root, 'add', '--', filename)
            self.run_git(root, 'commit', '-m', content)
        # B is already committed from the old common head before A publishes.
        with mock.patch.object(p, 'check_lane', return_value={}), mock.patch.object(p, 'common_checks'), contextlib.redirect_stdout(io.StringIO()):
            p.ROOT = a;p.publish('agent_a', 'A checkpoint')
            p.ROOT = b;head = p.publish('agent_b', 'B checkpoint')
        self.assertEqual(self.run_git(b, 'ls-remote', 'origin', 'refs/heads/main').split()[0], head)
        self.assertEqual(self.run_git(self.root, '--git-dir=' + str(remote), 'show', 'main:' + file_a), 'A saved')
        self.assertEqual(self.run_git(self.root, '--git-dir=' + str(remote), 'show', 'main:' + file_b), 'B saved')
        self.assertEqual(self.run_git(self.root, '--git-dir=' + str(remote), 'for-each-ref', '--format=%(refname)', 'refs/heads'), 'refs/heads/main')

    def test_guarded_stage_does_not_stage_foreign_file(self):
        _, a, _ = self.fixture_clones()
        (a / 'AGENTS.md').write_text('Accidental shared change')
        p.ROOT = a
        with self.assertRaisesRegex(ValueError, 'outside agent_a'):
            p.stage('agent_a')
        self.assertEqual(self.run_git(a, 'diff', '--cached', '--name-only'), '')

    def test_publish_rejects_foreign_file_already_committed_in_clean_tree(self):
        _, a, _ = self.fixture_clones()
        previous = self.run_git(a, 'rev-parse', 'origin/main')
        (a / 'AGENTS.md').write_text('Accidental committed shared change')
        self.run_git(a, 'add', '--', 'AGENTS.md')
        self.run_git(a, 'commit', '-m', 'must remain local')
        own_head = self.run_git(a, 'rev-parse', 'HEAD')
        p.ROOT = a
        with mock.patch.object(p, 'check_lane', return_value={}), mock.patch.object(p, 'common_checks'):
            with self.assertRaisesRegex(ValueError, 'outside agent_a'):
                p.publish('agent_a', 'must reject')
        self.assertEqual(self.run_git(a, 'rev-parse', 'HEAD'), own_head)
        self.assertEqual(self.run_git(a, 'ls-remote', 'origin', 'refs/heads/main').split()[0], previous)

    def test_push_race_retries_after_remote_changes_between_fetch_and_push(self):
        remote, a, b = self.fixture_clones()
        file_a = '10_agent_workflow/parallel/agent_a/WORK_LOG.md'
        file_b = '10_agent_workflow/parallel/agent_b/WORK_LOG.md'
        for root, filename, content in [(a, file_a, 'A race saved'), (b, file_b, 'B race saved')]:
            path = root / filename;path.parent.mkdir(parents=True, exist_ok=True);path.write_text(content)
            self.run_git(root, 'add', '--', filename)
            self.run_git(root, 'commit', '-m', content)
        original_git = p.git
        pushes = []

        def interleave(*args, **kwargs):
            if args == ('push', 'origin', 'main'):
                pushes.append(args)
                if len(pushes) == 1:
                    self.run_git(a, 'push', 'origin', 'main')
            return original_git(*args, **kwargs)

        p.ROOT = b
        with mock.patch.object(p, 'check_lane', return_value={}), mock.patch.object(p, 'common_checks'), \
                mock.patch.object(p, 'git', side_effect=interleave), contextlib.redirect_stdout(io.StringIO()):
            head = p.publish('agent_b', 'B race checkpoint')
        self.assertEqual(len(pushes), 2)
        self.assertEqual(self.run_git(b, 'ls-remote', 'origin', 'refs/heads/main').split()[0], head)
        self.assertEqual(self.run_git(self.root, '--git-dir=' + str(remote), 'show', 'main:' + file_a), 'A race saved')
        self.assertEqual(self.run_git(self.root, '--git-dir=' + str(remote), 'show', 'main:' + file_b), 'B race saved')


if __name__ == '__main__':
    unittest.main()
