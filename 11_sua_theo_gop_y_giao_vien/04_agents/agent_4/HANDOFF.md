# Bàn giao Agent 4 - PDF15-17

Trạng thái: **READY_FOR_COORDINATOR**. Không có trang BLOCKED. Chưa phải giáo viên duyệt hoặc toàn sách đã đồng bộ.

| Trang | Đã sửa | Đầu ra |
|---|---|---|
|PDF15|Thêm lời thề Trưng Trắc và hưởng ứng của nghĩa quân; cờ đỏ đất trơn toàn cảnh; trang phục thực dụng; thu ô vàng.|`output/PDF_15.png`, `output/PDF_15.pdf`|
|PDF16|Thánh Thiên khăn tang trắng, tóc búi thấp, mặt bầu hơi góc/mày ngang, áo lục và giáp ngắn; giữ cảnh cung tên; thoại báo thù cho cha và cứu dân; thu ô vàng.|`output/PDF_16.png`, `output/PDF_16.pdf`|
|PDF17|Giữ thuyền quân Hán trên, sa bàn dưới; Thánh Thiên theo khóa PDF16; đối thoại giả thua, phục cung nỏ, chặn bến/đoạt thuyền; giữ Tào Quyền, Lục Hiến và 30 khinh thuyền.|`output/PDF_17.png`, `output/PDF_17.pdf`|

PDF lô: `output/LO_TRANG.pdf`, đúng 3 trang theo thứ tự 15-16-17. Mỗi trang 430,08 x 576 pt, PNG 896 x 1200. Lớp chữ PDF dùng font Việt nhúng, có thể chọn/copy. Nội dung text chính xác trong `text/PDF_XX.json`, kèm người nói/thứ tự/khung và bố cục chữ. Lời thêm là chuyển thể biên tập, không phải trích nguyên văn lịch sử.

## Nguồn dựng lại

- `source/PDF_XX_art.png`: tranh đã chỉnh bằng công cụ ảnh tích hợp, dùng ảnh gốc làm tham chiếu, chưa có chữ.
- `source/PDF_XX_prompt.txt` và `source/PDF_XX_provenance.json`: prompt chỉnh tranh và các ảnh tham chiếu thật kèm SHA256. PDF16 có thêm nguồn/lệnh tinh chỉnh ô vàng; lưu bản trung gian để truy nguyên.
- `source/build_pages.py`: dựng lại PDF/PNG và cả PDF lô từ art + JSON. Chạy `python3 source/build_pages.py` từ lane, cần ReportLab và PyMuPDF. Font Noto Sans cùng giấy phép nằm trong `source/fonts/`.
- `source/THANH_THIEN_REFERENCE.png`: crop trực tiếp từ tranh PDF16 đã sửa, sạch chữ, cho Agent 5 đối chiếu. `source/PDF_17_REFERENCE_INPUT.png` giữ chính xác crop đã cấp cho lượt sửa PDF17 trước bước tinh chỉnh giữ tỉ lệ bản xuất.

## Kiểm đã thực hiện

Đã mở ảnh nguồn PDF15-17, 2 ảnh khoanh và cả 4 ảnh trang phục. Không dùng tranh thiết kế cũ. Đã mở trực tiếp cả PNG cuối và PDF render cuối của từng trang, kiểm cờ/trang phục/thoại/đuôi bóng/chữ/khung/sa bàn/cung tên. QA từng trang ở `qa/PDF_XX.json`, ảnh render có thật, ghi người kiểm Agent 4.

Kiểm kỹ thuật: nguồn bất biến/đúng nhánh/lane; PNG đủ kích thước; từng PDF một trang và MediaBox đúng; PDF lô đủ 3 trang đúng thứ tự; toàn bộ chữ trích từ PDF khớp JSON sau chuẩn hóa khoảng trắng. Báo cáo tại `qa/TECHNICAL_REPORT.json`.

Các lệnh cổng bàn giao: `check_packet.py`, `validate_lane.py agent_4 --ready`, `validate_lane.py agent_4 --staged`, `git diff --cached --check`. Không sửa công cụ kiểm hoặc tệp chung để đạt kiểm.

## Điều phối viên cần rà tiếp

**PENDING liên lane:** so mặt/khăn tang/áo lục của PDF16-17 với PDF18-20 và Thánh Thiên ở PDF21 của Agent 5. Đã đối chiếu nội bộ PDF16-17. Có reference để đối chiếu ngay; Agent 4 không khẳng định đã xem sản phẩm chưa có của lane khác. Điều phối viên ghép đủ 21 trang sau khi mọi lane được kiểm.

Giữ số cảnh và mạch gốc; vùng tường/sky trống được điều chỉnh cho thoại và ô vàng gọn. Do sửa bằng công cụ ảnh tham chiếu, có thay đổi nét phụ; không coi là bảo toàn tuyệt đối từng pixel ngoài vùng sửa. Cờ/trang phục là quy ước minh họa của gói, không khẳng định phục dựng lịch sử. Nguồn ban đầu 896 x 1200; không có tuyên bố đạt in 300 DPI.

## Git

Nhánh duy nhất `sua-theo-gop-y-giao-vien`, chỉ ghi lane `04_agents/agent_4/`. Checkpoint `fabd10b` (PDF15), `c0babd6` (PDF16 + reference, đã push và kiểm tổ tiên remote), `655a542` (PDF17). Commit bàn giao cuối đi kèm tệp này, SHA cuối được trả trong báo cáo phiên. Không lưu credential vào repo, URL hoặc lịch sử commit. Không force-push.
