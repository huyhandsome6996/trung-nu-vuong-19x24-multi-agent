# Phân tích và phân công ngày12/11/2026

Bản nền là PDF Gemini21 trang, không phải sản phẩm cũ28 trang trong repo. Nguyên tắc: chia theo trang, mỗi agent chịu cả chữ + tranh + QA trong phạm vi mình; 5 lane không ghi đè nhau. Trang có nhiều thoại được giao ít hơn.

|Agent|Trang PDF (tính bìa)|Trọng tâm|
|---|---|---|
|1|01–05|Bìa; chú giải; đồng quê; tên Phùng Công Lực; chim câu|
|2|06–09|Trang phục/cờ các cảnh Thi Sách chiến đấu|
|3|10–14|Cờ; ô vàng; Hoàng lẻ dòng; thoại Tô Định; khấn Hát Môn|
|4|15–17|Lời thề; gương mặt Thánh Thiên; thoại sa bàn|
|5|18–21|Dụ địch; giặc trốn; Trảm thủ; cờ/trang kết|

## Map ảnh giáo viên

|Tên gốc (tiền tố)|Trang|Vị trí|
|---|---:|---|
1794410420496|10|Cờ khung dưới|
1794410457761|11|Ô vàng dư|
1794410515628|12|Trang phục lính sau Trưng Trắc|
1794410565000|13|Hoàng lẻ dòng|
1794410699952|14|Cờ sau Hai Bà|
1794410782777|16|Thánh Thiên/khung dưới thêm thoại|
1794410825874|17|Bàn tính bên bản đồ|
1794410884170|19|Tướng giặc trốn dưới bàn|
1794410933191|20|thủ lẻ dòng|

## Phần suy luận cần lưu ý

- 9 ảnh chỉ khoanh đỏ; ý sửa lấy từ tin nhắn. Đặt lời khấn ở14 và lời thề ở15 dựa theo cảnh, không phải lời phê có đánh số trang.
- “Chuồn/chuần” hiểu là ý chạy thoát. Ở13 bổ sung bàn đường lui dự phòng, không biến thành đã trốn; ở19 làm rõ sợ hãi qua thoại.
- TQ được đối chiếu là Tào Quyền; MT là Mã Tắc. Tên Phùng Công Lực theo yêu cầu mới, không tự theo biến thể storyboard cũ.
- Cờ chưa có mẫu chốt từ giáo viên: đã đặt một quy ước minh họa trơn chung để không mỗi agent vẽ một kiểu; không coi là khảo chứng cờ cổ.
- Tạo hình Thánh Thiên mới được khóa bằng mô tả để agent 4/5 làm song song; cần kiểm mặt cạnh nhau lúc tổng hợp.
- Hình chỉ896×1200px; giữ đúng giới hạn nguồn khi báo chất lượng in.

## Trạng thái thực

Đây là gói phân tích/chuẩn bị nhiệm vụ. Chưa sửa ảnh, chưa hoàn thành trang truyện, chưa ghép PDF sửa. Các lane bắt đầu NOT_STARTED. Main và tài sản sản xuất cũ giữ nguyên. Sau khi5 agent báo READY, coordinator kiểm liên trang và chạy công cụ ghép; không mặc định bản ghép đã được giáo viên duyệt.
