# Agent 1 - PDF 01, 02, 03, 04, 05

Sửa trọn lô, không dừng ở kế hoạch. Nguyên tắc và định nghĩa đầu ra: đọc README.md, 02_quy_chuan/NGUYEN_TAC_SUA.md, 02_quy_chuan/GOI_Y_THOAI.md của ngăn sửa.

## PDF 01 - Bìa Trưng Nữ Vương

- Rà và thay tất cả cờ trên bìa theo mẫu mới; sửa trang phục nhân vật Lĩnh Nam nếu còn kiểu Trung Hoa.
- Giữ nguyên tiêu đề, phụ đề, nhân vật, bố cục bìa Gemini và câu dẫn chân trang; chỉ thu gọn ô nếu dư.

## PDF 02 - Tô Định dùng kế tiên phát chế nhân

- Bỏ riêng nhãn “Chú thích:” và dấu * gọi chú thích không còn cần thiết ở ô chân trang.
- Thuật ngữ viết “Tiên phát chế nhân” trong ngoặc kép; đặt lời chú giải chân trang in nghiêng, giữ nghĩa gốc. Trong ô dẫn cũng để thuật ngữ trong ngoặc kép.
- Thu gọn ô vàng trên và ô chú giải; không xóa phần giải nghĩa.
- Đây là cảnh quân Hán: giữ nhận diện phe Hán, không mặc đồng phục Lĩnh Nam cho Tô Định/Mã Tắc/Lữ Thạch.

## PDF 03 - Trưng Trắc từ biệt Thi Sách

- Khung trên: bỏ kiến trúc thành phía sau đôi nhân vật, thay đồng quê Việt Nam có ruộng lúa và trâu; giữ đôi người, tư thế và các khung còn lại.
- Thu gọn ô dẫn vàng; rà trang phục Thi Sách/Trưng Trắc theo quy chuẩn mới.

## PDF 04 - Dòng dõi Phùng Thị Chính

- Thay đại từ gây nhầm “ông” ở đoạn kể tổ tiên bằng tên rõ “Phùng Công Lực”; không đổi thành “Phùng Lực Công” theo storyboard cũ.
- Thay “Nay vợ chồng nàng” bằng “Nay vợ chồng Phùng Thị Chính”.
- Thay “quyết theo Thi Sách diệt giặc” bằng “quyết theo Thi Sách và Trưng Trắc diệt giặc”.
- Rà cờ ở thuyền và cờ xa; phục trang cảnh hồi tưởng cũng thuộc phe Văn Lang.

## PDF 05 - Chim câu đưa mật thư

- Đổi mở đầu “Bỗng chim câu...” thành “Một hôm, chim câu...”; giữ nội dung mật thư và hành động.
- Thu bớt khoảng vàng thừa trong ô dẫn, kiểm toàn bộ cờ và trang phục.

## Quyền ghi và đầu ra

Chỉ ghi lane này. Mỗi trang cần text/PDF_XX.json (toàn bộ chữ cuối cùng + người nói + quyết định thay đổi); source/PDF_XX.* (nguồn dàn trang/chỉnh sửa có thể tái tạo, ảnh sạch/mask nếu có); output/PDF_XX.png; output/PDF_XX.pdf (một trang cùng khổ nguồn); qa/PDF_XX.json (copy schema TEMPLATE, kiểm thật). Giữ source một thư mục rõ nếu có nhiều layer; không chỉ giao prompt thay cho ảnh sửa. Cuối lane tạo output/LO_TRANG.pdf và HANDOFF.md nêu điều đã sửa, hạn chế, SHA, trang nào BLOCKED.

Đọc thêm `02_quy_chuan/DAU_RA_VA_QA.md` trong ngăn sửa để dùng đúng schema chữ, QA, evidence và trạng thái READY_FOR_COORDINATOR.
