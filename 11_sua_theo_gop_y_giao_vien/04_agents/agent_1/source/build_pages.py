#!/usr/bin/env python3
"""Deterministic layout from archived imagegen edits, protected source pixels and real text.

No code paints replacement flags, people or costumes: all edited art comes from
art_edit_raw.png. Masks composite that art and protect original faces/objects.
"""
from pathlib import Path
import argparse, json, hashlib, subprocess
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import fitz

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
PACK = LANE.parents[1]
SIZE = (896, 1200)
SCALE = 0.48
PT = (430.08, 576)
pdfmetrics.registerFont(TTFont('Narration', str(HERE/'fonts/NotoSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Footnote', str(HERE/'fonts/NotoSans-Italic.ttf')))

# Coordinates are in original source pixels. White selects reference-edited art.
# Polygons protect the exact source faces, hair, hands, weapons and other objects.
REGIONS = {
 1: {
  'rectangles': [(0,855,190,1200),(748,850,896,1200)],
  'polygons': [
   [(6,439),(106,410),(248,424),(316,496),(291,575),(224,669),(105,740),(38,744),(0,645)],
   [(85,903),(205,850),(248,855),(330,870),(397,831),(471,849),(535,916),(606,1200),(80,1200)],
   [(437,852),(514,821),(623,850),(699,852),(746,906),(802,1200),(601,1200),(553,1037)]],
  'protect_polygons': [],
  'protect_rectangles':[(263,1127,633,1187)]},
 2: {'rectangles':[(72,70,833,279),(39,1137,855,1196)],'polygons':[],
     'protect_rectangles':[],'protect_polygons':[]},
 3: {
  'rectangles':[(65,57,833,321)],
  'polygons':[
   [(0,433),(90,424),(306,426),(336,501),(295,649),(0,649)],
   [(227,511),(343,490),(417,486),(491,526),(532,610),(520,697),(235,765)],
   [(492,482),(587,476),(705,475),(782,502),(804,644),(528,715)],
   [(35,953),(81,925),(158,933),(216,963),(230,1200),(10,1200)],
   [(212,950),(252,908),(326,908),(364,950),(404,1200),(200,1200)],
   [(411,884),(474,895),(514,977),(459,1065),(359,1037)],
   [(575,937),(648,915),(749,915),(896,940),(896,1085),(792,1078),(765,1064),(648,1064),(600,990)]],
  'protect_polygons': [
   [(449,597),(490,588),(522,603),(571,620),(591,646),(561,668),(516,657),(486,665),(455,647)]],
  'protect_rectangles':[]},
 4: {
  'rectangles':[(153,64,760,360),(509,380,660,583),(754,710,896,848),(550,795,626,855),(405,841,443,887),(664,836,704,875)],
  'polygons':[
   [(0,704),(92,669),(168,672),(243,688),(386,712),(402,797),(345,916),(372,1097),(409,1200),(0,1200)],
   [(466,858),(513,845),(543,892),(532,937),(478,931)],
   [(570,852),(614,848),(640,914),(607,949),(569,933)],
   [(631,850),(700,843),(766,879),(792,979),(749,1090),(692,1066),(691,981),(646,955)],
   [(778,859),(836,846),(880,863),(896,905),(896,1001),(839,983),(809,941)]],
  'protect_polygons':[
   [(397,679),(463,647),(575,636),(579,660),(528,678),(534,715),(515,753),(481,785),(444,785),(405,755)]],
  'protect_rectangles':[]},
 5: {
  'rectangles':[(64,57,834,323),(759,721,896,890),(644,859,706,925),(801,872,852,938)],
  'polygons':[
   [(740,724),(770,724),(776,845),(792,865),(812,952),(798,956),(770,880),(760,845),(740,775)],
   [(302,507),(407,479),(501,510),(573,568),(612,700),(437,739),(294,737)],
   [(610,473),(664,470),(723,490),(748,575),(719,665),(624,693)],
   [(708,487),(784,488),(833,532),(896,559),(896,634),(741,672)],
   [(347,840),(453,831),(511,843),(620,860),(649,982),(597,1087),(502,1115),(421,1010)],
   [(211,939),(290,908),(340,935),(355,1056),(341,1200),(208,1200)],
   [(682,927),(749,931),(802,975),(807,1055),(760,1130),(684,1122),(673,1032)],
   [(660,920),(686,918),(701,973),(668,990)],
   [(837,907),(875,898),(896,922),(896,1009),(858,1000)]],
  'protect_polygons':[
   [(249,612),(287,607),(303,623),(300,662),(277,681),(253,660)],
   [(410,631),(449,625),(488,650),(494,684),(473,707),(439,692),(417,671)],
   [(357,840),(382,841),(406,857),(418,876),(391,885),(375,877),(351,874)],
   [(556,980),(582,974),(608,985),(611,1007),(588,1021),(554,1004)],
   [(711,1045),(738,1044),(763,1063),(761,1082),(733,1084),(707,1063)]],
  'protect_rectangles':[]}
}

HIGHLIGHTS = {
2:['Thái thú Tô Định','Trưng Định','thần y Nguyễn Huyền','Thi Sách ở Chu Diên','“Tiên phát chế nhân”','Mã Tắc và Lữ Thạch'],
3:['cướp bóc, đàn áp bách tính Giao Chỉ','Trưng Trắc','Thi Sách','Đinh Lương và Phùng Thị Chính'],
4:['Đại Lực Vương Phùng Công Lực','nhấc nổi đỉnh đồng','theo học Tản Viên Sơn Thánh','đánh tan giặc Thục, giữ yên bờ cõi Văn Lang','nối chí tổ tiên'],
5:['mật thư khẩn của phu nhân Trưng Trắc','“Giặc Tô Định đã bắt giữ cha thiếp tại Luy Lâu, lại đang đem quân xuống Chu Diên bắt phu quân!”','27 tộc trưởng, 70 thương thuyền','Phùng Thị Chính']
}
LOCKS=['Thái thú Tô Định','Trưng Trắc','Trưng Định','Nguyễn Huyền','Thi Sách','Chu Diên','Mê Linh','Mã Tắc','Lữ Thạch','Phùng Thị Chính','Phùng Công Lực','Hùng Duệ Vương','Tản Viên Sơn Thánh','Ba Vì','Văn Lang','Đinh Lương','Luy Lâu','Giao Chỉ','Tiên phát chế nhân']

def source_art(n):
    original=Image.open(PACK/f'01_nguon_bat_bien/pages/PDF_{n:02}.jpg').convert('RGB')
    raw=Image.open(HERE/f'PDF_{n:02}/art_edit_raw.png').convert('RGB')
    edited=ImageOps.fit(raw,SIZE,method=Image.Resampling.LANCZOS)
    if n==2:
        # The blank top plaque was made too short by imagegen. This operation
        # sizes only the empty paper plaque for typography, never the artwork.
        plaque=edited.crop((75,74,832,206)).resize((757,180),Image.Resampling.LANCZOS)
        edited.paste(plaque,(75,74))
    mask=Image.new('L',SIZE,0);d=ImageDraw.Draw(mask);regions=REGIONS[n]
    for rect in regions['rectangles']: d.rectangle(rect,fill=255)
    for poly in regions['polygons']: d.polygon(poly,fill=255)
    mask=mask.filter(ImageFilter.GaussianBlur(1))
    d=ImageDraw.Draw(mask)
    for rect in regions['protect_rectangles']: d.rectangle(rect,fill=0)
    for poly in regions['protect_polygons']: d.polygon(poly,fill=0)
    # Protect all source faces/headgear by leaving their regions outside the edit
    # mask. The mask and source are archived so this can be inspected/replayed.
    composed=Image.composite(edited,original,mask)
    ddir=HERE/f'PDF_{n:02}'
    mask.save(ddir/'edit_selection_mask.png')
    composed.save(ddir/'art_for_layout.png')
    provenance=json.loads((ddir/'provenance.json').read_text())
    provenance['compositing']='Only white mask regions use the archived imagegen edit; black retains immutable JPEG pixels. No flags/costumes are drawn with code.'
    provenance['art_for_layout_sha256']=hashlib.sha256((ddir/'art_for_layout.png').read_bytes()).hexdigest()
    (ddir/'provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
    return composed

def wrap(text,width,font,size):
    locked=text
    for phrase in sorted(LOCKS,key=len,reverse=True):
        locked=locked.replace(phrase,phrase.replace(' ','\u00a0'))
    atoms=locked.split(' ');lines=[];line=''
    for atom in atoms:
        trial=(line+' '+atom).strip()
        if line and pdfmetrics.stringWidth(trial,font,size)>width:
            lines.append(line.replace('\u00a0',' '));line=atom
        else: line=trial
    if line:lines.append(line.replace('\u00a0',' '))
    # If final line is unusually short, move one intact phrase onto it.
    if len(lines)>1 and len(lines[-1].split())<3:
        atoms=lines[-2].split(' ')
        if len(atoms)>5:
            for cut in range(len(atoms)-1,1,-1):
                a=' '.join(atoms[:cut]);b=' '.join(atoms[cut:])+' '+lines[-1]
                if len(b.split())>=3 and pdfmetrics.stringWidth(b,font,size)<=width:
                    if any((a.endswith(p.split()[0]) and b.startswith(' '.join(p.split()[1:]))) for p in LOCKS if ' ' in p):
                        continue
                    lines[-2:]=[a,b];break
    return lines

def draw_paragraph(c,text,box,n,kind='narration'):
    x0,y0,x1,y1=box
    font='Footnote' if kind=='footnote' else 'Narration'
    size=14.6 if kind=='footnote' else 19.2
    width=x1-x0
    while True:
        lines=wrap(text,width,font,size)
        leading=size*(1.27 if kind=='narration' else 1.25)
        height=leading*len(lines)
        if height <= y1-y0 or size<15:break
        size-=.2
    assert height<=y1-y0+1, (n,size,height,y1-y0)
    first_y=y0+(y1-y0-height)/2+size*.89
    ranges=[]
    for phrase in HIGHLIGHTS.get(n,[]) if kind=='narration' else ['“Tiên phát chế nhân”']:
        start=text.find(phrase)
        if start>=0:ranges.append((start,start+len(phrase)))
    cursor=0;details=[]
    for i,line in enumerate(lines):
        start=text.find(line,cursor)
        assert start>=0, (n,line,cursor)
        cursor=start+len(line)
        line_width=pdfmetrics.stringWidth(line,font,size)
        x=x0+(width-line_width)/2
        y=first_y+i*leading
        c.setFont(font,size*SCALE)
        # Split at color boundaries to keep full phrases red across lines.
        splits={0,len(line)}
        for a,b in ranges:
            if a<start+len(line) and b>start:
                splits.update([max(0,a-start),min(len(line),b-start)])
        splits=sorted(splits)
        for a,b in zip(splits,splits[1:]):
            red=any(s<=start+a<e for s,e in ranges)
            c.setFillColor(HexColor('#A92D24' if red else '#171713'))
            segment=line[a:b]
            c.drawString(x*SCALE,PT[1]-y*SCALE,segment)
            x+=pdfmetrics.stringWidth(segment,font,size)
        details.append({'text':line,'baseline_y_px':round(y,3)})
    return {'font':font,'font_size_px':round(size,3),'box_px':box,'lines':details}

def build(n):
    art=source_art(n)
    data=json.loads((LANE/f'text/PDF_{n:02}.json').read_text())
    out=LANE/'output';out.mkdir(exist_ok=True)
    pdf=out/f'PDF_{n:02}.pdf'
    c=canvas.Canvas(str(pdf),pagesize=PT,pageCompression=1)
    c.setTitle(f'Trưng Nữ Vương - PDF {n:02} - sửa theo góp ý giáo viên')
    c.setAuthor('Agent 1')
    c.drawImage(str(HERE/f'PDF_{n:02}/art_for_layout.png'),0,0,width=PT[0],height=PT[1])
    layout={'pdf_page':n,'page_size_pt':list(PT),'image_size_px':list(SIZE),'art':'art_for_layout.png','paragraphs':[]}
    boxes={2:(96,91,808,240),3:(91,82,807,235),4:(180,91,733,295),5:(90,80,808,217)}
    if n!=1:
        layout['paragraphs'].append(draw_paragraph(c,data['narration'],boxes[n],n))
    if n==2:
        layout['paragraphs'].append(draw_paragraph(c,data['footnote'],(59,1146,835,1182),n,'footnote'))
    c.showPage();c.save()
    with fitz.open(pdf) as doc:
        pix=doc[0].get_pixmap(matrix=fitz.Matrix(1/SCALE,1/SCALE),alpha=False)
        assert (pix.width,pix.height)==SIZE,(pix.width,pix.height)
        pix.save(out/f'PDF_{n:02}.png')
    # Use a second rendering engine for the separate visual QA evidence.
    subprocess.run(['pdftoppm','-f','1','-singlefile','-r','150','-png',str(pdf),
                    str(LANE/f'qa/PDF_{n:02}_render')],check=True,
                   stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    (HERE/f'PDF_{n:02}/layout.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
    print(f'Built PDF_{n:02}: {pdf}')

def combine():
    doc=fitz.open()
    for n in range(1,6):
        with fitz.open(LANE/f'output/PDF_{n:02}.pdf') as p:doc.insert_pdf(p)
    doc.save(LANE/'output/LO_TRANG.pdf',garbage=4,deflate=True)
    doc.close()

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--page',type=int,choices=range(1,6));parser.add_argument('--combine',action='store_true');args=parser.parse_args()
    for n in ([args.page] if args.page else range(1,6)):build(n)
    if args.combine:combine()
