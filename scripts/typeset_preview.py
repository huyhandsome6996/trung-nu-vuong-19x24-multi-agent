#!/usr/bin/env python3
"""Make a portable local HTML proof from locked text and a real text-free illustration.
This is a review aid, not a PDF/X exporter or an automatic print approval.
"""
import argparse
import base64
import html
import json
from pathlib import Path
import re
import sys
import workflow


def keywords(text):
    if text.count('**') % 2:
        raise ValueError('Unpaired red keyword marker')
    parts = text.split('**')
    return ''.join(f'<strong>{html.escape(p)}</strong>' if i % 2 else html.escape(p) for i, p in enumerate(parts))


def build(text_path, raw_path, out_path, font_path):
    from PIL import Image
    data = workflow.read(text_path)
    if data.get('status') != 'locked' or data.get('dialogues_status') != 'locked':
        raise ValueError('Use locked text/dialogues, not the packet draft')
    page = data['page']
    if not isinstance(page, int) or not 1 <= page <= 28:
        raise ValueError('Page must be 1–28')
    with Image.open(workflow.local(raw_path)) as im:
        size = im.size
        if abs(im.width / im.height - 196 / 246) > .015:
            raise ValueError('Background ratio needs manual crop/outpaint to bleed ratio first; no automatic face crop')
        fmt = im.format.lower()
    font = workflow.local(font_path)
    if font.suffix.lower() not in ['.ttf', '.otf', '.woff', '.woff2']:
        raise ValueError('Supply a real font file with Vietnamese glyphs and permitted use')
    tokens = workflow.read('09_design_system/layout_components/layout_tokens.json')
    x,y,w,h = tokens['narration_text_mm']
    parchment = workflow.local('09_design_system/layout_components/parchment_blank.svg').read_bytes()
    bg = base64.b64encode(workflow.local(raw_path).read_bytes()).decode()
    font64 = base64.b64encode(font.read_bytes()).decode()
    parchment64 = base64.b64encode(parchment).decode()
    bubbles=[]
    safe = tokens['safe_odd_mm' if page % 2 else 'safe_even_mm']
    sx,sy,sw,sh=safe
    for n,d in enumerate(data.get('dialogues', [])):
        if not all(k in d for k in ['speaker','text','bbox_mm','tail_mm']):
            raise ValueError('Each dialogue needs speaker/text/bbox_mm/tail_mm after visual placement')
        bx,by,bw,bh=d['bbox_mm']; tx,ty=d['tail_mm']
        if bw <= 0 or bh <= 0 or not (sx<=bx and sy<=by and bx+bw<=sx+sw and by+bh<=sy+sh):
            raise ValueError(f'Bubble {n} outside safe text zone')
        if not (sx<=tx<=sx+sw and sy<=ty<=sy+sh):
            raise ValueError(f'Bubble {n} tail outside safe zone')
        # SVG callout tail behind ellipse; tip is manually aimed toward the speaker.
        cx=bx+bw/2;cy=by+bh/2
        tail=f'<svg class="tail" viewBox="0 0 196 246"><path d="M {cx-3+3} {cy+3} L {tx+3} {ty+3} L {cx+3+3} {cy+3} Z" fill="white" stroke="#1A1A1A" stroke-width=".4"/></svg>'
        bubbles.append(tail + f'<div class="bubble fit" data-speaker="{html.escape(d["speaker"],quote=True)}" style="left:{bx+3}mm;top:{by+3}mm;width:{bw}mm;height:{bh}mm">{html.escape(d["text"])}</div>')
    fx,fy=tokens['folio_center_odd_mm' if page%2 else 'folio_center_even_mm']
    proof=f'''<!doctype html><html lang="vi"><meta charset="utf-8"><title>Trang{page:02d} — bản kiểm</title>
<style>
@font-face{{font-family:ProjectFont;src:url(data:font/{font.suffix[1:]};base64,{font64});font-weight:100 900}}
@page{{size:196mm 246mm;margin:0}}*{{box-sizing:border-box}}body{{margin:0;background:#bbb;font-family:ProjectFont,sans-serif}}
.page{{width:196mm;height:246mm;position:relative;overflow:hidden;background:white;margin:0 auto}}
.background{{position:absolute;width:100%;height:100%;object-fit:fill}}
.parchment{{position:absolute;left:14mm;top:11mm;width:168mm;height:40mm}}
.narration{{position:absolute;left:{x+3}mm;top:{y+3}mm;width:{w}mm;height:{h}mm;display:flex;align-items:center;justify-content:center;text-align:center;font-size:12.8pt;line-height:1.42;color:#1A1A1A}}
strong{{color:#C81E1E;font-weight:700}}.tail{{position:absolute;inset:0;width:196mm;height:246mm}}
.bubble{{position:absolute;border:.4mm solid #1A1A1A;border-radius:50%;background:#fff;padding:2.5mm;text-align:center;font-size:10.8pt;display:flex;align-items:center;justify-content:center}}
.folio{{position:absolute;left:{fx+3-4}mm;top:{fy+3-4}mm;width:8mm;height:8mm;border-radius:50%;background:#991b1b;color:#e6b95c;display:flex;align-items:center;justify-content:center;font-size:10pt}}
.overflow{{outline:1mm solid red}}#qa-status{{padding:12px;max-width:850px;margin:auto;background:#fff;font:14px sans-serif}}@media print{{body{{background:white}}#qa-status{{display:none}}}}
</style>
<div id="qa-status">Đang nạp font… Bản kiểm; chưa duyệt in. Nguồn ảnh{size[0]}×{size[1]}px. Kiểm tiếp glyph Việt, dòng chữ, mặt và bleed.</div>
<div class="page"><img class="background" src="data:image/{fmt};base64,{bg}" alt="Tranh nền"><img class="parchment" src="data:image/svg+xml;base64,{parchment64}" alt="">
<div class="narration fit"><div>{keywords(data['narration'])}</div></div>{''.join(bubbles)}<div class="folio">{page}</div></div>
<script>
document.fonts.ready.then(()=>{{const issues=[];document.querySelectorAll('.fit').forEach((e)=>{{if(e.scrollHeight>e.clientHeight+1||e.scrollWidth>e.clientWidth+1){{e.classList.add('overflow');issues.push(e.className)}}}});document.getElementById('qa-status').textContent=issues.length?'LỖI TRÀN CHỮ: '+issues.join(', '):'Không thấy tràn hộp bằng DOM. Vẫn phải mở kiểm chữ Việt, dòng3–5, mặt và toàn trang; chưa duyệt in.';}});
</script></html>'''
    out=workflow.local(out_path)
    if out.exists():
        raise ValueError('Output exists; use a new version filename')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(proof,encoding='utf-8')
    print(out.relative_to(workflow.ROOT))
    print('HTML proof only. Open in a real renderer; verify overflow, font glyphs, 3–5 lines and visual placement.')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--text',required=True);p.add_argument('--raw',required=True);p.add_argument('--out',required=True);p.add_argument('--font',required=True)
    a=p.parse_args();build(a.text,a.raw,a.out,a.font)

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,KeyError) as ex:print('ERROR:',ex,file=sys.stderr);sys.exit(1)
