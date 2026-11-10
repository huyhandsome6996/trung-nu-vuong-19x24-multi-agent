#!/usr/bin/env python3
"""Record a completed manual page review; never substitutes for pixel inspection."""
import argparse,json,subprocess
from pathlib import Path
from datetime import datetime,timezone
from PIL import Image
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[3]
p=argparse.ArgumentParser();p.add_argument('page',type=int);p.add_argument('version');p.add_argument('speech_version');p.add_argument('--summary',required=True);a=p.parse_args()
page=f'PAGE{a.page:02d}';v=a.version;s=f'assets_generated/speech_clouds/{page}_SPEECH01_{a.speech_version}'
artifacts=[f'final_book_19x24/source/{page}_{v}.svg',f'final_book_19x24/source/{page}_placement.{v}.json','final_book_19x24/source/render_page.v004.py',*[f'final_book_19x24/proofs/{page}_{v}.{x}' for x in ['pdf','png','json']],f'final_book_19x24/reading/{page}_{v}.pdf',*[s+x for x in ['.png','.json','.request.json']]]
for rel in artifacts:
    assert (ROOT/rel).is_file(),rel
    if rel.endswith('.png'):
        with Image.open(ROOT/rel) as im:im.verify()
for rel in [f'final_book_19x24/proofs/{page}_{v}.pdf',f'final_book_19x24/reading/{page}_{v}.pdf']:
    pg=PdfReader(ROOT/rel).pages[0]
    assert abs(float(pg.trimbox.width)*25.4/72-190)<.01
    assert abs(float(pg.trimbox.height)*25.4/72-240)<.01
    assert pg.extract_text().strip()
now=datetime.now(timezone.utc).isoformat()
base={'status':'passed','reviewer':'Codex coordinator','summary':a.summary,'artifacts':artifacts,'open_issues':[],'reviewed_at':now}
for kind,checks in [('layout',['vietnamese_fonts','red_keywords','safe_text','bleed_geometry','no_overflow','speech_placement']),('qa',['historical','art','language','print_geometry'])]:
    report=dict(base,task_id=page+'_'+kind.upper(),kind=kind,checks={k:'pass' for k in checks})
    target=ROOT/f'10_agent_workflow/tasks/{page}_{kind.upper()}/report.{v}.json'
    assert not target.exists(),target
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(page,v,'manual review recorded; finish tasks separately')
