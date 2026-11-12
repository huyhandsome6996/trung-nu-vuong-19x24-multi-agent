# Kiểm kỹ thuật thực hiện

- `check_packet.py`: PASS — 36 file nguồn bất biến, 21 trang, 5 lane rời nhau, đúng nhánh, không credential.
- `validate_lane.py agent_1 --ready`: PASS — đủ output/nguồn/QA/evidence, STATUS READY_FOR_COORDINATOR.
- `validate_lane.py agent_1 --staged`: PASS ở cả 5 checkpoint từng trang; chạy lại trước commit bàn giao.
- `git diff --cached --check`: PASS ở 5 checkpoint; PDF được khai báo binary bằng .gitattributes trong lane để không hiểu sai các khoảng trắng bắt buộc của cấu trúc PDF là lỗi văn bản.
- PNG đầu ra: 896 × 1200 px; PDF lẻ và lô: 430,08 × 576 pt.
- Hai đường kiểm hình: mở PNG từ PyMuPDF và ảnh render độc lập Poppler của cả 5 PDF.

- PDF01: PASS — một trang, đúng MediaBox; chữ bìa giữ raster nguồn, đã đọc kiểm.
- PDF02: PASS — một trang, đúng MediaBox; chữ trích xuất trong PDF lô khớp JSON.
- PDF03: PASS — một trang, đúng MediaBox; chữ trích xuất trong PDF lô khớp JSON.
- PDF04: PASS — một trang, đúng MediaBox; chữ trích xuất trong PDF lô khớp JSON.
- PDF05: PASS — một trang, đúng MediaBox; chữ trích xuất trong PDF lô khớp JSON.

QA thị giác và từng yêu cầu nằm trong PDF_XX.json. Công cụ kiểm kỹ thuật không chứng minh thay giáo viên/coordinator về mỹ thuật và đồng bộ liên trang.
