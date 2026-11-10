#!/usr/bin/env python3
"""Editable cover/matter source. All coordinates mm from trim top-left."""
import json,math,hashlib,argparse
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from pypdf import PdfReader,PdfWriter
from pypdf.generic import RectangleObject
from PIL import Image
ROOT=Path(__file__).resolve().parents[0]
# The immutable snapshot lives in final_book_19x24/source.
REPO=ROOT.parents[1]
FONTS=ROOT/'fonts'
for n,f in [('R','NotoSans-Regular.ttf'),('B','NotoSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(n,str(FONTS/f)))
class Page:
 def __init__(self,name):
  self.name=name;self.proof=REPO/f'final_book_19x24/proofs/{name}_v002.pdf'
  assert not self.proof.exists(),self.proof
  self.c=canvas.Canvas(str(self.proof),pagesize=(196*mm,246*mm),initialFontName='R')
  self.c.setTitle('TRƯNG NỮ VƯƠNG - '+name);self.ops=[];self.rasters=[]
 def text(self,s,x,y,size=12,font='R',color='#251E17',align='left',outline=False):
  c=self.c;c.setFillColor(color);c.setFont(font,size);w=pdfmetrics.stringWidth(s,font,size)/mm
  if align=='center':x-=w/2
  if align=='right':x-=w
  assert x>=11 and x+w<=179.1,(s,x,w)
  assert 8<=y<=231,(s,y)
  if outline:
   for stroke,lw,fill in [('#251E17',4.2,'#251E17'),('#FFFBEB',2.4,'#FFFBEB'),(color,0,color)]:
    c.setStrokeColor(stroke);c.setFillColor(fill);c.setLineWidth(lw);t=c.beginText((x+3)*mm,(243-y)*mm);t.setFont(font,size);t.setTextRenderMode(2 if lw else 0);t.textOut(s);c.drawText(t)
  else:c.drawString((x+3)*mm,(243-y)*mm,s)
  self.ops.append(dict(type='text',text=s,x=x,baseline_y=y,font=font,size_pt=size,color=color))
 def para(self,s,x,y,w,size=11.5,leading=5.7,font='R',color='#251E17'):
  words=s.split();line='';lines=[]
  for word in words:
   candidate=(line+' '+word).strip()
   if pdfmetrics.stringWidth(candidate,font,size)/mm>w and line:lines.append(line);line=word
   else:line=candidate
  if line:lines.append(line)
  for i,l in enumerate(lines):self.text(l,x,y+i*leading,size,font,color)
  return y+len(lines)*leading
 def poly(self,pts,fill,stroke='#765534',width=.35):
  c=self.c;p=c.beginPath()
  for i,(x,y) in enumerate(pts):(p.moveTo if i==0 else p.lineTo)((x+3)*mm,(243-y)*mm)
  p.close();c.setFillColor(fill);c.setStrokeColor(stroke);c.setLineWidth(width*mm);c.drawPath(p,fill=1,stroke=1)
  self.ops.append(dict(type='polygon',points=pts,fill=fill,stroke=stroke))
 def rect(self,x,y,w,h,fill='#FFF7E1',stroke='#AA8454',radius=0):
  c=self.c;c.setFillColor(fill);c.setStrokeColor(stroke);c.setLineWidth(.3*mm)
  if radius:c.roundRect((x+3)*mm,(243-y-h)*mm,w*mm,h*mm,radius*mm,fill=1,stroke=1)
  else:c.rect((x+3)*mm,(243-y-h)*mm,w*mm,h*mm,fill=1,stroke=1)
  self.ops.append(dict(type='rect',bbox=[x,y,w,h],fill=fill,stroke=stroke))
 def line(self,x1,y1,x2,y2,col='#A48254',width=.5):
  c=self.c;c.setStrokeColor(col);c.setLineWidth(width*mm);c.line((x1+3)*mm,(243-y1)*mm,(x2+3)*mm,(243-y2)*mm)
  self.ops.append(dict(type='line',points=[x1,y1,x2,y2],color=col))
 def circle(self,x,y,r,fill='#B78B40',stroke='#6D4B24'):
  c=self.c;c.setFillColor(fill);c.setStrokeColor(stroke);c.setLineWidth(.3*mm);c.circle((x+3)*mm,(243-y)*mm,r*mm,fill=1,stroke=1)
 def art(self,path,x,y,w,h,mode='cover'):
  im=Image.open(REPO/path);iw,ih=im.size;scale=(max if mode=='cover' else min)(w/iw,h/ih);dw,dh=iw*scale,ih*scale;dx=x+(w-dw)/2;dy=y+(h-dh)/2
  c=self.c;c.saveState();p=c.beginPath();p.rect((x+3)*mm,(243-y-h)*mm,w*mm,h*mm);c.clipPath(p,fill=0,stroke=0);c.drawImage(str(REPO/path),(dx+3)*mm,(243-dy-dh)*mm,width=dw*mm,height=dh*mm);c.restoreState()
  self.rasters.append(dict(path=path,native_size_px=[iw,ih],bbox_mm=[x,y,w,h],scale_mode=mode,effective_dpi=25.4/scale,uniform_scale=True))
 def base(self,kicker,title,folio=None):
  self.rect(-3,-3,196,246,'#FFF7E5','#FFF7E5')
  self.rect(11,10,168,219,'#FFF9ED','#BD9C6C')
  self.text(kicker,19,23,9,'B','#9A6D35')
  self.text(title,19,36,22,'B','#902923');self.line(19,41,171,41,'#B88A4D',.5)
  if folio:self.text(folio,171,222,10,'B','#9A6D35',align='right')
 def finish(self):
  self.c.save();pg=PdfReader(self.proof).pages[0];pg.trimbox=RectangleObject([3*mm,3*mm,193*mm,243*mm]);pg.bleedbox=RectangleObject([0,0,196*mm,246*mm]);w=PdfWriter();w.add_page(pg)
  temp=self.proof.with_suffix('.tmp.pdf')
  with temp.open('wb') as f:w.write(f)
  temp.replace(self.proof);pg.cropbox=pg.trimbox;w=PdfWriter();w.add_page(pg);reading=REPO/f'final_book_19x24/reading/{self.name}_v002.pdf'
  with reading.open('wb') as f:w.write(f)
  d=dict(name=self.name,version='v002',operations=self.ops,rasters=self.rasters,trim_mm=[190,240],bleed_mm=[196,246],print_ready=False,user_approved=False,pdf_sha256=hashlib.sha256(self.proof.read_bytes()).hexdigest())
  (ROOT/f'{self.name}_placement.v002.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
  print(self.name)
def front():
 p=Page('FRONT');p.rect(-3,-3,196,246,'#D9B775','#D9B775')
 # Preserve entire foreground and boots in reading trim; matching landscape fills side strips.
 p.art('assets_generated/covers/FRONT_v001.png',0,0,190,240,'contain');p.line(5,0,5,240,'#986A2D',.4);p.line(185,0,185,240,'#986A2D',.4)
 p.poly([(13,12),(177,12),(174,17),(177,22),(13,22),(16,17)],'#EFB957','#5F351E',.5)
 p.text('TRUYỆN CỔ TÍCH LỊCH SỬ HÀO HÙNG',95,19,14.5,'B',align='center')
 p.text('TRƯNG NỮ VƯƠNG',95,39,44,'B','#B51F20',align='center',outline=True)
 p.poly([(15,44),(18,42.5),(172,42.5),(176,46),(175,51.5),(171,53),(19,53),(14,50)],'#FFF3CE','#906139',.3)
 p.text('Máu lửa Chu Diên, lời thề sông Nhị Hà',95,47,10.5,'R',align='center')
 p.text('và chiến công hiển hách của',95,51,10.5,'R',align='center')
 p.text('HAI BÀ TRƯNG',95,59,20,'B','#B51F39',align='center',outline=True)
 p.text('THI SÁCH – THÁNH THIÊN',95,66,16,'B','#183E76',align='center',outline=True)
 p.finish()
def back():
 p=Page('BACK');p.art('assets_generated/covers/BACK_v001.png',-3,-3,196,246)
 p.poly([(14,148),(18,146),(173,147),(177,151),(176,202),(171,205),(16,203),(13,199)],'#FFF4D8','#775332',.5)
 p.text('MỘT LỜI THỀ, MUÔN TẤM LÒNG',95,155,13,'B','#922F26',align='center')
 y=164
 for s in ['Mùa xuân năm 40, tiếng gọi đứng lên chống ách đô hộ vang dậy từ cửa sông Hát.',
 'Qua cuộc chiến bi tráng ở Chu Diên, lời thề Hát Môn và chiến công núi Phượng Hoàng, truyện khắc họa lòng yêu nước, tình nghĩa và ý chí tự chủ của những người con đất Việt.']:
  y=p.para(s,21,y,148,11.3,5.6)+2
 p.text('Truyện chuyển thể kết hợp lịch sử và huyền tích.',95,199,9.2,'R','#6D5037',align='center')
 p.text('Dành cho học sinh lớp 8–10',95,216,12,'B','#223F61',align='center')
 p.text('19 × 24 cm',95,223,10,'R','#6D5037',align='center');p.finish()
def matter1():
 p=Page('MATTER_I');p.base('TRUYỆN MINH HỌA','', 'i')
 p.text('TRƯNG',95,70,40,'B','#9B2526',align='center');p.text('NỮ VƯƠNG',95,89,40,'B','#9B2526',align='center')
 p.text('Từ Chu Diên đến lời thề Hát Môn',95,106,13,'R','#40566E',align='center')
 for r in [23,20,16]:p.circle(95,146,r,'#F7E6B8','#B58A42')
 for j in range(12):
  a=j*math.pi/6;p.line(95+10*math.cos(a),146+10*math.sin(a),95+18*math.cos(a),146+18*math.sin(a),'#A16D2C',.6)
 p.circle(95,146,9,'#B9873F','#7B542C')
 p.para('Một câu chuyện về lòng yêu nước, tình nghĩa và ý chí tự chủ, kể bằng tranh theo nguồn truyện và tư liệu lịch sử đối chiếu.',32,189,126,12,6)
 p.text('Dành cho học sinh lớp 8–10',95,214,11,'B','#40566E',align='center');p.finish()
def matter2():
 p=Page('MATTER_II');p.base('LỜI DẪN NHẬP','Trước khi mở truyện','ii')
 y=p.para('Năm 40 sau Công nguyên, Trưng Trắc và Trưng Nhị phát động khởi nghĩa ở cửa sông Hát. Nghĩa quân tiến đánh Luy Lâu; Trưng Trắc được suy tôn làm vua, đóng đô tại Mê Linh. [1]',19,53,151,11.7,5.8)
 y=p.para('Cuốn truyện theo chân những con người gắn với Mê Linh, Chu Diên và núi Phượng Hoàng. Lời thoại, huyền tích, trang phục và nhiều cảnh chiến đấu là cách kể của truyện; hãy đọc phân biệt với sự kiện lịch sử đã được đối chiếu.',19,y+5,151,11.5,5.7)
 p.text('Bốn gương mặt dẫn đường',19,119,15,'B','#8F3028')
 rows=[('Trưng Trắc','Người đứng đầu nghĩa quân; từ nỗi đau đến lời thề.','#A62A2A'),('Trưng Nhị','Người em luôn sát cánh cùng chị.','#234577'),('Thi Sách','Nhân vật trung tâm của mạch truyện Chu Diên.','#6D386D'),('Thánh Thiên','Nữ tướng của mạch truyện núi Phượng Hoàng.','#28613E')]
 for i,(name,s,col) in enumerate(rows):
  y=131+i*17;p.rect(19,y-5,151,15,'#F8EDD5','#DFCCAA');p.text(name,23,y,11.5,'B',col);p.text(s,23,y+6,10,'R')
 p.para('Gợi ý: đọc liền mạch để cảm nhận câu chuyện, rồi trở lại hai trang phụ lục để đối chiếu nguồn và trao đổi cùng bạn.',19,204,151,10.5,5)
 p.finish()
def matter3():
 p=Page('MATTER_III');p.base('PHỤ LỤC ĐỌC HIỂU','Lịch sử và huyền tích','iii')
 p.text('Những điểm lịch sử đã đối chiếu [1]',19,54,13,'B','#234577')
 items=[('NĂM 40','Hai Bà Trưng khởi nghĩa ở cửa sông Hát.'),('LUY LÂU','Nghĩa quân đánh đổ chính quyền đô hộ tại đây.'),('MÊ LINH','Trưng Trắc được suy tôn làm vua và đóng đô ở Mê Linh.')]
 for i,(k,s) in enumerate(items):
  y=67+i*22;p.text(k,19,y,11,'B','#9A332B');p.para(s,55,y,115,11,5.5)
 p.line(19,125,171,125)
 p.text('Đọc truyện với hai lớp thông tin',19,138,14,'B','#9A332B')
 y=p.para('Lịch sử: những sự kiện được đối chiếu với tư liệu, như mốc khởi nghĩa năm 40 và việc Trưng Trắc xưng vương.',19,150,151,11.5,5.7)
 y=p.para('Huyền tích và chuyển thể: khổng tước, huyết sâm, các lời thoại và nhiều chi tiết chiến trận giúp câu chuyện sinh động; chúng không tự trở thành chứng cứ lịch sử.',19,y+5,151,11.5,5.7)
 p.text('Hai di tích, hai địa điểm [2][3]',19,191,12,'B','#234577')
 p.para('Đền Hai Bà Trưng ở Hạ Lôi (Mê Linh) và đền Hát Môn là hai di tích khác nhau. Tranh tưởng niệm trong truyện là hình tượng minh họa.',19,201,151,10.5,5.2)
 p.finish()
def matter4():
 p=Page('MATTER_IV');p.base('PHỤ LỤC ĐỌC HIỂU','Cùng suy ngẫm','iv')
 terms=[('Tiên phát chế nhân','Chủ động ra tay trước để giành lợi thế; hiểu theo bối cảnh nhân vật sử dụng trong truyện.'),('Lời thề Hát Môn','Biểu tượng cho sự đồng lòng và quyết tâm giành quyền tự chủ.'),('Thánh Thiên','Nữ tướng trong mạch truyện Phượng Hoàng; chi tiết huyết sâm thuộc lớp huyền tích.')]
 y=53
 for k,s in terms:
  p.text(k,19,y,11.5,'B','#91382C');y=p.para(s,19,y+6,151,10.5,5.1)+7
 p.line(19,114,171,114)
 for i,s in enumerate(['Chi tiết nào cho thấy tình nghĩa gắn với trách nhiệm đối với cộng đồng?','Chọn một cảnh: đâu là sự kiện đối chiếu, đâu là yếu tố chuyển thể?','Bạn học được điều gì từ quyết tâm và sự đoàn kết của các nhân vật?'],1):
  y=p.para(str(i)+'. '+s,19,124+(i-1)*18,151,11,5.3)
 p.text('Nguồn đọc thêm',19,182,12,'B','#234577')
 sources=json.loads((REPO/'10_agent_workflow/tasks/SOURCE_EPILOGUE/sources.v001.json').read_text())
 labels=['[1] Bảo tàng Lịch sử Quốc gia: Khởi nghĩa Hai Bà Trưng.','[2] Cục Di sản văn hóa: Đền Hai Bà Trưng (Hạ Lôi).','[3] Cục Di sản văn hóa: Đền Hát Môn.']
 for i,(s,label) in enumerate(zip(sources,labels)):
  y=191+i*6;p.text(label,19,y,8.7,'R','#234577');p.c.linkURL(s['url'],(22*mm,(243-y-1)*mm,174*mm,(243-y+4)*mm),relative=0)
 p.text('Tư liệu truyện: trích Hồi 7–8 trong hồ sơ dự án.',19,213,8.5)
 p.text('Tranh minh họa được tạo bằng AI.',19,218,8.5);p.finish()
def insidefront():
 p=Page('INSIDE_FRONT');p.base('SƠ ĐỒ ĐỊA DANH','Không gian câu chuyện')
 p.text('Sơ đồ đọc truyện; không theo tỉ lệ địa lí.',19,52,10,'R','#715E48')
 groups=[('MÊ LINH',[(25,75,'Mê Linh'),(106,75,'Cổ Lôi')],'#294E79'),('CHU DIÊN',[(25,117,'Chu Diên'),(106,117,'Luy Lâu')],'#843D4E'),('HÁT MÔN',[(25,159,'Hát Môn'),(106,159,'Sông Nhị Hà')],'#2E6875'),('PHƯỢNG HOÀNG',[(25,201,'Núi Phượng Hoàng'),(106,201,'Lục Đầu Giang')],'#356644')]
 for title,nodes,col in groups:
  y=nodes[0][1];p.text(title,19,y-11,10,'B',col)
  for x,yy,label in nodes:p.rect(x,yy-6,62,14,'#F8ECD3',col,2);p.text(label,x+31,yy+3,10,'B',col,align='center')
  p.line(88,y+1,105,y+1,col,.6)
 p.finish()
def insideback():
 p=Page('INSIDE_BACK');p.base('HỒ SƠ NHÂN VẬT','Những mối dây nghĩa tình')
 p.text('Quan hệ theo nguồn truyện, không phải gia phả khảo chứng.',19,52,9.5,'R','#715E48')
 def box(x,y,w,name,size=11,col='#274D77'):
  p.rect(x,y,w,14,'#F9EDD3',col,2);p.text(name,x+w/2,y+9,size,'B',col,align='center')
 box(22,66,67,'Trưng Định');box(111,66,60,'Nguyễn Huyền',10.5)
 p.line(55.5,80,55.5,91);p.line(141,80,141,104)
 p.text('cha – con',141,97,8.5,'R','#715E48',align='center')
 p.line(35,91,77,91);p.line(35,91,35,104);p.line(77,91,77,104)
 box(15,104,40,'Trưng Trắc',10.3);box(61,104,40,'Trưng Nhị',10.3);box(111,104,60,'Thánh Thiên',10.5,col='#326544')
 p.line(35,118,35,139);p.text('vợ – chồng',36,130,8.5)
 box(15,139,56,'Thi Sách',11,col='#7D3D68')
 p.text('Các lực lượng trong mạch truyện',19,174,13,'B','#91362B')
 for i,(name,s,col) in enumerate([('Mê Linh','Hai Bà Trưng và các tộc trưởng.','#274D77'),('Chu Diên','Thi Sách, Đinh Lương, Phùng Thị Chính.','#7D3D68'),('Phượng Hoàng','Thánh Thiên và bảy bộ tộc.','#326544')]):
  y=187+i*13;p.text(name,19,y,10.5,'B',col);p.text(s,57,y,9.5)
 p.finish()
MAP={'FRONT':front,'BACK':back,'MATTER_I':matter1,'MATTER_II':matter2,'MATTER_III':matter3,'MATTER_IV':matter4,'INSIDE_FRONT':insidefront,'INSIDE_BACK':insideback}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('name',choices=MAP);arg=a.parse_args();MAP[arg.name]()
