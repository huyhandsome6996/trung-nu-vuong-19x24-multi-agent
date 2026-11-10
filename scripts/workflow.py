#!/usr/bin/env python3
"""Local, resumable production queue. Never calls AI services or pushes Git."""
import argparse
import collections
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
STATE = '10_agent_workflow/production_state.json'
REQUIRED = {
    'source': ['external_sources', 'source_comparison'],
    'text': ['source_alignment', 'narration_35_65', 'keywords_preserved', 'dialogue_locked', 'template_locked'],
    'art': ['actual_refs', 'character_consistency', 'no_text', 'top_clearance', 'anatomy'],
    'layout': ['vietnamese_fonts', 'red_keywords', 'safe_text', 'bleed_geometry', 'no_overflow', 'speech_placement'],
    'qa': ['historical', 'art', 'language', 'print_geometry'],
    'frontmatter': ['pagination', 'text', 'rights'],
    'print_spec': ['printer_confirmed', 'icc_profile', 'binding', 'spine', 'font_license'],
    'assemble': ['page_order', '32_interior', '4_cover_faces', 'pdf_boxes', 'font_embedding', 'native_resolution'],
    'release': ['visual_review', 'print_preflight', 'delivery_manifest', 'no_open_issues'],
}


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def write(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(target.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(target)


def local(path):
    target = (ROOT / path).resolve()
    if not target.is_relative_to(ROOT.resolve()):
        raise ValueError('Path must stay inside repository')
    return target


def digest(path):
    return hashlib.sha256(local(path).read_bytes()).hexdigest()


def load():
    return read(STATE)


def task_by_id(state, task_id):
    return next((t for t in state['tasks'] if t['id'] == task_id), None)


def ready(state, task):
    return all(task_by_id(state, d)['status'] == 'done' for d in task['depends_on'])


def delegated_lane(task):
    if STATE != '10_agent_workflow/production_state.json':
        return None
    manifest = ROOT / '10_agent_workflow/parallel/assignments.json'
    if manifest.exists():
        for lane, data in json.loads(manifest.read_text())['lanes'].items():
            if task.get('page') in data['pages']:
                return lane
    return None


def choose(state):
    active = [t for t in state['tasks'] if t['status'] == 'in_progress' and not delegated_lane(t)]
    return (active or [t for t in state['tasks'] if t['status'] == 'todo' and not delegated_lane(t) and ready(state, t)] or [None])[0]


def story(page):
    for path in sorted((ROOT / '03_storyboards_and_scripts').glob('STORYBOARD*.md')):
        for m in re.finditer(r'(?ms)^### TRANG (\d+)\b.*?(?=^### TRANG |\Z)', path.read_text()):
            if int(m[1]) == page:
                section = m[0].strip()
                narration = re.search(r'^  > (.+)$', section, re.M)
                template = re.search(r'Template ([ABC])', section)
                if not narration or not template:
                    raise ValueError(f'Invalid storyboard structure: page {page}')
                return path.relative_to(ROOT).as_posix(), section, narration[1], template[1]
    raise ValueError(f'Page not found: {page}')


def page_refs(page):
    reg = read('09_design_system/design_registry.json')
    jobs = {j['id']: j for j in read('09_design_system/image_jobs.json')}
    matrix = next(p for p in read('09_design_system/page_asset_matrix.json') if p['page'] == page)
    refs = {'CHAR01': 'assets_generated/characters/CHAR_01_Trung_Trac_v001.png'}
    mapping = []
    for field in ['characters', 'environments', 'props']:
        for item in reg[field]:
            if item['id'] in matrix[field]:
                board = item['board']
                refs[board] = refs.get(board) or jobs[board]['output']
                mapping.append({'id': item['id'], 'name': item['name'], 'board': board,
                                'positions': jobs.get(board, {}).get('positions', 'Xem IMAGE_CATALOG.md')})
    # Add animal/crowd design boards as candidates; agent selects only relevant references.
    for board in ['ANIMAL01', 'ARMY01', 'CHIEFS01']:
        refs[board] = jobs[board]['output']
    return matrix, mapping, [{'board': b, 'path': p, 'sha256': digest(p)} for b, p in refs.items()]


def packet(state, task):
    folder = f"10_agent_workflow/tasks/{task['id']}"
    out = local(folder)
    out.mkdir(parents=True, exist_ok=True)
    report = {'task_id': task['id'], 'kind': task['kind'], 'status': 'draft', 'reviewer': '',
              'summary': '', 'checks': {k: 'not_checked' for k in REQUIRED.get(task['kind'], [])},
              'artifacts': [], 'open_issues': [], 'reviewed_at': ''}
    template = out / 'report.template.json'
    if not template.exists():
        write(f'{folder}/report.template.json', report)
    text = f"# {task['id']} — {task['title']}\n\nTệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.\n\n"
    text += f"Loại: `{task['kind']}`. Trạng thái: `{task['status']}`. Phụ thuộc: {', '.join(task['depends_on']) or 'không'}.\n\n"
    text += 'Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.\n\n'
    text += '## Việc cần làm\n\n' + task['instructions'] + '\n\n'
    if task.get('page'):
        page = task['page']
        source, section, narration, template_name = story(page)
        matrix, mapping, refs = page_refs(page)
        write(f'{folder}/reference_candidates.json', {'page': page, 'matrix': matrix, 'identities': mapping, 'candidates': refs})
        # Preserve manual edits. Text draft is not a locked production text.
        textpath = out / 'text.draft.json'
        if not textpath.exists():
            write(f'{folder}/text.draft.json', {'page': page, 'template': template_name, 'status': 'draft',
                'narration': narration, 'dialogues': [], 'dialogues_status': 'NOT_TRANSCRIBED',
                'storyboard_path': source, 'storyboard_sha256': digest(source), 'source_notes': '',
                'note': 'Chép đủ thoại từ storyboard, biên tập và kiểm nguồn trước khi khóa chữ.'})
        text += f'## Trang {page:02d}\n\nNguồn chữ hiện hành: `{source}`. Đếm tiếng bằng khoảng trắng: {len(narration.replace("**", "").split())}; mục tiêu35–65.\n\n'
        text += 'Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.\n\n'
        text += '### Cảnh và chữ từ storyboard\n\n' + section + '\n\n'
        text += '### Ảnh tham chiếu ứng viên\n\n'
        for ref in refs:
            rel = os.path.relpath(ROOT / ref['path'], out)
            text += f"- [{ref['board']}]({rel}): `{ref['path']}`\n"
        text += '\nreference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.\n'
        text += f'\nCác tệp của bước trước nằm trong evidence của dependencies tại `{STATE}`. Không tạo lại chữ/ảnh đã khóa.\n'
    text += '\n## Tiêu chí bàn giao\n\n'
    text += '\n'.join('- ' + k + ': kiểm thật và ghi pass khi có bằng chứng.' for k in REQUIRED.get(task['kind'], []))
    text += '\n\nCopy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.\n'
    text += '\nChạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.\n'
    (out / 'BRIEF.md').write_text(text, encoding='utf-8')
    print(folder + '/BRIEF.md')


def verify_report(task, path):
    report = read(local(path).relative_to(ROOT).as_posix())
    if report.get('task_id') != task['id'] or report.get('kind') != task['kind']:
        raise ValueError('Report task/kind mismatch')
    if report.get('status') != 'passed' or not all(report.get(k) for k in ['reviewer', 'summary', 'reviewed_at']):
        raise ValueError('Report needs passed status, reviewer, summary, reviewed_at')
    if report.get('open_issues') != []:
        raise ValueError('Resolve open issues before completing this task')
    for key in REQUIRED.get(task['kind'], []):
        if report.get('checks', {}).get(key) != 'pass':
            raise ValueError('Missing passed check: ' + key)
    artifacts = report.get('artifacts', [])
    if not artifacts or not all(isinstance(p, str) and local(p).is_file() for p in artifacts):
        raise ValueError('Report must reference existing artifact files inside repo')
    if task['kind'] == 'text':
        candidates = [read(p) for p in artifacts if p.endswith('.json')]
        candidates = [p for p in candidates if p.get('page') == task.get('page') and 'narration' in p]
        if not candidates:
            raise ValueError('Text task needs a page text JSON artifact')
        data = candidates[0]
        count = len(data['narration'].replace('**', '').split())
        if not 35 <= count <= 65 or data['narration'].count('**') % 2 or '**' not in data['narration']:
            raise ValueError('Narration needs 35–65 whitespace tokens and paired red keyword markers')
        if data.get('status') != 'locked' or data.get('dialogues_status') != 'locked':
            raise ValueError('Text and dialogues must be locked after real review')
        if data.get('template') != story(task['page'])[3]:
            raise ValueError('Template differs from storyboard; update canonical storyboard first')
        source = data.get('storyboard_path', '')
        if source != story(task['page'])[0] or data.get('storyboard_sha256') != digest(source):
            raise ValueError('Text was locked against a stale/different storyboard')
        for d in data.get('dialogues', []):
            if not d.get('speaker') or not d.get('text'):
                raise ValueError('Invalid dialogue speaker/text')
    if task['kind'] == 'art':
        from PIL import Image
        images = [p for p in artifacts if p.lower().endswith(('.png', '.jpg', '.webp'))]
        metas = [read(p) for p in artifacts if p.endswith('.json')]
        if not images or not metas:
            raise ValueError('Art requires image plus JSON metadata')
        meta = next((m for m in metas if m.get('image') in images), None)
        if not meta or not meta.get('prompt') or not meta.get('actual_references'):
            raise ValueError('Art metadata needs image, exact prompt and actual_references')
        if meta['prompt'].strip().lower() in {'undefined', 'null', 'none', 'exact_prompt_actually_sent'}:
            raise ValueError('Art metadata contains a placeholder instead of the actual submitted prompt')
        if meta.get('sha256') != digest(meta['image']):
            raise ValueError('Art hash mismatch')
        for ref in meta['actual_references']:
            if ref.get('sha256') != digest(ref['path']):
                raise ValueError('Reference hash mismatch')
        with Image.open(local(meta['image'])) as im:
            im.verify()
        with Image.open(local(meta['image'])) as im:
            if list(im.size) != meta.get('native_size_px'):
                raise ValueError('Native dimensions mismatch')
        if meta.get('text_free') is not True or meta.get('print_ready') is not False:
            raise ValueError('Raw image must be text-free and not labelled print-ready')
    return [{'path': path, 'sha256': digest(path)}] + [{'path': p, 'sha256': digest(p)} for p in artifacts]


def check(state):
    errors = []
    tasks = state['tasks']
    ids = [t['id'] for t in tasks]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate task IDs')
    visiting, visited = set(), set()
    def visit(i):
        if i in visiting:
            raise ValueError('Cycle at ' + i)
        if i in visited:
            return
        visiting.add(i)
        t = task_by_id(state, i)
        if t is None:
            raise ValueError('Missing task ' + i)
        for d in t['depends_on']:
            visit(d)
        visiting.remove(i)
        visited.add(i)
    try:
        for task in tasks:
            visit(task['id'])
            if task['status'] not in ['todo', 'in_progress', 'blocked', 'done']:
                errors.append('Unknown status ' + task['id'])
            if task['status'] in ['done', 'in_progress'] and not ready(state, task):
                errors.append('Incomplete dependency ' + task['id'])
            if task['status'] == 'blocked' and not task.get('block_reason'):
                errors.append('Blocked task missing reason ' + task['id'])
            if task['status'] == 'done' and not task.get('baseline'):
                ev = task.get('evidence', [])
                if not ev:
                    errors.append('Missing evidence ' + task['id'])
                else:
                    # Recheck acceptance, not just existence, to catch manual state edits.
                    verify_report(task, ev[0]['path'])
                    for entry in ev:
                        if digest(entry['path']) != entry['sha256']:
                            errors.append('Changed completed evidence ' + entry['path'])
        if sum(t['status'] == 'in_progress' for t in tasks) > 1:
            errors.append('main-only workflow allows one active writer')
        for p in range(1, 29):
            story(p)
        for path, sha in read('10_agent_workflow/source_hashes.json').items():
            if digest(path) != sha:
                errors.append('Source reference changed ' + path)
    except (ValueError, OSError, KeyError, StopIteration) as ex:
        errors.append(str(ex))
    return errors


def mutate(state, task, args):
    command = args.command
    if delegated_lane(task):
        raise ValueError('Delegated task: use scripts/parallel_workflow.py --lane ' + delegated_lane(task))
    if command == 'start':
        if task['status'] != 'todo' or not ready(state, task):
            raise ValueError('Task must be todo with all dependencies done')
        if any(t['status'] == 'in_progress' for t in state['tasks']):
            raise ValueError('Resume/checkpoint/block existing active task first')
        task.update(status='in_progress', owner=args.owner)
    elif command == 'checkpoint':
        if task['status'] != 'in_progress':
            raise ValueError('Checkpoint requires in_progress task')
    elif command == 'block':
        if task['status'] not in ['todo', 'in_progress']:
            raise ValueError('Can block only todo/in_progress')
        task.update(status='blocked', block_reason=args.note)
    elif command == 'unblock':
        if task['status'] != 'blocked':
            raise ValueError('Task is not blocked')
        task.update(status='todo', block_reason='')
    elif command == 'reopen':
        if task.get('baseline'):
            raise ValueError('Baseline is immutable in queue; use explicit design change control')
        affected = {task['id']}
        while True:
            expanded = affected | {t['id'] for t in state['tasks'] if set(t['depends_on']) & affected}
            if expanded == affected:
                break
            affected = expanded
        for downstream in state['tasks']:
            if downstream['id'] in affected:
                if downstream.get('evidence'):
                    downstream.setdefault('previous_evidence', []).append(downstream['evidence'])
                downstream.update(status='todo', evidence=[], block_reason='', last_note='Reopen: ' + args.note)
        print('Reopened dependency chain:', ', '.join(sorted(affected)))
    elif command == 'finish':
        if task['status'] != 'in_progress' or not ready(state, task):
            raise ValueError('Finish requires active task and completed dependencies')
        task['evidence'] = verify_report(task, args.evidence)
        task['status'] = 'done'
    task['last_note'] = args.note
    task['updated_at'] = now()
    state['history'].append({'at': now(), 'task': task['id'], 'action': command, 'note': args.note})
    write(STATE, state)
    print(task['id'], task['status'], args.note)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ['doctor', 'status', 'next', 'check']:
        p = sub.add_parser(name)
        if name == 'check':
            p.add_argument('--release', action='store_true')
    p = sub.add_parser('packet'); p.add_argument('task', nargs='?')
    for name in ['start', 'checkpoint', 'block', 'unblock', 'finish', 'reopen']:
        p = sub.add_parser(name); p.add_argument('task'); p.add_argument('--note', required=True)
        if name == 'start':
            p.add_argument('--owner', required=True)
        if name == 'finish':
            p.add_argument('--evidence', required=True)
    args = parser.parse_args()
    state = load()
    if args.command == 'doctor':
        print('Python:', sys.version.split()[0], '(requires 3.10+)')
        print('Pillow:', bool(importlib.util.find_spec('PIL')))
        print('Git branch:', subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip())
        print('Image generation: requires agent image tool / configured external provider; not bundled.')
        print('Print export: requires Vietnamese fonts, renderer and confirmed printer profile; not bundled.')
        return
    if args.command == 'check':
        errors = check(state)
        if args.release and any(t['status'] != 'done' for t in state['tasks']):
            errors.append('Release incomplete: outstanding production tasks')
        if errors:
            raise ValueError('\n'.join(errors))
        print(f"PASS workflow: {len(state['tasks'])} tasks, DAG, 28 storyboards, evidence and source hashes")
        return
    if args.command == 'status':
        print('Main-only; one active task per queue. Coordinator and delegated lanes have separate writers. Final book is not produced.')
        print(dict(collections.Counter(t['status'] for t in state['tasks'])))
        for t in state['tasks']:
            if t['status'] in ['blocked', 'in_progress']:
                print(t['id'], t['status'], t.get('block_reason') or t.get('last_note', ''))
        return
    if args.command == 'next':
        t = choose(state)
        print(f"{t['id']} [{t['status']}]: {t['title']}" if t else 'No executable task. Check blockers/release state.')
        if t and t.get('last_note'):
            print('Resume note:', t['last_note'])
        return
    task = task_by_id(state, args.task) if args.task else choose(state)
    if task is None:
        raise ValueError('Unknown task or no executable task')
    if delegated_lane(task):
        raise ValueError('Delegated task: use scripts/parallel_workflow.py --lane ' + delegated_lane(task))
    if args.command == 'packet':
        packet(state, task)
    else:
        mutate(state, task, args)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, StopIteration) as error:
        print('ERROR:', error, file=sys.stderr)
        sys.exit(1)
