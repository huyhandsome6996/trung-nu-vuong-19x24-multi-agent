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
