#!/usr/bin/env python3
"""Run local acceptance checks without generating art or approving print quality."""
from pathlib import Path
import re
import subprocess
import sys
import workflow

ROOT = Path(__file__).resolve().parents[1]
errors = workflow.check(workflow.load())
if (ROOT / '10_agent_workflow/parallel/assignments.json').exists():
    import parallel_workflow
    try:
        parallel_workflow.validate_all()
    except (ValueError, OSError, KeyError) as error:
        errors.append('Parallel lanes: ' + str(error))
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    # Code samples may describe future artifacts; only actual Markdown links are checked.
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
        if '://' in target or target.startswith('#'):
            continue
        if not (path.parent / target.split('#')[0]).exists():
            errors.append(f'Broken Markdown target: {path.relative_to(ROOT)} -> {target}')
for path in ROOT.rglob('*'):
    if not path.is_file() or '.git' in path.parts or path.suffix not in ['.md', '.py', '.json', '.yml', '.yaml', '.html', '.txt']:
        continue
    if re.search(r'gh[pousr]_[A-Za-z0-9]{20,}', path.read_text(encoding='utf-8')):
        errors.append(f'Credential-like content: {path.relative_to(ROOT)}')
for command in [[sys.executable, '09_design_system/validate_design_system.py', '--complete'], ['git', 'diff', '--check']]:
    if subprocess.run(command, cwd=ROOT).returncode:
        errors.append('Command failed: ' + ' '.join(command))
if errors:
    print('\n'.join('FAIL ' + e for e in errors)); sys.exit(1)
print('PASS repository: workflow, Markdown targets, credential patterns, design assets and whitespace')
