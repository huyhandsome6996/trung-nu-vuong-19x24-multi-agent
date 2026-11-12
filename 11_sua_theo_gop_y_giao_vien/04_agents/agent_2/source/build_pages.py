#!/usr/bin/env python3
"""Rebuild typeset pages from saved, imagegen-edited art and final text.

Only narration typography is authored here; costume and flag corrections are
in the supplied edited_art.png files, produced with original-page references.
"""
from pathlib import Path
import argparse
import hashlib
import io
import json
import re
from PIL import Image, ImageDraw, ImageFont, ImageOps
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config
import fitz

rl_config.useA85 = 0

LANE = Path(__file__).resolve().parents[1]
FONT = LANE / 'source/fonts/NotoSans-Bold.ttf'
PAGE = (430.08, 576)
SCALE = .48


def tokens(value):
    out = []
    for span in value['rich_text']:
        for word in span['text'].split():
            out.append((word, span.get('color', '#171611')))
    return out


def lines_for(words, font, width):
    # Bind names and fixed expressions, avoiding isolated final syllables.
    phrases = ['mạc khách họ Kiều', 'Lão trượng họ Khúc', 'Thi Sách', 'Lữ Thạch', 'Mã Tắc', 'Đinh Lương', 'Chu Diên',
               'Lạc hầu', 'Hồng Bàng', 'Mãnh long giáng địa', 'Lĩnh Nam']
    grouped = []
    i = 0
    while i < len(words):
        for phrase in phrases:
            n = len(phrase.split())
            if i+n <= len(words) and ' '.join(x[0] for x in words[i:i+n]).strip('“”\"!.,:;') == phrase and len({x[1] for x in words[i:i+n]}) == 1:
                grouped.append((' '.join(x[0] for x in words[i:i+n]), words[i][1]))
                i += n
                break
        else:
            grouped.append(words[i]); i += 1
    lines, line = [], []
    for word in grouped:
        trial = ' '.join(x[0] for x in line+[word])
        if line and font.getlength(trial) > width:
            lines.append(line); line=[]
        line.append(word)
    if line: lines.append(line)
    if len(lines[-1]) == 1 and len(lines) > 1:
        lines[-1].insert(0, lines[-2].pop())
    return lines


def build(page):
    stem = f'PDF_{page:02}'
    src = LANE/'source'/stem
    text = json.loads((LANE/'text'/f'{stem}.json').read_text())
    layout = json.loads((src/'layout.json').read_text())
    original = Image.open(src/'edited_art.png').convert('RGB')
    # Crop at most a few edge pixels to original aspect, then downsample.
    image = ImageOps.fit(original, (896,1200), method=Image.Resampling.LANCZOS)
    x0,y0,x1,y1 = layout['box']
    draw = ImageDraw.Draw(image)
    if layout.get('redraw_box'):
        draw.rounded_rectangle((x0,y0,x1,y1), radius=24,
                               fill='#F4E6AA', outline='#201F16', width=3)
    size = layout.get('font_size', 19.5)
    font = ImageFont.truetype(str(FONT), size=size)
    lines = lines_for(tokens(text),font,x1-x0-2*layout.get('horizontal_padding',19))
    advance = layout.get('line_height', 26)
    total = len(lines)*advance
    assert total <= y1-y0-24, (stem,len(lines),total,y1-y0)
    top = y0+(y1-y0-total)/2
    runs = []
    for row,line in enumerate(lines):
        width = font.getlength(' '.join(w for w,c in line))
        x = (x0+x1-width)/2
        y = top+row*advance
        for j,(word,color) in enumerate(line):
            chunk=word+(' ' if j<len(line)-1 else '')
            draw.text((x,y),chunk,font=font,fill=color,anchor='lt')
            runs.append({'text':chunk,'x':x,'y':y,'color':color})
            x += font.getlength(chunk)
    out = LANE/'output'; qa=LANE/'qa'
    out.mkdir(exist_ok=True); qa.mkdir(exist_ok=True)
    image.save(out/f'{stem}.png')
    # PDF retains real selectable Vietnamese text atop exactly the same art.
    background = ImageOps.fit(original,(896,1200),method=Image.Resampling.LANCZOS)
    if layout.get('redraw_box'):
        ImageDraw.Draw(background).rounded_rectangle((x0,y0,x1,y1),radius=24,fill='#F4E6AA',outline='#201F16',width=3)
    background.save(src/'typesetting_background.png')
    pdfmetrics.registerFont(TTFont('Narration',str(FONT)))
    c=canvas.Canvas(str(out/f'{stem}.pdf'),pagesize=PAGE,pageCompression=1)
    c.setTitle(f'Trưng Nữ Vương - {stem} - sửa giáo viên')
    c.setAuthor('Agent 2')
    c.drawImage(ImageReader(background),0,0,width=PAGE[0],height=PAGE[1])
    c.setFont('Narration',size*SCALE)
    # Align using actual font ascent so PNG/PDF start at the same top.
    ascent=pdfmetrics.getAscent('Narration')/1000*size
    for run in runs:
        c.setFillColor(run['color'])
        c.drawString(run['x']*SCALE,PAGE[1]-(run['y']+ascent)*SCALE,run['text'])
    c.showPage(); c.save()
    # Binary compressed serialization avoids treating generated PDF as text
    # during Git whitespace checks and keeps font/image streams compact.
    pdf_path=out/f'{stem}.pdf'
    with fitz.open(pdf_path) as raw:
        binary=raw.tobytes(garbage=4,deflate=True,deflate_fonts=True,deflate_images=True)
    pdf_path.write_bytes(binary)
    with fitz.open(out/f'{stem}.pdf') as pdf:
        pix = pdf[0].get_pixmap(matrix=fitz.Matrix(1/SCALE,1/SCALE),alpha=False)
        pix.save(qa/f'{stem}_render.png')
        pix.save(out/f'{stem}.png')
        extracted=pdf[0].get_text()
    report={'pdf_page':page,'input_art_pixels':list(original.size),
            'output_pixels':[896,1200],'media_box_pt':list(PAGE),
            'font_size_px':size,'lines':[' '.join(w for w,c in ln) for ln in lines],
            'pdf_extracted_text':extracted,
            'art_sha256':hashlib.sha256((src/'edited_art.png').read_bytes()).hexdigest(),
            'print_note':'No 300 DPI claim; original source 896×1200 px. AI edit can introduce local stroke drift.'}
    (qa/f'{stem}_technical.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(stem,original.size,len(lines),'lines',report['lines'])


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('pages',nargs='*',type=int,default=[6,7,8,9])
    args=parser.parse_args()
    for p in args.pages: build(p)
    if all((LANE/'output'/f'PDF_{p:02}.pdf').exists() for p in [6,7,8,9]):
        combined=fitz.open()
        for p in [6,7,8,9]:
            with fitz.open(LANE/'output'/f'PDF_{p:02}.pdf') as item: combined.insert_pdf(item)
        combined.save(LANE/'output/LO_TRANG.pdf',garbage=4,deflate=True)
