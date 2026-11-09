"""Exercise failure/recovery paths without changing the actual production queue."""
import argparse
import contextlib
import copy
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import workflow as w
import typeset_preview as proof

REAL_ROOT = w.ROOT


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        w.ROOT = Path(self.tmp.name)
        self.addCleanup(setattr, w, 'ROOT', REAL_ROOT)
        shutil.copytree(REAL_ROOT/'03_storyboards_and_scripts', w.ROOT/'03_storyboards_and_scripts')
        w.write('10_agent_workflow/source_hashes.json', {})
        self.state={'tasks': [
            dict(id='BASE', kind='baseline', baseline=True, status='done', depends_on=[]),
            dict(id='SOURCE', kind='source', status='blocked', depends_on=['BASE'], block_reason='Needs source'),
            dict(id='PAGE01_TEXT', kind='text', page=1, status='todo', depends_on=['BASE']),
            dict(id='PAGE01_ART', kind='art', page=1, status='todo', depends_on=['PAGE01_TEXT'])
        ], 'history': []}
        w.write(w.STATE,self.state)

    def mutate(self, task_id, command, **kwargs):
        args=argparse.Namespace(command=command,note='Test checkpoint',owner='test-agent',**kwargs)
        with contextlib.redirect_stdout(io.StringIO()):
            w.mutate(self.state,w.task_by_id(self.state,task_id),args)

    def text_report(self):
        source,_,narration,template=w.story(1)
        w.write('text.json',dict(page=1,template=template,narration=narration,dialogues=[],status='locked',dialogues_status='locked',storyboard_path=source,storyboard_sha256=w.digest(source)))
        report=dict(task_id='PAGE01_TEXT',kind='text',status='passed',reviewer='test',summary='Fixture report',reviewed_at='2026-11-09',checks={k:'pass' for k in w.REQUIRED['text']},artifacts=['text.json'],open_issues=[])
        w.write('report.json',report)
        return report

    def test_next_skips_blocker_and_resumes_after_reload(self):
        self.assertEqual(w.choose(self.state)['id'],'PAGE01_TEXT')
        self.mutate('PAGE01_TEXT','start')
        self.mutate('PAGE01_TEXT','checkpoint')
        self.assertEqual(w.choose(w.load())['last_note'],'Test checkpoint')
        self.assertEqual(w.choose(w.load())['status'],'in_progress')

    def test_start_rejects_unfinished_dependency(self):
        with self.assertRaisesRegex(ValueError,'dependencies'):
            self.mutate('PAGE01_ART','start')

    def test_finish_rejects_unchecked_report(self):
        report=self.text_report();report['checks']['source_alignment']='not_checked';w.write('report.json',report)
        self.mutate('PAGE01_TEXT','start')
        with self.assertRaisesRegex(ValueError,'source_alignment'):
            self.mutate('PAGE01_TEXT','finish',evidence='report.json')
        self.assertEqual(w.load()['tasks'][2]['status'],'in_progress')

    def test_finish_hash_tampering_and_reopen_downstream(self):
        self.text_report();self.mutate('PAGE01_TEXT','start');self.mutate('PAGE01_TEXT','finish',evidence='report.json')
        self.assertEqual(w.choose(self.state)['id'],'PAGE01_ART')
        self.assertEqual(w.check(self.state),[])
        text=w.read('text.json');text['source_notes']='Changed';w.write('text.json',text)
        self.assertTrue(any('Changed completed evidence' in e for e in w.check(self.state)))
        self.mutate('PAGE01_TEXT','reopen')
        self.assertEqual(w.task_by_id(self.state,'PAGE01_ART')['status'],'todo')
        self.assertTrue(w.task_by_id(self.state,'PAGE01_TEXT')['previous_evidence'])
        self.assertEqual(w.check(self.state),[])

    def test_stale_storyboard_rejected(self):
        self.text_report();source=w.story(1)[0]
        with (w.ROOT/source).open('a') as out:out.write('\nChanged script\n')
        with self.assertRaisesRegex(ValueError,'stale'):
            w.verify_report(w.task_by_id(self.state,'PAGE01_TEXT'),'report.json')

    def test_cycle_and_path_escape_rejected(self):
        self.state['tasks'][0]['depends_on']=['PAGE01_ART']
        self.assertTrue(any('Cycle' in e for e in w.check(self.state)))
        with self.assertRaisesRegex(ValueError,'inside repository'):
            w.local('../outside')

    def test_art_native_dimensions_and_reference_integrity(self):
        from PIL import Image
        Image.new('RGB',(80,100)).save(w.ROOT/'art.png')
        Image.new('RGB',(4,4)).save(w.ROOT/'reference.png')
        meta=dict(image='art.png',prompt='Actual prompt fixture',actual_references=[dict(path='reference.png',sha256=w.digest('reference.png'))],sha256=w.digest('art.png'),native_size_px=[81,100],text_free=True,print_ready=False)
        w.write('art.json',meta)
        report=dict(task_id='PAGE01_ART',kind='art',status='passed',reviewer='test',summary='Fixture art review',reviewed_at='2026-11-09',checks={k:'pass' for k in w.REQUIRED['art']},artifacts=['art.png','art.json'],open_issues=[])
        w.write('report.json',report)
        with self.assertRaisesRegex(ValueError,'Native dimensions'):
            w.verify_report(w.task_by_id(self.state,'PAGE01_ART'),'report.json')
        meta['native_size_px']=[80,100];w.write('art.json',meta)
        self.assertEqual(len(w.verify_report(w.task_by_id(self.state,'PAGE01_ART'),'report.json')),3)
        (w.ROOT/'reference.png').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError,'Reference hash'):
            w.verify_report(w.task_by_id(self.state,'PAGE01_ART'),'report.json')

    def test_preview_red_keywords_escape_and_draft_rejection(self):
        self.assertEqual(proof.keywords('A **đỏ** <b>'),'A <strong>đỏ</strong> &lt;b&gt;')
        w.write('draft.json',dict(status='draft',dialogues_status='NOT_TRANSCRIBED'))
        with self.assertRaisesRegex(ValueError,'locked'):
            proof.build('draft.json','missing.png','proof.html','missing.ttf')
        with self.assertRaisesRegex(ValueError,'Unpaired'):
            proof.keywords('**dangling')


if __name__=='__main__':unittest.main()
