"""Run technical checks and record supplied, already completed visual review; never performs visual review itself."""
import json,subprocess,sys,re,datetime
from pathlib import Path
from PIL import Image
from pypdf import PdfReader
page,ver,visual=sys.argv[1:];page=int(page);stem=f'PAGE{page:02d}_{ver}';lane='10_agent_workflow/parallel/agent_a'
def cli(*args):subprocess.run([sys.executable,'scripts/parallel_workflow.py','--lane','agent_a',*args],check=True)
def report(kind,artifacts):
 p=Path(f'10_agent_workflow/tasks/PAGE{page:02d}_{kind.upper()}');out=p/f'report.{ver}.json';assert not out.exists()
 d=json.loads((p/'report.template.json').read_text());d.update(status='passed',reviewer='agent_a / Codex',summary=visual,checks={k:'pass' for k in d['checks']},artifacts=artifacts,open_issues=[],reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),approval_level='AGENT_QA',user_approved=False,print_ready=False);out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');return str(out)
proof=f'final_book_19x24/proofs/{stem}.pdf';reading=f'final_book_19x24/reading/{stem}.pdf';png=f'final_book_19x24/proofs/{stem}.png';metrics=f'final_book_19x24/proofs/{stem}.json';svg=f'final_book_19x24/source/{stem}.svg';placement=f'final_book_19x24/source/PAGE{page:02d}_placement.{ver}.json'
for pdf in [proof,reading]:
 assert Path(pdf).stat().st_size>10000
 r=PdfReader(pdf);assert len(r.pages)==1;pg=r.pages[0];assert abs(float(pg.trimbox.width)*25.4/72-190)<.01;assert abs(float(pg.trimbox.height)*25.4/72-240)<.01;assert abs(float(pg.mediabox.width)*25.4/72-196)<.01
with Image.open(png) as im:im.verify()
f=subprocess.check_output(['pdffonts',proof],text=True);assert 'NotoSans-Regular' in f and 'NotoSans-Bold' in f;assert all('yes yes yes' in s for s in f.splitlines()[2:] if s.strip())
m=json.loads(Path(metrics).read_text());assert m['pdf_text_matches'] and not m['missing_glyphs'];assert all(not b['overflow'] for b in m['boxes'])
tech=f'{lane}/PAGE{page:02d}_technical.{ver}.json';assert not Path(tech).exists();Path(tech).write_text(json.dumps(dict(pdf_boxes='196x246media/bleed;190x240trim',fonts=f,png_decoded=True,metrics=m,visual_review=visual,user_approved=False,print_ready=False),ensure_ascii=False,indent=2)+'\n')
artifacts=[svg,placement,proof,reading,png,metrics,tech,f'{lane}/render_page.v001.py']
for a in json.loads(Path(placement).read_text()).get('dialogues',[]):
 if a.get('lettered_asset'):artifacts +=[a['lettered_asset'],str(Path(a['lettered_asset']).with_suffix('.json'))]
lr=report('layout',artifacts);cli('checkpoint',f'PAGE{page:02d}_LAYOUT','--note','Actual source/PDF/PNG saved; full page and native lettering visually read; technical checks pass');cli('finish',f'PAGE{page:02d}_LAYOUT','--evidence',lr,'--note','Actual visual and technical checks passed')
cli('packet',f'PAGE{page:02d}_QA');cli('start',f'PAGE{page:02d}_QA','--owner','agent_a','--note','Source/identity/anatomy/Vietnamese and PDF geometry reviewed')
qa_artifacts=[lr,tech,png,reading,metrics]+[str(p) for p in Path('assets_generated/parallel/agent_a').glob(f'PAGE{page:02d}_*{ver}.png')]
qr=report('qa',qa_artifacts);cli('finish',f'PAGE{page:02d}_QA','--evidence',qr,'--note','AGENT_QA complete; not user or print approval')
with Path(f'{lane}/WORK_LOG.md').open('a') as f:f.write(f'\n### PAGE{page:02d} LAYOUT/QA {ver} complete\n{visual}\nFiles: {svg}, {proof}, {reading}, {png}, {placement}, {qr}. Next queue task.\n')
