# Agent 3 - PDF 10, 11, 12, 13, 14

Sửa trọn lô, không dừng ở kế hoạch. Nguyên tắc và định nghĩa đầu ra: đọc README.md, 02_quy_chuan/NGUYEN_TAC_SUA.md, 02_quy_chuan/GOI_Y_THOAI.md của ngăn sửa.

## PDF 10 - Cổ Lôi sơn trang

- Thay lá cờ có ngôi sao ở khung dưới đã khoanh trong ảnh PDF_10_khoanh_do.jpg; rà các cờ còn lại.
- Rà trang phục quân Hai Bà ở cảnh tập hợp; thu gọn ô dẫn.

## PDF 11 - Trưởng lão và huyện lệnh hưởng ứng

- Thu hẹp rõ khoảng vàng thừa cả trên và dưới đoạn dẫn như ảnh khoanh; tăng vừa phải kích cỡ chữ nếu cần, không nhồi thêm nội dung.
- Rà quân Hai Bà, các cờ và trang phục theo phe. Không tự đổi mọi công trình trong truyện: yêu cầu thay thành bằng đồng quê áp dụng trực tiếp PDF03.

## PDF 12 - Các huyện lệnh hội tụ

- Sửa trang phục nhóm lính sau Trưng Trắc ở khung dưới theo ảnh khoanh, kiểm luôn quân Lĩnh Nam ở khung trên.
- Rà cờ/ô vàng toàn trang.

## PDF 13 - Tô Định lo sợ và bàn kế

- Dàn lại đoạn dẫn để “Phượng Hoàng” cùng dòng hoặc cùng cụm, không để “Hoàng.” một mình ở dòng cuối.
- Sửa phục trang quân Hai Bà ở khung trên phải; giữ Tô Định, Tào Quyền, Mã Tắc ở phe Hán.
- Khung dưới: bổ sung vài câu thoại Tô Định với Tào Quyền (TQ) và Mã Tắc (MT), thể hiện lo sợ/bàn phương án thoát thân và kế đối phó. Kế chạy là dự phòng, không kể họ đã bỏ chạy ở thời điểm này; vẫn giữ kế chia quân trong lời dẫn.
- Đối chiếu tên: PDF có chỗ giống “Tào Quyên”, repo chú giải nguồn dùng “Tào Quyền”. Dùng thống nhất “Tào Quyền” cho thoại mới và sửa biến thể sai dấu nếu xác nhận bằng nguồn trong repo; ghi lại quyết định ở text/changes.md.

## PDF 14 - Đàn tế Hát Môn

- Thay cờ phía sau Hai Bà đã khoanh và tất cả cờ còn lại.
- Thêm lời khấn nguyện của Hai Bà tại khung tế lễ dưới; lời khấn ngắn thể hiện hướng về tổ tiên và quyết chí cứu nước, không bịa là trích nguyên văn lịch sử.
- Rà trang phục Hai Bà và nghĩa quân, giữ đàn tế/cảnh sông và hai khung.

## Quyền ghi và đầu ra

Chỉ ghi lane này. Mỗi trang cần text/PDF_XX.json (toàn bộ chữ cuối cùng + người nói + quyết định thay đổi); source/PDF_XX.* (nguồn dàn trang/chỉnh sửa có thể tái tạo, ảnh sạch/mask nếu có); output/PDF_XX.png; output/PDF_XX.pdf (một trang cùng khổ nguồn); qa/PDF_XX.json (copy schema TEMPLATE, kiểm thật). Giữ source một thư mục rõ nếu có nhiều layer; không chỉ giao prompt thay cho ảnh sửa. Cuối lane tạo output/LO_TRANG.pdf và HANDOFF.md nêu điều đã sửa, hạn chế, SHA, trang nào BLOCKED.

Đọc thêm `02_quy_chuan/DAU_RA_VA_QA.md` trong ngăn sửa để dùng đúng schema chữ, QA, evidence và trạng thái READY_FOR_COORDINATOR.
