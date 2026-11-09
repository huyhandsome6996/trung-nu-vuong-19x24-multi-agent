#!/usr/bin/env python3
"""Render a locked page to editable SVG, vector-text PDF and trimmed reading PDF.

Coordinates are trim-relative millimetres. Output is a proof, never PDF/X or print approval.
Native art is uniformly scaled with a centred crop; it is never stretched or relabelled native.
"""
import argparse
import base64
import html
import json
import re
from pathlib import Path

from PIL import Image
from fontTools.ttLib import TTFont as FontToolsFont
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import workflow as w


def run(text_path, raw_path, version, placement_path=None):
    data = w.read(text_path)
    if data['status'] != 'locked' or data['dialogues_status'] != 'locked':
        raise ValueError('Locked text and complete dialogues required')
    tokens = w.read('09_design_system/layout_components/layout_tokens.json')
    page = data['page']; stem = f'PAGE{page:02d}_{version}'
    paths = {k: w.local(f'final_book_19x24/{folder}/{stem}.{ext}') for k, folder, ext in [
        ('svg','source','svg'),('pdf','proofs','pdf'),('reading','reading','pdf'),('metrics','proofs','json')]}
    if any(p.exists() for p in paths.values()):
        raise ValueError('Use a new version; existing output is immutable')
    for p in paths.values(): p.parent.mkdir(parents=True, exist_ok=True)
    fonts = w.local('final_book_19x24/source/fonts')
    cmap = set()
    for name, file in [('TNRegular','NotoSans-Regular.ttf'),('TNBold','NotoSans-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(fonts/file)))
        ft=FontToolsFont(fonts/file); cmap.update(ft.getBestCmap()); ft.close()
    missing = sorted({c for c in data['narration']+''.join(d['text'] for d in data['dialogues']) if not c.isspace() and ord(c) not in cmap})
    if missing: raise ValueError('Missing glyphs: '+repr(missing))
    width, height = tokens['bleed_canvas_mm']
    c = canvas.Canvas(str(paths['pdf']), pagesize=(width*mm,height*mm), pageCompression=1, initialFontName='TNRegular')
    c.setTitle(f'TRƯNG NỮ VƯƠNG — trang {page:02d} — bản kiểm')
    c.setAuthor('TRƯNG NỮ VƯƠNG production')
    iw, ih = Image.open(w.local(raw_path)).size
    scale = max(width/iw,height/ih); aw, ah = iw*scale, ih*scale
    crop_x, crop_y = (aw-width)/2,(ah-height)/2
    png64=base64.b64encode(w.local(raw_path).read_bytes()).decode()
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="196mm" height="246mm" viewBox="0 0 196 246"><defs><style>@font-face{{font-family:TNRegular;src:url(fonts/NotoSans-Regular.ttf)}}@font-face{{font-family:TNBold;src:url(fonts/NotoSans-Bold.ttf)}}</style><radialGradient id="paper"><stop offset="0" stop-color="#FFFBEB"/><stop offset=".75" stop-color="#FEF3C7"/><stop offset="1" stop-color="#F59E0B"/></radialGradient></defs>']
    spec=w.read(placement_path) if placement_path else {}
    panel_metrics=[]
    if spec.get('art_panels'):
        # Explicit, manually reviewed placement crops. Native bitmap is kept unchanged.
        for i,panel in enumerate(spec['art_panels']):
            sx,sy,ex,ey=panel['source_crop_px'];dx,dy,dw,dh=panel['bbox_mm']
            if not (0<=sx<ex<=iw and 0<=sy<ey<=ih):raise ValueError('Invalid art crop')
            ps=max(dw/(ex-sx),dh/(ey-sy))
            px=dx+3-sx*ps-((ex-sx)*ps-dw)/2
            py=dy+3-sy*ps-((ey-sy)*ps-dh)/2
            c.saveState();clip=c.beginPath();clip.rect((dx+3)*mm,(height-dy-dh-3)*mm,dw*mm,dh*mm);c.clipPath(clip,stroke=0,fill=0)
            c.drawImage(str(w.local(raw_path)),px*mm,(height-py-ih*ps)*mm,width=iw*ps*mm,height=ih*ps*mm)
            c.restoreState()
            svg.append(f'<defs><clipPath id="art{i}"><rect x="{dx+3}" y="{dy+3}" width="{dw}" height="{dh}"/></clipPath></defs><image clip-path="url(#art{i})" x="{px}" y="{py}" width="{iw*ps}" height="{ih*ps}" href="data:image/png;base64,{png64}"/>')
            panel_metrics.append({'source_crop_px':[sx,sy,ex,ey],'bbox_mm':[dx,dy,dw,dh],'effective_dpi':25.4/ps,'uniform_scale':True})
    else:
        c.drawImage(str(w.local(raw_path)),-crop_x*mm,-crop_y*mm,width=aw*mm,height=ah*mm)
        svg.append(f'<image x="{-crop_x}" y="{-crop_y}" width="{aw}" height="{ah}" href="data:image/png;base64,{png64}"/>')
    if data['template']=='B':
        # The scene must already have a visually checked matching seam; this is a geometric edge.
        gutter_y,gutter_h=spec.get('gutter_mm',[128,3.5])
        if not (80<=gutter_y<=190 and 2<=gutter_h<=5):raise ValueError('Invalid reviewed gutter variant')
        gy0=gutter_y+3;gy1=gy0+gutter_h
        c.setFillColor('#FFFFFF');c.rect(0,(height-gy1)*mm,width*mm,gutter_h*mm,fill=1,stroke=0)
        c.setStrokeColor('#1A1A1A');c.setLineWidth(.3*mm)
        for gy in [gy0,gy1]:c.line(0,(height-gy)*mm,width*mm,(height-gy)*mm)
        svg.append(f'<rect x="0" y="{gy0}" width="196" height="{gutter_h}" fill="white"/><path d="M0 {gy0}H196 M0 {gy1}H196" stroke="#1A1A1A" stroke-width=".3"/>')
    # The existing parchment path is in trim-relative coordinates; shift it by the bleed.
    parchment=w.local('09_design_system/layout_components/parchment_blank.svg').read_text()
    pth=re.search(r'<path d="([^"]+)"',parchment)[1]
    svg.append(f'<path transform="translate(3 3)" d="{pth}" fill="url(#paper)" stroke="#1C1917" stroke-width=".7"/>')
    # PDF parchment uses the same polygon, with subtle nested fill gradation.
    points=[(float(a),float(b)) for a,b in re.findall(r'[ML]([\d.]+) ([\d.]+)',pth)]
    p=c.beginPath()
    for i,(x,y) in enumerate(points):
        (p.moveTo if i==0 else p.lineTo)((x+3)*mm,(height-y-3)*mm)
    p.close();c.setFillColor('#FEF3C7');c.setStrokeColor('#1C1917');c.setLineWidth(.7*mm);c.drawPath(p,fill=1,stroke=1)
    metrics={'page':page,'version':version,'print_ready':False,'user_approved':False,'renderer':'ReportLab / vector text; PDF rendered separately with Poppler','native_size_px':[iw,ih],'art_effective_dpi':[iw/(aw/25.4),ih/(ah/25.4)],'crop_mm':[crop_x,crop_y],'missing_glyphs':missing,'boxes':[]}
    if panel_metrics:
        metrics['manual_panel_placements']=panel_metrics
        metrics['art_effective_dpi']=[p['effective_dpi'] for p in panel_metrics]

    def draw_text(marked,bbox,pt,leading,kind):
        x,y,bw,bh=bbox
        parts=marked.split('**'); words=[]
        for i,part in enumerate(parts):
            for token in re.findall(r'\s+|\S+',part):words.append((' ' if token.isspace() else token,'TNBold' if i%2 else 'TNRegular','#C81E1E' if i%2 else '#1A1A1A'))
        lines=[];line=[];used=0
        for token,font,col in words:
            tw=pdfmetrics.stringWidth(token,font,pt)/mm
            if used+tw>bw and line:
                while line and line[-1][0].isspace():line.pop()
                lines.append(line);line=[];used=0
            if token.isspace() and not line:continue
            if tw>bw:raise ValueError('Unbreakable token too wide')
            line.append((token,font,col,tw));used+=tw
        if line:lines.append(line)
        required=len(lines)*leading/mm
        if required>bh:raise ValueError(f'{kind}: {required:.2f}mm text exceeds {bh}mm box')
        if kind=='narration' and not 3<=len(lines)<=5:raise ValueError('Narration must occupy 3–5 lines')
        # Baseline includes ascent/descent, so accents remain inside the measured box.
        baseline=y+(bh-required)/2+pdfmetrics.getAscent('TNRegular')*pt/1000/mm
        for line in lines:
            lw=sum(a[3] for a in line);xx=x+(bw-lw)/2
            for token,font,col,tw in line:
                c.setFont(font,pt);c.setFillColor(col);c.drawString((xx+3)*mm,(height-baseline-3)*mm,token)
                svg.append(f'<text x="{xx+3:.5f}" y="{baseline+3:.5f}" font-family="{font}" font-size="{pt/mm:.5f}" fill="{col}" xml:space="preserve">{html.escape(token)}</text>')
                xx+=tw
            baseline+=leading/mm
        metrics['boxes'].append({'kind':kind,'bbox_mm':bbox,'font_pt':pt,'lines':len(lines),'text_height_mm':required,'max_width_mm':max(sum(a[3] for a in line) for line in lines),'overflow':False})

    draw_text(data['narration'],tokens['narration_text_mm'],12.8,12.8*1.42,'narration')
    placements=w.read(placement_path)['dialogues'] if placement_path else data['dialogues']
    if len(placements)!=len(data['dialogues']):raise ValueError('Speech placement count mismatch')
    safe=tokens['safe_odd_mm' if page%2 else 'safe_even_mm'];sx,sy,sw,sh=safe
    for i,(dialogue,placement) in enumerate(zip(data['dialogues'],placements)):
        bx,by,bw,bh=placement['bbox_mm'];tx,ty=placement['tail_mm']
        if not(sx<=bx and sy<=by and bx+bw<=sx+sw and by+bh<=sy+sh):raise ValueError('Speech outside safe zone')
        cx=bx+bw/2;cy=by+bh/2
        letter=placement.get('style')=='letter'
        p=c.beginPath();p.moveTo((cx)*mm+3*mm,(height-cy-3)*mm);p.lineTo((tx+3)*mm,(height-ty-3)*mm);p.lineTo((cx+6+3)*mm,(height-cy-3)*mm);p.close()
        fill='#FFF8DD' if letter else '#FFFFFF';radius=1 if letter else 6
        c.setFillColor(fill);c.setStrokeColor('#1A1A1A');c.setLineWidth(.4*mm)
        if not letter:
            c.drawPath(p,fill=1,stroke=1)
            svg.append(f'<path d="M{cx+3} {cy+3} L{tx+3} {ty+3} L{cx+9} {cy+3}Z" fill="white" stroke="#1A1A1A" stroke-width=".4"/>')
        c.roundRect((bx+3)*mm,(height-by-bh-3)*mm,bw*mm,bh*mm,radius*mm,fill=1,stroke=1)
        svg.append(f'<rect x="{bx+3}" y="{by+3}" width="{bw}" height="{bh}" rx="{radius}" fill="{fill}" stroke="#1A1A1A" stroke-width=".4"/>')
        draw_text(dialogue['text'],[bx+3,by+2.5,bw-6,bh-5],10.8,13.2,f'speech_{i}')
    fx,fy=tokens['folio_center_odd_mm' if page%2 else 'folio_center_even_mm'];radius=4
    c.setFillColor('#991B1B');c.setStrokeColor('#D4A649');c.setLineWidth(.35*mm);c.circle((fx+3)*mm,(height-fy-3)*mm,radius*mm,fill=1,stroke=1)
    c.setFillColor('#E6B95C');c.setFont('TNBold',10);c.drawCentredString((fx+3)*mm,(height-fy-3)*mm-3.5,str(page))
    svg.append(f'<circle cx="{fx+3}" cy="{fy+3}" r="4" fill="#991B1B" stroke="#D4A649" stroke-width=".35"/><text x="{fx+3}" y="{fy+4.23}" text-anchor="middle" font-family="TNBold" font-size="{10/mm}" fill="#E6B95C">{page}</text></svg>')
    c.save();paths['svg'].write_text(''.join(svg),encoding='utf-8')
    reader=PdfReader(paths['pdf']);pg=reader.pages[0]
    pg.trimbox=RectangleObject([3*mm,3*mm,193*mm,243*mm]);pg.bleedbox=RectangleObject([0,0,width*mm,height*mm])
    writer=PdfWriter();writer.add_page(pg)
    atomic=paths['pdf'].with_suffix('.pdf.tmp')
    with atomic.open('wb') as f:writer.write(f)
    atomic.replace(paths['pdf'])
    pg.cropbox=pg.trimbox
    writer=PdfWriter();writer.add_page(pg)
    with paths['reading'].open('wb') as f:writer.write(f)
    extracted=PdfReader(paths['pdf']).pages[0].extract_text()
    normalize=lambda s:re.sub(r'\s+','',s.replace('**',''))
    if normalize(data['narration']) not in normalize(extracted):raise ValueError('PDF text differs from locked narration')
    metrics['pdf_text_matches']=True
    metrics['hashes']={k:w.digest(v.relative_to(w.ROOT)) for k,v in paths.items() if k!='metrics'}
    paths['metrics'].write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n')
    for p in paths.values():print(p.relative_to(w.ROOT))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--text',required=True);p.add_argument('--raw',required=True);p.add_argument('--version',default='v001');p.add_argument('--placements');a=p.parse_args()
    run(a.text,a.raw,a.version,a.placements)
