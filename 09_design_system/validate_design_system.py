"""Validate local design registry, references and generated asset integrity (not visual QA)."""
from pathlib import Path
import hashlib,json,re,sys
from xml.etree import ElementTree
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'09_design_system'
errors=[]
def check(ok,message):
    if not ok:errors.append(message)
reg=json.loads((D/'design_registry.json').read_text())
jobs=json.loads((D/'image_jobs.json').read_text())
pages=json.loads((D/'page_asset_matrix.json').read_text())
for key in ['characters','environments','props','animals']:
    ids=[x['id'] for x in reg[key]]
    check(len(ids)==len(set(ids)),f'duplicate IDs: {key}')
cids={x['id'] for x in reg['characters']};eids={x['id'] for x in reg['environments']};pids={x['id'] for x in reg['props']};aids={x['id'] for x in reg['animals']}
job_ids={j['id'] for j in jobs}
check(len(job_ids)==len(jobs),'duplicate image job IDs')
crowd=json.loads((D/'crowd_registry.json').read_text())
check(len(crowd)==24 and len({c['id'] for c in crowd})==24,'expected 24 unique collective faces')
check(len({(c['row'],c['column']) for c in crowd})==24,'duplicate face cell')
for c in crowd:check(1<=c['row']<=4 and 1<=c['column']<=6,'face cell outside grid')
check(len(cids)==41,'expected 41 character profiles')
for c in reg['characters']:
    check((D/'characters'/f"{c['id']}.md").exists(),f"missing profile {c['id']}")
    check(set(c['props'])<=pids|aids,f"unknown prop for {c['id']}")
    check(c['board']=='CHAR01' or c['board'] in job_ids,f"unknown casting board {c['id']}")
for e in reg['environments']:check(e['board'] in job_ids,f"missing environment board {e['id']}")
check([p['page'] for p in pages]==list(range(1,29)),'page range')
for p in pages:
    for field,allowed in [('characters',cids),('environments',eids),('props',pids)]:
        check(set(p[field])<=allowed,f"page {p['page']} unknown {field}")
for j in jobs:
    for f in j['reference_paths']:check((ROOT/f).exists(),f"missing image reference {f}")
    check((D/'prompts'/f"{j['id']}.md").exists(),f"missing prompt {j['id']}")
    if j['status']=='GENERATED':
        path=ROOT/j['output']
        check(path.exists(),f"missing generated {path}")
        if path.exists():
            try:
                with Image.open(path) as im:im.load();size=im.size
                meta=json.loads(path.with_suffix('.json').read_text())
                check(size==(meta['width'],meta['height']),f"wrong dimensions {j['id']}")
                check(hashlib.sha256(path.read_bytes()).hexdigest()==meta['sha256'],f"hash mismatch {j['id']}")
                check(meta['print_ready'] is False,f"concept mislabelled print-ready {j['id']}")
                check(meta['version']==path.stem.rsplit('_',1)[-1],f"wrong version metadata {j['id']}")
                check(meta['user_approved'] is False,f"unrecorded user approval {j['id']}")
            except Exception as e:errors.append(f"asset error {j['id']}: {e}")
for path in D.rglob('*.svg'):
    try:ElementTree.parse(path)
    except Exception as e:errors.append(f'invalid SVG {path}: {e}')
for path in list(D.rglob('*.md'))+list((ROOT/'08_project_memory').glob('*.md')):
    text=path.read_text()
    check(re.search(r'gh[pousr]_[A-Za-z0-9]{20,}',text) is None,f'credential-like text in {path}')
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
        if '://' not in target and not target.startswith('#'):
            check((path.parent/target.split('#')[0]).exists(),f'broken link {path.name}: {target}')
remaining=[j['id'] for j in jobs if j['status']!='GENERATED']
if '--complete' in sys.argv:check(not remaining,'not generated: '+','.join(remaining))
if errors:
    print('\n'.join('FAIL '+e for e in errors));raise SystemExit(1)
print(f'PASS {len(cids)} profiles; {len(eids)} environments; {len(pids)} props; {len(aids)} animals; {len(pages)} pages mapped; {len(jobs)-len(remaining)}/{len(jobs)} new image jobs generated')
print('Visual QA, user approval, historical verification and print production are separate checks.')
