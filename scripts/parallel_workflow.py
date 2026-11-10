#!/usr/bin/env python3
"""Disjoint page queues and guarded main-only publication for delegated agents."""
import argparse
import collections
import json
import os
from pathlib import Path
import re
import subprocess
import sys

import workflow as w

ROOT = w.ROOT
ASSIGNMENTS = '10_agent_workflow/parallel/assignments.json'
GLOBAL_STATE = '10_agent_workflow/production_state.json'
TASK_ACTIONS = {'packet', 'start', 'checkpoint', 'block', 'unblock', 'finish', 'reopen'}


def assignments():
    return json.loads((ROOT / ASSIGNMENTS).read_text(encoding='utf-8'))


def owned_tasks(lane):
    return {f'PAGE{p:02d}_{step}' for p in assignments()['lanes'][lane]['pages']
            for step in ['TEXT', 'ART', 'LAYOUT', 'QA']}


def state_path(lane):
    return f'10_agent_workflow/parallel/{lane}/production_state.json'


def allowed_path(lane, filename):
    path = Path(filename)
    if path.is_absolute() or '..' in path.parts or '\\' in filename:
        return False
    if filename.startswith(f'10_agent_workflow/parallel/{lane}/'):
        return True
    if filename.startswith(f'assets_generated/parallel/{lane}/'):
        return True
    pages = '|'.join(f'{p:02d}' for p in assignments()['lanes'][lane]['pages'])
    return bool(re.fullmatch(
        rf'(?:10_agent_workflow/tasks/PAGE(?:{pages})_(?:TEXT|ART|LAYOUT|QA)/.+|'
        rf'assets_generated/(?:raw_pages|speech_clouds)/PAGE(?:{pages})_[^/]+|'
        rf'final_book_19x24/(?:source|proofs|reading)/PAGE(?:{pages})_[^/]+)', filename))


def guard_paths(lane, paths, deleted=()):
    if deleted:
        raise ValueError('Preserve old versions; staged deletions are forbidden: ' + ', '.join(deleted))
    foreign = [p for p in paths if not allowed_path(lane, p)]
    if foreign:
        raise ValueError('Files outside ' + lane + ' ownership: ' + ', '.join(foreign))


def git(*args, check=True):
    env = os.environ.copy()
    env['GIT_TERMINAL_PROMPT'] = '0'
    token = env.get('TNV_GIT_TOKEN') or env.get('GH_TOKEN') or env.get('GITHUB_TOKEN')
    prefix = ['git']
    if token:
        # No token in repository, remote URL, persistent helper or printed command.
        env['TNV_EPHEMERAL_CREDENTIAL'] = ('protocol=https\nhost=github.com\n'
                                         'username=x-access-token\npassword=' + token + '\n\n')
        helper = '!f() { if [ "$1" = get ]; then printf "%s" "$TNV_EPHEMERAL_CREDENTIAL"; fi; }; f'
        prefix += ['-c', 'credential.helper=' + helper]
    result = subprocess.run(prefix + list(args), cwd=ROOT, env=env, capture_output=True, text=True)
    if token:
        result.stdout = result.stdout.replace(token, '[redacted]')
        result.stderr = result.stderr.replace(token, '[redacted]')
    if check and result.returncode:
        raise ValueError('git ' + args[0] + ' failed: ' + result.stderr.strip())
    return result


def names(*args):
    return [x for x in git(*args).stdout.split('\0') if x]


def changed_paths():
    return sorted(set(names('diff', '--name-only', '--no-renames', '-z') +
                      names('diff', '--cached', '--name-only', '--no-renames', '-z') +
                      names('ls-files', '--others', '--exclude-standard', '-z')))


def guard(lane):
    if git('branch', '--show-current').stdout.strip() != 'main':
        raise ValueError('Only main is authorized')
    deleted = names('diff', '--diff-filter=D', '--name-only', '--no-renames', '-z')
    deleted += names('diff', '--cached', '--diff-filter=D', '--name-only', '--no-renames', '-z')
    paths = changed_paths()
    guard_paths(lane, paths, deleted)
    return paths


