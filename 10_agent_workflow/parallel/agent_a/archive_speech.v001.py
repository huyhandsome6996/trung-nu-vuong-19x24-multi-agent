import sys,json,shutil,hashlib
from pathlib import Path
from PIL import Image
page,idx,ver,src,review=sys.argv[1:];stem=f'PAGE{int(page):02d}_SPEECH{int(idx):02d}'
p=Path(f'assets_generated/speech_clouds/{stem}_{ver}.png');assert not p.exists();shutil.copyfile(src,p)
with Image.open(p) as im:im.verify()
d=json.loads(Path(f'assets_generated/speech_clouds/{stem}_request.{ver}.json').read_text());d.update(image=str(p),status='visual_text_verified',native_size_px=list(Image.open(p).size),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),visual_review=review,user_approved=False,print_ready=False);p.with_suffix('.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
