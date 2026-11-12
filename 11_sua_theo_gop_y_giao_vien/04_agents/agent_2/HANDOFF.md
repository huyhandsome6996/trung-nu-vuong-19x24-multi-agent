# Bàn giao Agent 2 - PDF06–09

Trạng thái nội bộ: READY_FOR_COORDINATOR. Hoàn thành 4 trang, không có BLOCKED_ART.
Chỉ làm trong lane agent_2, nhánh sua-theo-gop-y-giao-vien; không sửa main,
nguồn bất biến, công cụ chung hoặc lane khác. Không ghép cả 21 trang.

## Sản phẩm thật

- `output/LO_TRANG.pdf`: 4 trang theo thứ tự vật lý 06, 07, 08, 09.
- `output/PDF_06…09.pdf`: từng PDF một trang, MediaBox 430,08×576 pt.
- `output/PDF_06…09.png`: PNG 896×1200, render từ PDF có chữ Việt thật.
- `text/PDF_06…09.json`: toàn bộ chữ, màu đỏ, người nói và quyết định sửa.
- `source/PDF_XX/`: ảnh đã chỉnh, prompt, layout, provenance/hash; trang 07/09
  giữ thêm ảnh trước lần chỉnh chi tiết. `source/build_pages.py` tái tạo đầu ra;
  font và giấy phép đi kèm. Không dùng ảnh thiết kế cũ trong repo.
- `qa/PDF_XX.json`, `qa/PDF_XX_render.png`, `qa/PDF_XX_technical.json` và
  `qa/text_roundtrip.json`: chứng cứ kiểm thật.

## Thay đổi chính

| Trang | Đã sửa và giữ |
|---|---|
| PDF06 | Thi Sách áo tía vạt trái/giáp ngắn phiến ngang; các lão trượng đai vải, áo nâu/chàm; giữ hổ phù và gia truyền. Cờ ở hàng quân Hán phía cửa thành xám than trơn. Ô dẫn từ khoảng 300 xuống 175px. |
| PDF07 | Phục trang Thi Sách thống nhất giữa hai khung; quân Hán vẫn giáp/mũ riêng. Sửa riêng cung còn một mũi lắp, các tên đã bay biểu diễn nối tiếp; lời dẫn giữ mười phát/mười lính. |
| PDF08 | Giáp ngắn và áo vạt trái cho Thi Sách ở cả hai khung; giữ Lữ Thạch khác phe, ngựa đen, tư thế và hai khung. Giữ nguyên “Mãnh long giáng địa” liền cụm, màu đỏ. |
| PDF09 | Thi Sách, Đinh Lương sửa phục trang; Mã Tắc/Lữ Thạch và quân xa giữ trang phục Hán. Cờ nhỏ trên thành và mép phải xám than trơn. Thu ô dẫn còn khoảng 150px, giữ bi tráng, không tăng máu. |

Không thêm thoại chuyển thể. Lời hô tập thể PDF06 là chữ đã có trong nguồn,
người nói được ghi ở JSON; không thêm bóng thoại.

## Kiểm đã thực hiện

Mở JPEG gốc PDF06–09 và cả bốn ảnh trang phục. Không có ảnh khoanh riêng
tương ứng bốn trang này theo phân công. Mở PNG cuối và ảnh render PDF từng
trang; kiểm phục trang theo phe, cờ kể cả phía xa, bố cục, chữ và màu đỏ.
Đọc lại chữ trích từ PDF và so với JSON: khớp hoàn toàn sau chuẩn hóa khoảng
trắng trên cả bốn trang. Kiểm gói nguồn, phạm vi stage, kích thước và đầu ra
bằng các công cụ trong ngăn 06 trước commit cuối.

Checkpoint đã có: `865a873` (PDF06), `ba3e3a4` (PDF08), `6f0b2f8` (PDF07).
Commit cuối mang thông điệp `sua giao vien: agent_2 hoan thanh lo trang`;
SHA cuối và tình trạng push được báo kèm khi bàn giao, không suy từ file này
rằng đã push thành công.

Lượt push trước đã bị bộ duyệt tự động chặn vì chưa công nhận ủy quyền.
Ngày12/11/2026, chủ dự án xác nhận trực tiếp cho phép push vào nhánh sửa.
Sau khi phiên làm việc được làm mới, khôi phục nguyên gói ZIP đã bàn giao
(SHA256 01e4947784f6b15f2ae7158236d9b542e5430f061b47740005659d1b5fb87513).
Các SHA checkpoint cũ ở trên là lịch sử phiên trước; lượt xuất bản dùng commit
mới trên đầu nhánh hiện hành, không thay đổi nội dung tranh/chữ đã kiểm.
Chỉ báo thành công sau fetch và xác nhận commit thuộc lịch sử nhánh remote.

## Coordinator cần rà

- Đối chiếu Thi Sách/Đinh Lương với lane 1 và chuyển cảnh sang lane 3;
  cross_lane_identity và cross_lane_review đang PENDING.
- Chỉnh AI có sai khác nét nhỏ so với gốc; giữ bố cục, diễn biến và phong cách,
  không cam kết giữ nguyên từng pixel ngoài vùng chỉnh.
- Ảnh gốc 896×1200 px. Không nâng nhãn DPI, không tuyên bố đạt in 300 DPI.
- Đây là QA nội bộ, chưa phải giáo viên duyệt hoặc nghiệm thu toàn sách.
