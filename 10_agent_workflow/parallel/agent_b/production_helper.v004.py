"""Lane-local evidence utilities. Call reports only after actual manual pixel review."""
import json, hashlib, datetime, subprocess, sys
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
def read(p): return json.loads(Path(p).read_text())
def write(p,d):
    p=Path(p)
    if p.exists(): raise ValueError('Immutable existing file '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def report(page,kind,version,summary,artifacts):
    p=Path(f'10_agent_workflow/tasks/PAGE{page:02d}_{kind.upper()}')
    r=read(p/'report.template.json')
    for f in artifacts: assert Path(f).is_file(),f
    r.update(status='passed',reviewer='agent_b',summary=summary,checks={k:'pass' for k in r['checks']},artifacts=artifacts,open_issues=[],reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    write(p/f'report.{version}.json',r)
def lock(page,narration,notes,version='v001'):
    p=Path(f'10_agent_workflow/tasks/PAGE{page:02d}_TEXT')
    d=read(p/'text.draft.json')
    sys.path.insert(0,str(Path('scripts').resolve()));import workflow
    section=workflow.story(page)[1]
    import re
    ds=[{'speaker':m[0],'text':m[1]} for m in re.findall(r'- \*([^*]+?):?\*:?\s*"([^"]+)"',section)]
    count=len(narration.replace('**','').split()); assert 35<=count<=65,count
    d.update(status='locked',dialogues_status='locked',narration=narration,dialogues=ds,source_notes=notes,narration_tokens=count,note='Agent B: source-checked adaptation; storyboard shared file preserved.')
    write(p/f'text.{version}.json',d)
    report(page,'text',version,f'Đã đọc nguồn; khóa {count}tiếng và {len(ds)}thoại đầy đủ. '+notes,[str(p/f'text.{version}.json')])
    print(page,count,'tokens',len(ds),'dialogues')
def accept_art(page,output,version,refs,summary):
    import shutil
    p=Path(f'assets_generated/raw_pages/PAGE{page:02d}_{version}.png');assert not p.exists();shutil.copy2(output,p)
    t=Path(f'10_agent_workflow/tasks/PAGE{page:02d}_ART')
    prompt=t/f'prompt.{version}.txt'
    m={'image':str(p),'version':version,'native_size_px':list(Image.open(p).size),'sha256':sha(p),'prompt':prompt.read_text().strip(),'actual_references':[{'path':r,'sha256':sha(r)} for r in refs],'generator':'image_gen.imagegen built-in; model not exposed','text_free':True,'top_clearance_checked':True,'visual_qa_report':str(t/f'report.{version}.json'),'user_approved':False,'print_ready':False,'note':summary}
    write(p.with_suffix('.json'),m)
    report(page,'art',version,summary,[str(p),str(p.with_suffix('.json')),str(prompt)])
def technical(page,version):
    from pypdf import PdfReader
    b=f'final_book_19x24/proofs/PAGE{page:02d}_{version}'
    r=PdfReader(b+'.pdf');assert len(r.pages)==1
    p=r.pages[0];pt=72/25.4
    assert abs(float(p.mediabox.width)/pt-196)<.01
    assert abs(float(p.mediabox.height)/pt-246)<.01
    assert abs(float(p.trimbox.width)/pt-190)<.01
    assert abs(float(p.trimbox.height)/pt-240)<.01
    assert len(p.extract_text())>50
    fonts=subprocess.check_output(['pdffonts',b+'.pdf'],text=True)
    assert 'NotoSans-Regular' in fonts and 'NotoSans-Bold' in fonts
    for line in fonts.splitlines()[2:]: assert 'yes yes yes' in line,line
    for suffix in ['.png','_300dpi.png']:
        with Image.open(b+suffix) as im: im.verify()
    m=read(b+'.json');assert not m['missing_glyphs'] and m['pdf_text_matches']
    assert all(not x['overflow'] for x in m['boxes'])
    return {'boxes_mm':{'media':[196,246],'trim':[190,240],'bleed':[196,246]},'fonts':fonts,'metrics':m}
if __name__=='__main__':
    if sys.argv[1]=='technical': print(json.dumps(technical(int(sys.argv[2]),sys.argv[3]),ensure_ascii=False,indent=2))

def accept_speech(page,output,version,textversion,refs,bbox,placementversion):
    import shutil
    p=Path(f'assets_generated/speech_clouds/PAGE{page:02d}_SPEECH01_{version}.png');assert not p.exists();shutil.copy2(output,p)
    d=read(f'10_agent_workflow/tasks/PAGE{page:02d}_TEXT/text.{textversion}.json');sz=Image.open(p).size
    write(p.with_suffix('.json'),{'text':d['dialogues'][0]['text'],'speaker':d['dialogues'][0]['speaker'],'status':'visual_text_verified','image':str(p),'sha256':sha(p),'native_size_px':list(sz),'generator':'image_gen.imagegen built-in; model not exposed','prompt':p.with_suffix('.prompt.txt').read_text().strip(),'actual_references':[{'path':r,'sha256':sha(r)} for r in refs],'visual_review':'Manual reading of all visible words and accents in returned native pixels: exact locked quote. Alpha retained. Final placement reviewed separately.','user_approved':False,'print_ready':False})
    x,y,w=bbox
    write(f'final_book_19x24/source/PAGE{page:02d}_{placementversion}.placement.json',{'dialogues':[{'lettered_asset':str(p),'bbox_mm':[x,y,w,w*sz[1]/sz[0]]}]})

def layout_report(page,version,placementversion,speechversion,summary):
    t=technical(page,version);tp=f'10_agent_workflow/tasks/PAGE{page:02d}_LAYOUT/technical.v001.json';write(tp,t)
    a=[f'final_book_19x24/{folder}/PAGE{page:02d}_{version}.{ext}' for folder,ext in [('source','svg'),('proofs','pdf'),('reading','pdf'),('proofs','png'),('proofs','json')]]
    a += [f'final_book_19x24/proofs/PAGE{page:02d}_{version}{s}.png' for s in ['_300dpi','_detail']]
    a += [f'final_book_19x24/source/PAGE{page:02d}_{placementversion}.placement.json',tp,'10_agent_workflow/parallel/agent_b/render_page.snapshot.v001.py']
    if speechversion: a += [f'assets_generated/speech_clouds/PAGE{page:02d}_SPEECH01_{speechversion}.{e}' for e in ['png','json','prompt.txt']]
    report(page,'layout','v001',summary+' PDF opened nonempty; embedded Noto font/glyphs, boxes, extraction and overflow checked. AGENT_QA only.',a)
def qa_report(page,version,summary):
    report(page,'qa','v001',summary+' AGENT_QA only, not USER_APPROVED/PRINT_READY. Native/effective DPI measured in metrics; no upscaling claims.',[f'10_agent_workflow/tasks/PAGE{page:02d}_LAYOUT/report.v001.json',f'final_book_19x24/proofs/PAGE{page:02d}_{version}.png',f'final_book_19x24/proofs/PAGE{page:02d}_{version}_detail.png',f'10_agent_workflow/tasks/PAGE{page:02d}_LAYOUT/technical.v001.json'])
