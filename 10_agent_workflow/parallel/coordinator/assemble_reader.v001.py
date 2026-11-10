#!/usr/bin/env python3
"""Assemble a 36-face READING PDF after all current page QA and lane integration."""
import argparse,hashlib,json,sys
from pathlib import Path
from pypdf import PdfReader,PdfWriter
from pypdf.generic import RectangleObject
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'scripts'))
import workflow as w
def main():
 p=argparse.ArgumentParser();p.add_argument('--preflight',action='store_true');p.add_argument('--output',default='final_book_19x24/TRUNG_NU_VUONG_READING_v001.pdf');a=p.parse_args()
 state=w.read('10_agent_workflow/production_state.json');tasks={t['id']:t for t in state['tasks']}
 needed=[f'PAGE{i:02d}_QA' for i in range(1,29)]+['FRONT_QA','BACK_QA','FRONT_MATTER']
 missing=[i for i in needed if tasks[i]['status']!='done']
 errors=w.check(state)
 if errors:raise SystemExit('Evidence validation failed: '+'; '.join(errors))
 if missing:
  print(json.dumps({'ready':False,'missing_current_qa':missing,'reading_only':True},ensure_ascii=False,indent=2))
  if not a.preflight:raise SystemExit(2)
  return
 pagination=w.read('10_agent_workflow/tasks/FRONT_MATTER/pagination.v001.json')
 assert len(pagination['reader_sequence'])==36
 sources=[]
 for entry in pagination['reader_sequence']:
  if 'qa_task_id' in entry:
   task=tasks[entry['qa_task_id']]
   report=w.read(task['evidence'][0]['path'])
   files=[x for x in report['artifacts'] if x.startswith('final_book_19x24/reading/') and x.endswith('.pdf')]
   if len(files)!=1:raise ValueError('Expected one current reading PDF for '+entry['qa_task_id'])
   rel=files[0]
  else:rel=entry['path']
  r=PdfReader(ROOT/rel);assert len(r.pages)==1
  pg=r.pages[0];width=float(pg.cropbox.width)*25.4/72;height=float(pg.cropbox.height)*25.4/72
  assert abs(width-190)<.01 and abs(height-240)<.01,(rel,width,height)
  assert pg.extract_text().strip(),rel
  sources.append((entry,rel,pg))
 if a.preflight:
  print(json.dumps({'ready':True,'faces':len(sources),'reading_only':True},ensure_ascii=False));return
 out=ROOT/a.output;assert out.is_relative_to(ROOT);assert not out.exists(),out
 out.parent.mkdir(parents=True,exist_ok=True)
 writer=PdfWriter();manifest=[]
 for entry,rel,pg in sources:
  # Keep original coordinate origin to preserve link annotation rectangles.
  pg.mediabox=RectangleObject(pg.cropbox);pg.trimbox=RectangleObject(pg.cropbox);pg.bleedbox=RectangleObject(pg.cropbox)
  writer.add_page(pg);writer.add_outline_item(entry['label'],len(writer.pages)-1)
  manifest.append(dict(entry,source=rel,sha256=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()))
 writer.add_metadata({'/Title':'TRƯNG NỮ VƯƠNG','/Subject':'Bản đọc - 32 trang ruột và 4 mặt bìa','/Creator':'TRƯNG NỮ VƯƠNG production'})
 with out.open('wb') as f:writer.write(f)
 r=PdfReader(out);assert len(r.pages)==36
 for pg in r.pages:
  assert abs(float(pg.mediabox.width)*25.4/72-190)<.01
  assert abs(float(pg.mediabox.height)*25.4/72-240)<.01
  assert pg.extract_text().strip()
 out.with_suffix('.manifest.json').write_text(json.dumps({'reading_only':True,'print_ready':False,'user_approved':False,'faces':36,'pages':manifest,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},ensure_ascii=False,indent=2)+'\n')
 print(out)
if __name__=='__main__':main()
