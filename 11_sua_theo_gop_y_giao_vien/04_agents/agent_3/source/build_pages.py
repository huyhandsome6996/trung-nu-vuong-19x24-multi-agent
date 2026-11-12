#!/usr/bin/env python3
"""Rebuild real-font PDF/PNG from immutable edited art masters and text JSON.
Only typography/its narration box is drawn here; costume/flag edits are image_gen.
"""
from pathlib import Path
import json, re, hashlib, shutil
import fitz
from reportlab import rl_config
rl_config.useA85 = 0  # Binary Flate streams; PDF is a binary Git artifact.
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
ROOT=Path(__file__).resolve().parents[1]
FONT=ROOT/'source/fonts/NotoSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('Narration',str(FONT)))
W,H=896,1200
S=.48
# Coordinates use the original 896x1200 grid.
LAYOUT={
 10:{'narration':[79,67,817,211], 'font':19.2,'leading':24,'box':[55,55,790,175]},
 11:{'narration':[91,77,805,218], 'font':19.2,'leading':24,'box':[67,62,760,178]},
 12:{'narration':[116,65,794,212], 'font':19.2,'leading':24,'box':[94,45,725,187]},
 13:{'narration':[80,65,821,259], 'font':22.5,'leading':29,
     'dialogue':{'Tào Quyền':[92,842,316,903,16,19], 'Tô Định':[368,804,580,875,16,19], 'Mã Tắc':[651,797,794,855,15,18]}},
 14:{'narration':[81,76,821,249], 'font':23,'leading':29,
     'dialogue':{'Trưng Trắc':[189,787,387,856,14,17], 'Trưng Nhị':[584,724,742,784,15,18]}}
}
def split_tokens(t):
    # Keep explicit proper names together during wrapping.
    for name in ['Phượng Hoàng','Tào Quyền','Đỗ Năng Tế','Trưng Trắc','Trưng Nhị','Thi Sách','Nguyễn Huyền','Hát Môn','Mã Tắc','Tô Định','Hùng Vương','non sông','chẳng lui','chị em']:
        t=t.replace(name,name.replace(' ','\u00a0'))
    return t.split(' ')
def wrap(text,font,size,width):
    lines=[];line=''
    for token in split_tokens(text):
        trial=(line+' '+token).strip()
        if pdfmetrics.stringWidth(trial,font,size)>width and line:
            lines.append(line);line=token
        else:line=trial
    if line:lines.append(line)
    return lines

def write_text(c,text,rect,size,leading,red=()):
    x0,y0,x1,y1=rect
    lines=wrap(text,'Narration',size,x1-x0)
    height=(len(lines)-1)*leading+size*1.2
    if height>y1-y0:raise ValueError(f'Text overflow: {height}, rect {rect}: {lines}')
    # Character-level coloring is driven by actual phrases, not line boundaries.
    normalized=text.replace('\u00a0',' ')
    red_spans=[]
    for phrase in red:
        for match in re.finditer(re.escape(phrase),normalized):red_spans.append(match.span())
    cursor=0
    y=y0+(y1-y0-height)/2+size*.97
    evidence=[]
    for line in lines:
        clean=line.replace('\u00a0',' ')
        idx=normalized.find(clean,cursor)
        if idx<0:raise ValueError('Line text mismatch '+clean)
        cursor=idx+len(clean)
        x=x0+((x1-x0)-pdfmetrics.stringWidth(line,'Narration',size))/2
        start=0
        colors=[any(a<=idx+i<b for a,b in red_spans) for i in range(len(line))]
        while start<len(line):
            end=start+1
            while end<len(line) and colors[end]==colors[start]:end+=1
            run=line[start:end]
            c.setFillColor(HexColor('#A52E24' if colors[start] else '#171612'))
            c.setFont('Narration',size)
            c.drawString(x,H-y,run)
            x+=pdfmetrics.stringWidth(run,'Narration',size);start=end
        evidence.append({'text':clean,'baseline_y':round(y,2)})
        y+=leading
    return {'font_px':size,'leading_px':leading,'rect_px':rect,'lines':evidence}

def build(page):
    d=json.loads((ROOT/f'text/PDF_{page:02}.json').read_text())
    cfg=LAYOUT[page]
    out=ROOT/f'output/PDF_{page:02}.pdf'
    c=canvas.Canvas(str(out),pagesize=(430.08,576),pageCompression=1)
    c.setTitle(f'Trưng Nữ Vương - PDF{page:02} - Agent 3')
    c.setAuthor('Agent 3 - sửa theo góp ý giáo viên')
    c.scale(S,S)
    c.drawImage(str(ROOT/f'source/PDF_{page:02}/art_master.png'),0,0,width=W,height=H)
    if 'box' in cfg:
        x,y,w,h=cfg['box'];c.setFillColor(HexColor('#F9EDBE'));c.setStrokeColor(HexColor('#171612'));c.setLineWidth(2.4)
        c.roundRect(x,H-y-h,w,h,26,fill=1,stroke=1)
    layout={'narration':write_text(c,d['narration'],cfg['narration'],cfg['font'],cfg['leading'],d['red_phrases']), 'dialogue':[]}
    for dia in d['dialogue']:
        r=cfg['dialogue'][dia['speaker']]
        layout['dialogue'].append({'speaker':dia['speaker'],'order':dia['order'],**write_text(c,dia['text'],r[:4],r[4],r[5])})
    c.showPage();c.save()
    (ROOT/f'source/PDF_{page:02}/layout.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
    with fitz.open(out) as pdf:
        # Final PNG and independent PDF review render, exact source aspect.
        pix=pdf[0].get_pixmap(matrix=fitz.Matrix(896/430.08,1200/576),alpha=False)
        pix.save(ROOT/f'output/PDF_{page:02}.png')
        pdf[0].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(ROOT/f'qa/PDF_{page:02}_render.png')
    print(f'Built PDF{page:02}:',len(layout['narration']['lines']),'narration lines')

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('pages',type=int,nargs='*',default=list(range(10,15)));args=ap.parse_args()
    for page in args.pages:build(page)
