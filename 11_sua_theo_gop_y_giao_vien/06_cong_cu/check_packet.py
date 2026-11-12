#!/usr/bin/env python3
"""Validate this 21-page correction packet without using the old production queue."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

PACK = Path(__file__).resolve().parents[1]
ROOT = PACK.parent


def main():
    errors = []
    assignments = json.loads((PACK / '00_dieu_phoi/ASSIGNMENTS.json').read_text())
    manifest = json.loads((PACK / '00_dieu_phoi/SOURCE_MANIFEST.json').read_text())
    branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip()
    if branch != assignments['branch']:
        errors.append('Wrong branch: ' + branch)
    pages = [n for values in assignments['lanes'].values() for n in values]
    if sorted(pages) != list(range(1, 22)) or len(set(pages)) != len(pages):
        errors.append('Assignments must cover PDF01-21 exactly once')
    for item in manifest['files']:
        path = PACK / item['path']
        if not path.is_file():
            errors.append('Missing immutable source: ' + item['path'])
        elif path.stat().st_size != item['bytes'] or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            errors.append('Source changed: ' + item['path'])
    for lane, assigned in assignments['lanes'].items():
        for relative in [f'04_agents/{lane}/BRIEF.md', f'04_agents/{lane}/STATUS.json', f'05_prompts/PROMPT_{lane.upper()}.md']:
            if not (PACK / relative).is_file():
                errors.append('Missing: ' + relative)
        for page in assigned:
            for suffix in ['md', 'json']:
                path = PACK / f'03_nhiem_vu_tung_trang/PDF_{page:02}.{suffix}'
                if not path.is_file():
                    errors.append('Missing page task: ' + str(page))
            task = json.loads((PACK / f'03_nhiem_vu_tung_trang/PDF_{page:02}.json').read_text())
            if task['owner'] != lane or task['pdf_page'] != page:
                errors.append('Page ownership mismatch: ' + str(page))
    for path in PACK.rglob('*'):
        if path.is_file() and path.suffix in {'.md', '.json', '.py', '.txt', '.svg'}:
            content = path.read_text(encoding='utf-8')
            # Build the pattern without placing credential-shaped material in this tool.
            pattern = 'gh' + '[pousr]_' + '[A-Za-z0-9]{20,}'
            if re.search(pattern, content):
                errors.append('Credential-like content: ' + str(path.relative_to(PACK)))
    if subprocess.run(['git', 'diff', '--check'], cwd=ROOT, capture_output=True).returncode:
        errors.append('git diff --check failed')
    for error in errors:
        print('FAIL', error)
    if errors:
        return 1
    print(f'PASS packet: {len(manifest["files"])} immutable files, 21 pages, 5 disjoint lanes, correct branch, no credentials')
    return 0


if __name__ == '__main__':
    sys.exit(main())
