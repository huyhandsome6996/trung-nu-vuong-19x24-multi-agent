#!/usr/bin/env python3
"""Assemble only after every assigned page has real output and per-page QA."""
from pathlib import Path
import hashlib
import json
import sys
import fitz
from PIL import Image, ImageDraw
from check_packet import main as check_packet
from validate_lane import validate

PACK = Path(__file__).resolve().parents[1]


def main():
    if check_packet():
        return 1
    assignments = json.loads((PACK / '00_dieu_phoi/ASSIGNMENTS.json').read_text())
    errors = []
    for lane in assignments['lanes']:
        errors.extend(lane + ': ' + error for error in validate(lane, ready=True))
    if errors:
        print('BLOCKED: no final PDF written. Resolve lane output/QA first.')
        print('\n'.join(errors))
        return 1
    page_owners = {p: lane for lane, pages in assignments['lanes'].items() for p in pages}
    output = PACK / '07_tong_hop'
    pdf = fitz.open()
    records = []
    thumbs = []
    for page in range(1, 22):
        source = PACK / f'04_agents/{page_owners[page]}/output/PDF_{page:02}.pdf'
        with fitz.open(source) as part:
            pdf.insert_pdf(part)
        records.append({'pdf_page': page, 'lane': page_owners[page], 'source': str(source.relative_to(PACK)), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
        image_path = source.with_suffix('.png')
        with Image.open(image_path) as im:
            thumb = im.convert('RGB')
            thumb.thumbnail((260, 350))
        tile = Image.new('RGB', (280, 390), 'white')
        tile.paste(thumb, ((280 - thumb.width) // 2, 30))
        ImageDraw.Draw(tile).text((12, 8), f'PDF {page:02}', fill='black')
        thumbs.append(tile)
    destination = output / 'BAN_SUA_GIAO_VIEN.pdf'
    pdf.save(destination, garbage=4, deflate=True)
    pdf.close()
    with fitz.open(destination) as check:
        assert len(check) == 21
        assert all(abs(p.rect.width - assignments['page_size_pt'][0]) < .1 and abs(p.rect.height - assignments['page_size_pt'][1]) < .1 for p in check)
    for group in range(3):
        sheet = Image.new('RGB', (280 * 4, 390 * 2), '#dddddd')
        for index, tile in enumerate(thumbs[group * 7:(group + 1) * 7]):
            sheet.paste(tile, ((index % 4) * 280, (index // 4) * 390))
        sheet.save(output / f'TONG_QUAN_SUA_{group + 1}.jpg', quality=92)
    (output / 'ASSEMBLY_MANIFEST.json').write_text(json.dumps({'status': 'ASSEMBLED_PENDING_FINAL_VISUAL_REVIEW', 'page_count': 21, 'pages': records, 'pdf_sha256': hashlib.sha256(destination.read_bytes()).hexdigest()}, ensure_ascii=False, indent=2) + '\n')
    print('WROTE', destination)
    print('Pending coordinator review of all rendered pages; teacher approval is not implied.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
