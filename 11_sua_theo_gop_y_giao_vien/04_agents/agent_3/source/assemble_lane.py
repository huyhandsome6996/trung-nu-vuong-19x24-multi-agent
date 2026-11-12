#!/usr/bin/env python3
from pathlib import Path
import fitz
lane=Path(__file__).resolve().parents[1]
merged=fitz.open()
for n in range(10,15):
 with fitz.open(lane/f'output/PDF_{n:02}.pdf') as src:merged.insert_pdf(src)
merged.save(lane/'output/LO_TRANG.pdf',garbage=4,deflate=True)
print('Merged PDF10–14:',len(merged),'pages')
