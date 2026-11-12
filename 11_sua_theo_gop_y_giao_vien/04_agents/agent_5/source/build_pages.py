#!/usr/bin/env python3
"""Rebuild typeset comic page from retained edited art and editable text JSON.

Run with python3 source/build_pages.py 18 [19 20 21]. Coordinates use the
original 896 x 1200 canvas. No character, costume or flag is drawn in code.
"""
from pathlib import Path
import sys, json, re, hashlib
from reportlab.pdfgen import canvas
from reportlab import rl_config
# Binary Flate streams keep PDFs compact and correctly recognized as binary by git.
rl_config.useA85 = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz

LANE = Path(__file__).resolve().parents[1]
FONT_DIR = LANE / 'source/fonts'
pdfmetrics.registerFont(TTFont('NotoSans', str(FONT_DIR/'NotoSans-Regular.ttf')))
pdfmetrics.registerFont(TTFont('NotoSansBold', str(FONT_DIR/'NotoSans-Bold.ttf')))
W, H = 896, 1200
PW, PH = 430.08, 576

def width(text, font, size):
    return pdfmetrics.stringWidth(text, font, size)

def wrap(text, font, size, limit):
    # Nonbreaking spaces in JSON lock names and fixed expressions.
    words = text.split(' ')
    lines, current = [], ''
    for word in words:
        trial = (current+' '+word).strip()
        if current and width(trial, font, size) > limit:
            lines.append(current); current = word
        else:
            current = trial
    if current: lines.append(current)
    # Balance short final lines without splitting names or fixed expressions.
    if len(lines)>1:
        while width(lines[-1],font,size)<limit*.40:
            prev=lines[-2].rsplit(' ',1)
            if len(prev)!=2 or len(prev[0].split(' '))<3: break
            trial=prev[1]+' '+lines[-1]
            if width(trial,font,size)>limit: break
            lines[-2],lines[-1]=prev[0],trial
    return lines

def draw_text(c, block):
    x,y,w,h = block['box']
    font=block.get('font','NotoSansBold')
    size=block.get('size',18)
    while True:
        lines=wrap(block['text'],font,size,w)
        leading=size*block.get('leading_ratio',1.30)
        if len(lines)*leading<=h: break
        size-=0.25
        if size<12: raise ValueError('Text too small: '+block['text'])
    baseline=y+(h-len(lines)*leading)/2+size
    red_ranges=[]
    normalized=block['text'].replace('\u00a0',' ')
    for phrase in block.get('red',[]):
        phrase=phrase.replace('\u00a0',' ')
        start=normalized.find(phrase)
        if start<0: raise ValueError('Red phrase not found: '+phrase)
        red_ranges.append((start,start+len(phrase)))
    c.setFont(font,size)
    cursor=0
    for line in lines:
        start=x+(w-width(line,font,size))/2
        line_offset=block['text'].find(line,cursor)
        if line_offset<0: raise ValueError('Unable to map wrapped line')
        segments=[]
        for i,ch in enumerate(line):
            is_red=any(a<=line_offset+i<b for a,b in red_ranges)
            if segments and segments[-1][0]==is_red:
                segments[-1][1]+=ch
            else:segments.append([is_red,ch])
        for is_red,token in segments:
            color=(.67,.16,.12) if is_red else (.10,.09,.07)
            c.setFillColorRGB(*color)
            c.drawString(start,H-baseline,token)
            start+=width(token,font,size)
        cursor=line_offset+len(line)
        baseline+=leading
    return {'font_size_px':size,'line_count':len(lines),'lines':lines,'box':block['box']}

def build(page):
    stem=f'PDF_{page:02}'
    text_path=LANE/'text'/f'{stem}.json'
    data=json.loads(text_path.read_text())
    art=LANE/'source'/f'{stem}_art.png'
    out=LANE/'output'/f'{stem}.pdf'
    c=canvas.Canvas(str(out),pagesize=(PW,PH))
    c.setTitle(f'Trưng Nữ Vương - trang PDF {page} - sửa góp ý giáo viên')
    c.scale(PW/W,PH/H)
    c.drawImage(str(art),0,0,width=W,height=H,preserveAspectRatio=True,anchor='c')
    metrics=[draw_text(c,b) for b in data['layout_blocks']]
    c.showPage();c.save()
    with fitz.open(out) as pdf:
        # Source-level resolution; no claim of 300 DPI or generated detail gain.
        pix=pdf[0].get_pixmap(matrix=fitz.Matrix(W/PW,H/PH),alpha=False)
        pix.save(LANE/'output'/f'{stem}.png')
        pdf[0].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(LANE/'qa'/f'{stem}_render.png')
    (LANE/'qa'/f'{stem}_typography.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n')
    print(stem, 'built', out)

if __name__=='__main__':
    for page in map(int,sys.argv[1:] or ['18','19','20','21']):build(page)
    paths=[LANE/'output'/f'PDF_{p:02}.pdf' for p in [18,19,20,21]]
    if all(p.exists() for p in paths):
        with fitz.open() as batch:
            for path in paths:
                with fitz.open(path) as page:batch.insert_pdf(page)
            batch.set_metadata({'title':'Trưng Nữ Vương - lô sửa PDF18-21 - Agent 5',
                                'author':'Agent 5','subject':'Bản sửa góp ý giáo viên; chờ coordinator rà liên trang'})
            batch.save(LANE/'output/LO_TRANG.pdf',garbage=4,deflate=True)
        print('LO_TRANG.pdf assembled in order 18,19,20,21')
