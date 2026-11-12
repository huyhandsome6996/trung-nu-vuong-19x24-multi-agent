# Agent 4 - PDF 15, 16, 17

Sửa trọn lô, không dừng ở kế hoạch. Nguyên tắc và định nghĩa đầu ra: đọc README.md, 02_quy_chuan/NGUYEN_TAC_SUA.md, 02_quy_chuan/GOI_Y_THOAI.md của ngăn sửa.

## PDF 15 - Lời thề trước ba quân

- Thêm lời thề trực tiếp của Trưng Trắc và lời hưởng ứng ngắn của Trưng Nhị/nghĩa quân nếu bố cục cho phép, làm rõ quyết chí đánh giặc.
- Giữ cảnh đọc hịch, nhân vật trung tâm và bố cục một khung; không sao chép đoạn hịch dài từ repo để che tranh.
- Rà cờ và phục trang toàn trang.

## PDF 16 - Nữ tướng Thánh Thiên

- Thêm thoại Thánh Thiên tại khung dưới, nêu quyết tâm báo thù cho cha và cứu dân.
- Làm gương mặt Thánh Thiên khác rõ Trưng Trắc theo khóa nhận diện chung; cùng khóa này dùng trên PDF17–20 và nhân vật tương ứng PDF21.
- Giữ hai khung và hành động bắn cung phía trên; sửa trang phục Thánh Thiên cùng nghĩa quân theo quy chuẩn.

## PDF 17 - Bàn kế sa bàn

- Thêm đối thoại ở khung bàn bản đồ: Thánh Thiên nói kế giả thua dụ quân vào khe Mãng Xà; tướng đáp về phục binh/chiếm thuyền.
- Giữ mạch dụ địch, vị trí hai khung; thoại phải làm rõ mưu trí mà không kể thắng trận sớm.
- Giữ mặt Thánh Thiên khác Trưng Trắc, áp dụng cùng quy chuẩn với PDF16; kiểm tên Tào Quyền theo nguồn cốt truyện.

## Quyền ghi và đầu ra

Chỉ ghi lane này. Mỗi trang cần text/PDF_XX.json (toàn bộ chữ cuối cùng + người nói + quyết định thay đổi); source/PDF_XX.* (nguồn dàn trang/chỉnh sửa có thể tái tạo, ảnh sạch/mask nếu có); output/PDF_XX.png; output/PDF_XX.pdf (một trang cùng khổ nguồn); qa/PDF_XX.json (copy schema TEMPLATE, kiểm thật). Giữ source một thư mục rõ nếu có nhiều layer; không chỉ giao prompt thay cho ảnh sửa. Cuối lane tạo output/LO_TRANG.pdf và HANDOFF.md nêu điều đã sửa, hạn chế, SHA, trang nào BLOCKED.

Xuất source/THANH_THIEN_REFERENCE.png sau khi sửa trang16 để lane 5 đọc.

Đọc thêm `02_quy_chuan/DAU_RA_VA_QA.md` trong ngăn sửa để dùng đúng schema chữ, QA, evidence và trạng thái READY_FOR_COORDINATOR.
