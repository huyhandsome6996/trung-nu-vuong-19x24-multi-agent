# Nguồn chế bản và phiên bản hiện hành

Bản đọc kiểm được tạo bằng scripts/render_page.py từ chữ khóa và nền thật. SVG giữ chữ Việt sửa được, liên kết font tương đối trong fonts/, nhúng tranhPNG. Chạy lệnh từ gốc repo.

Trang01 hiện hành: TEXTv002, ARTv002, LAYOUTv002. LAYOUTv001 bị thay vì khoảng trắng tại ranh giới từ khóa; giữ để đối chiếu, không dùng để ghép sách.

Lệnh tái tạo cần một version mới, ví dụ:

```bash
python scripts/render_page.py --text 10_agent_workflow/tasks/PAGE01_TEXT/text.v002.json --raw assets_generated/raw_pages/PAGE01_v002.png --version v003
/usr/bin/pdftoppm -r 150 -singlefile -png final_book_19x24/proofs/PAGE01_v003.pdf final_book_19x24/proofs/PAGE01_v003
```

Sử dụng Poppler thực đã kiểm. Binary override tên pdftoppm trong môi trường phiên này từng tạoPNG không giải mã đủ; kiểm Pillow.verify trước khi mở ảnh.

ProofPDF: Media/Bleed196×246mm, Trim190×240mm cách3mm. ReadingPDF: CropBox ở trim. FontNotoSans nhúng có OFL; tranh nguồn có độ phân giải hiệu dụng khoảng145DPI. Render300DPI chỉ là lấy mẫu bản kiểm, không tăng chi tiết tranh gốc. Không file nào trong đợt này được gắnPRINT_READY hoặcUSER_APPROVED.

## Bảng phiên bản đang dùng sau trang06

| Trang | Chữ | Tranh | Layout |
| --- | --- | --- | --- |
|01|v002|v002|v002|
|02|v001|v002 (metadata v003)|v001|
|03|v001|v001|v001|
|04|v001|v002|v002|
|05|v001|v001|v002|
|06|v001|v001|v001|

Bản đọc ghép6trang đầu là checkpoint, chưa đủ sách. Trang04LAYOUTv001 bị thay vì đuôi thoại đi ngang tóc; trang05proofv001 không dùng vì lỗi xuất (tệp rỗng đã loại, nguồn/bảnđọc cũ còn). Chỉ dùng phiên bản trong bảng vàevidence state để ghép sách. Snapshotrendererv003 thêm clip thủ công từng khung, trích thư khôngđuôi, vàghiPDF bằng tệp tạm rồi thay nguyên tử.

## User lettering revision10Nov2026

Latest accepted illustrated-speech samples: PAGE12LAYOUTv003/ARTv001; PAGE13LAYOUTv002/ARTv003. Both contain actual lettered-cloud PNG artwork placed without distortion; original locked quote and exact generation request are retained. Render snapshotv004 supports these assets. PDF extraction validates narration only; visible dialogue requires manual review.

Old layouts03,04,06,07,09,10,11 are retained as historical drafts and reopened for the new speech style. Do not assemble them as fully revised/approved pages. Pages01,02,05,08 have no ordinary speech clouds requiring this restyle. PAGE12v003 and PAGE13v002 are agent-reviewed proofs, not user approval or print release. Use current task evidence for the remaining version selections; the six-page table above is historical.

## Coordinator checkpoint10Nov after A/B launch

Current illustrated-speech layout/QA:06v002,07v003,09v004,10v004,11v003;04v003/12v003/13v002 remain unchanged.03is still blocked, old03v001 is not revised-QA.

Front coverv002; backv001; insidefrontv001; insidebackv002; MATTER_I/II/III/IVv001. Sources are immutable render_ancillaryv001/v002/v003 and placementJSON; report evidence selects exact versions. Pagination inFRONT_MATTER selects36reading faces, including28story pages resolved from currentQA after lane integration. Eight-face covers/matter reviewPDF is not a full book.
