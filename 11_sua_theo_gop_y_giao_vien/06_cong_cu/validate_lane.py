#!/usr/bin/env python3
"""Check lane staging and real per-page deliverables; visual review remains human work."""
from pathlib import Path
import argparse
import json
import subprocess
import sys

PACK = Path(__file__).resolve().parents[1]
ROOT = PACK.parent
CHECKS = ['source_and_scope', 'teacher_specific', 'yellow_boxes', 'flags_all_visible',
          'costumes_by_faction', 'vietnamese_text', 'dialogue_and_tail',
          'layout_and_no_damage', 'rendered_pdf_review']


def validate(lane, staged=False, ready=False):
    assignments = json.loads((PACK / '00_dieu_phoi/ASSIGNMENTS.json').read_text())
    errors = []
    if lane not in assignments['lanes']:
        return ['Unknown lane: ' + lane]
    lane_dir = PACK / '04_agents' / lane
    expected = assignments['lanes'][lane]
    if staged:
        raw = subprocess.check_output(['git', 'diff', '--cached', '--name-only', '--no-renames', '-z'], cwd=ROOT)
        names = [p.decode('utf-8') for p in raw.split(b'\0') if p]
        allowed = str(lane_dir.relative_to(ROOT)) + '/'
        if not names:
            errors.append('Nothing staged')
        errors.extend('Staged path outside lane: ' + p for p in names if not p.startswith(allowed))
    if ready:
        import fitz
        from PIL import Image
        for page in expected:
            stem = f'PDF_{page:02}'
            for relative in [f'text/{stem}.json', f'output/{stem}.png', f'output/{stem}.pdf', f'qa/{stem}.json']:
                if not (lane_dir / relative).is_file():
                    errors.append('Missing deliverable: ' + relative)
            source_candidates = list((lane_dir / 'source').glob(stem + '*'))
            if not any((p.is_file() and p.name != 'README.md') or
                       (p.is_dir() and any(child.is_file() and child.name != 'README.md' for child in p.rglob('*')))
                       for p in source_candidates):
                errors.append('Missing editable source: ' + stem)
            text_path = lane_dir / f'text/{stem}.json'
            if text_path.exists():
                value = json.loads(text_path.read_text())
                if not isinstance(value, dict) or not value.get('narration'):
                    errors.append('Text JSON needs final narration: ' + stem)
                if 'dialogue' not in value or 'changes' not in value:
                    errors.append('Text JSON needs dialogue list and changes: ' + stem)
            pdf_path = lane_dir / f'output/{stem}.pdf'
            if pdf_path.exists():
                with fitz.open(pdf_path) as pdf:
                    if len(pdf) != 1:
                        errors.append('PDF must contain one page: ' + stem)
                    elif abs(pdf[0].rect.width - assignments['page_size_pt'][0]) > .1 or abs(pdf[0].rect.height - assignments['page_size_pt'][1]) > .1:
                        errors.append('PDF page size changed: ' + stem)
            image_path = lane_dir / f'output/{stem}.png'
            if image_path.exists():
                with Image.open(image_path) as image:
                    w, h = image.size
                    if w < 896 or h < 1200 or abs(w / h - 896 / 1200) > .003:
                        errors.append('Image too small or aspect ratio changed: ' + stem)
            qa_path = lane_dir / f'qa/{stem}.json'
            if qa_path.exists():
                qa = json.loads(qa_path.read_text())
                if qa.get('pdf_page') != page or qa.get('status') != 'PASS':
                    errors.append('QA not PASS for page: ' + stem)
                for check in CHECKS:
                    if qa.get('checks', {}).get(check) != 'PASS':
                        errors.append('QA check incomplete: ' + stem + '/' + check)
                review = qa.get('visual_review', {})
                if not review.get('reviewed') or not review.get('reviewer') or not review.get('evidence'):
                    errors.append('Visual review evidence missing: ' + stem)
                for evidence in review.get('evidence', []):
                    evidence_path = (lane_dir / evidence).resolve()
                    if not evidence_path.is_relative_to(PACK) or not evidence_path.is_file():
                        errors.append('Visual evidence path missing/outside packet: ' + str(evidence))
                required = json.loads((PACK / f'03_nhiem_vu_tung_trang/{stem}.json').read_text())['requirements']
                results = qa.get('teacher_requirement_results', [])
                if len(results) != len(required) or any(not isinstance(r, dict) or r.get('status') != 'PASS' or not r.get('note') for r in results):
                    errors.append('Need one PASS with a note per teacher requirement: ' + stem)
        for relative in ['HANDOFF.md', 'output/LO_TRANG.pdf']:
            if not (lane_dir / relative).is_file():
                errors.append('Missing lane handoff: ' + relative)
        combined_path = lane_dir / 'output/LO_TRANG.pdf'
        if combined_path.exists():
            with fitz.open(combined_path) as combined:
                if len(combined) != len(expected):
                    errors.append('Wrong page count in lane PDF')
                elif any(abs(p.rect.width - assignments['page_size_pt'][0]) > .1 or abs(p.rect.height - assignments['page_size_pt'][1]) > .1 for p in combined):
                    errors.append('Wrong page size in lane PDF')
        if lane == 'agent_4' and not (lane_dir / 'source/THANH_THIEN_REFERENCE.png').is_file():
            errors.append('Missing Thánh Thiên reference for lane5')
        state = json.loads((lane_dir / 'STATUS.json').read_text())
        if state.get('status') != 'READY_FOR_COORDINATOR' or sorted(state.get('completed_pages', [])) != expected or state.get('blocked_pages'):
            errors.append('STATUS must be READY_FOR_COORDINATOR with all assigned pages complete and no blocked pages')
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('lane')
    parser.add_argument('--staged', action='store_true')
    parser.add_argument('--ready', action='store_true')
    args = parser.parse_args()
    if not args.staged and not args.ready:
        parser.error('Use --staged and/or --ready')
    errors = validate(args.lane, staged=args.staged, ready=args.ready)
    for error in errors:
        print('FAIL', error)
    if not errors:
        print('PASS', args.lane, '(technical/evidence checks only; coordinator visual review still required)')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
