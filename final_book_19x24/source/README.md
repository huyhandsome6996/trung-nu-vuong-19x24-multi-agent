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
