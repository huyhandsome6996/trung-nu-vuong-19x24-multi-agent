# Agent 2 - PDF 06, 07, 08, 09

Sửa trọn lô, không dừng ở kế hoạch. Nguyên tắc và định nghĩa đầu ra: đọc README.md, 02_quy_chuan/NGUYEN_TAC_SUA.md, 02_quy_chuan/GOI_Y_THOAI.md của ngăn sửa.

## PDF 06 - Thi Sách tập hợp lực lượng

- Sửa trang phục Thi Sách và lực lượng Lĩnh Nam quanh chàng theo ảnh tham khảo; phân biệt với quân Hán ở xa nếu có.
- Giữ thông tin hổ phù, gia truyền, nhân vật và bố cục; không sửa sự kiện vì yêu cầu sửa phục trang.

## PDF 07 - Thi Sách đối đầu Lữ Thạch

- Rà trang phục Thi Sách và phe Lĩnh Nam, giữ phe Hán khác biệt.
- Giữ hai khung hành động, diễn biến và số lượng phát tên theo bản truyện; không biến thành một phát bắn cả chùm nếu phải sửa tranh.

## PDF 08 - Giao chiến trên lưng ngựa

- Rà phục trang Thi Sách, lính và cờ nếu có; giữ hai khung giao chiến, tư thế và diễn biến.
- Thu gọn ô vàng khi cần, giữ tên tuyệt kỹ và diễn đạt của PDF gốc.

## PDF 09 - Trận chiến Chu Diên

- Rà phục trang Thi Sách, Đinh Lương, nghĩa sĩ; không đổi quân Hán sang phục trang Lĩnh Nam.
- Giữ diễn biến bi tráng, bố cục hai khung và mức thể hiện phù hợp học sinh.

## Quyền ghi và đầu ra

Chỉ ghi lane này. Mỗi trang cần text/PDF_XX.json (toàn bộ chữ cuối cùng + người nói + quyết định thay đổi); source/PDF_XX.* (nguồn dàn trang/chỉnh sửa có thể tái tạo, ảnh sạch/mask nếu có); output/PDF_XX.png; output/PDF_XX.pdf (một trang cùng khổ nguồn); qa/PDF_XX.json (copy schema TEMPLATE, kiểm thật). Giữ source một thư mục rõ nếu có nhiều layer; không chỉ giao prompt thay cho ảnh sửa. Cuối lane tạo output/LO_TRANG.pdf và HANDOFF.md nêu điều đã sửa, hạn chế, SHA, trang nào BLOCKED.

Đọc thêm `02_quy_chuan/DAU_RA_VA_QA.md` trong ngăn sửa để dùng đúng schema chữ, QA, evidence và trạng thái READY_FOR_COORDINATOR.
