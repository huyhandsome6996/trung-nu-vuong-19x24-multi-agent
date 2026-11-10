"""Archive native image, exact request metadata and explicit visual review without task mutation."""
import sys,json,shutil,hashlib
from pathlib import Path
from PIL import Image
page,version,source,review=sys.argv[1:]
p=int(page);dest=Path(f'assets_generated/raw_pages/PAGE{p:02d}_{version}.png')
assert not dest.exists();shutil.copyfile(source,dest)
with Image.open(dest) as im:im.verify()
req=json.loads(Path(f'10_agent_workflow/tasks/PAGE{p:02d}_ART/generation_request.{version}.json').read_text())
rp=Path(f'10_agent_workflow/tasks/PAGE{p:02d}_ART/VISUAL_REVIEW.{version}.md');assert not rp.exists();rp.write_text(review+'\n')
meta=dict(image=dest.as_posix(),version=version,native_size_px=list(Image.open(dest).size),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),prompt=req['prompt'],actual_references=req['actual_references'],generator='image_gen.imagegen (model not exposed)',text_free=True,top_clearance_checked=True,visual_qa_report=rp.as_posix(),user_approved=False,print_ready=False)
dest.with_suffix('.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
