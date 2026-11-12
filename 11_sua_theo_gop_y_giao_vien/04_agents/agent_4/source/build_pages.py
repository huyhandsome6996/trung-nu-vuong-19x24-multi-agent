#!/usr/bin/env python3
"""Rebuild typeset comic page from retained edited art and editable text JSON.

Run with python3 source/build_pages.py 15 [16 17]. Coordinates use the
original 896 x 1200 canvas. No character, costume or flag is drawn in code.
"""
from pathlib import Path
import sys, json, re, hashlib
from reportlab.pdfgen import canvas
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
    if len(lines)>1 and len(lines[-1].split()) == 1:
        prev = lines[-2].rsplit(' ',1)
        if len(prev)==2 and width(prev[1]+' '+lines[-1],font,size)<=limit:
            lines[-2],lines[-1]=prev[0],prev[1]+' '+lines[-1]
    return lines

def draw_text(c, block):
    x,y,w,h = block['box']
    font=block.get('font','NotoSansBold')
    size=block.get('size',18)
    while True:
        lines=wrap(block['text'],font,size,w)
        leading=size*1.30
        if len(lines)*leading<=h: break
        size-=0.25
        if size<12: raise ValueError('Text too small: '+block['text'])
    baseline=y+(h-len(lines)*leading)/2+size
    red=set()
    for phrase in block.get('red',[]):
        red.update(phrase.replace('\u00a0',' ').split())
    c.setFont(font,size)
    for line in lines:
        start=x+(w-width(line,font,size))/2
        for token in re.findall(r'\S+|\s+',line):
            color=(.67,.16,.12) if token.strip() in red else (.10,.09,.07)
            c.setFillColorRGB(*color)
            c.drawString(start,H-baseline,token)
            start+=width(token,font,size)
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
    c.drawImage(str(art),0,0,width=W,height=H)
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
    for page in map(int,sys.argv[1:]):build(page)