def check_lane(lane):
    state = json.loads((ROOT / state_path(lane)).read_text(encoding='utf-8'))
    owned = owned_tasks(lane)
    found = {t['id'] for t in state['tasks'] if t.get('page') is not None}
    if found != owned:
        raise ValueError('Lane task scope does not match immutable assignments')
    for task in state['tasks']:
        if task['id'] not in owned and task['status'] != 'done':
            raise ValueError('External prerequisite must remain a completed read-only snapshot')
    errors = w.check(state)
    if errors:
        raise ValueError('\n'.join(errors))
    return state


def common_checks():
    subprocess.run([sys.executable, 'scripts/check_repo.py'], cwd=ROOT, check=True)


def stage(lane):
    paths = guard(lane)
    if paths:
        git('add', '--', *paths)
    print(f'{lane}: staged {len(paths)} owned paths')


def publish(lane, message, retries=8):
    guard(lane)
    if git('diff', '--quiet', check=False).returncode or names('ls-files', '--others', '--exclude-standard', '-z'):
        raise ValueError('Run the guarded stage command first; no unstaged/untracked work may be left behind')
    check_lane(lane)
    common_checks()
    if git('diff', '--cached', '--quiet', check=False).returncode:
        git('commit', '-m', message)
    published = git('rev-parse', 'HEAD').stdout.strip()
    for attempt in range(retries):
        git('fetch', 'origin', 'main')
        rebased = git('rebase', 'origin/main', check=False)
        if rebased.returncode:
            git('rebase', '--abort', check=False)
            raise ValueError('Unexpected overlap; rebase aborted and own commit preserved. Do not overwrite another lane.')
        check_lane(lane)
        common_checks()
        pushed = git('push', 'origin', 'main', check=False)
        if pushed.returncode:
            race = any(x in pushed.stderr.lower() for x in ['non-fast-forward', 'fetch first', 'updates were rejected'])
            if race and attempt + 1 < retries:
                continue
            raise ValueError('Push failed: ' + pushed.stderr.strip())
        for _ in range(retries):
            local = git('rev-parse', 'HEAD').stdout.strip()
            remote = git('ls-remote', 'origin', 'refs/heads/main').stdout.split()[0]
            if local == remote:
                print(json.dumps({'lane': lane, 'published_commit_before_rebase': published,
                                  'verified_local_and_remote_sha': local}, ensure_ascii=False))
                return local
            git('fetch', 'origin', 'main')
            git('merge', '--ff-only', 'origin/main')
        raise ValueError('Remote kept advancing; commits were pushed, but matching-head verification is pending')
    raise ValueError('Push race retry limit reached; do not force-push')


def validate_all():
    data = assignments()
    all_pages = [p for lane in data['lanes'].values() for p in lane['pages']]
    if len(all_pages) != len(set(all_pages)) or set(all_pages) & set(data['coordinator']['pages']):
        raise ValueError('Overlapping page ownership')
    if set(all_pages) | set(data['coordinator']['pages']) != set(range(1, 29)):
        raise ValueError('Page ownership must cover exactly01–28')
    for lane in data['lanes']:
        check_lane(lane)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lane', choices=['agent_a', 'agent_b'], required=True)
    parser.add_argument('command', choices=sorted(TASK_ACTIONS | {'status', 'next', 'check', 'guard', 'stage', 'publish', 'doctor'}))
    parser.add_argument('rest', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    lane = args.lane
    if args.command == 'guard':
        print(f'PASS {lane}: {len(guard(lane))} changed paths are owned')
        return
    if args.command == 'stage':
        stage(lane)
        return
    if args.command == 'publish':
        p = argparse.ArgumentParser();p.add_argument('--message', required=True)
        publish(lane, p.parse_args(args.rest).message)
        return
    if args.command == 'check':
        check_lane(lane);print('PASS scoped queue/evidence: ' + lane)
        return
    state = check_lane(lane)
    if args.command == 'status':
        tasks = [t for t in state['tasks'] if t['id'] in owned_tasks(lane)]
        print(lane, dict(collections.Counter(t['status'] for t in tasks)))
        for task in tasks:
            if task['status'] in ['in_progress', 'blocked']:
                print(task['id'], task.get('last_note', ''))
        return
    if args.command in TASK_ACTIONS:
        if not args.rest or args.rest[0] not in owned_tasks(lane):
            raise ValueError('Explicit owned task ID required; no cross-lane operations')
    w.STATE = state_path(lane)
    sys.argv = [sys.argv[0], args.command, *args.rest]
    w.main()


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        print('ERROR:', error, file=sys.stderr)
        sys.exit(1)
