# Agent 5 - PDF 18, 19, 20, 21

Sửa trọn lô, không dừng ở kế hoạch. Nguyên tắc và định nghĩa đầu ra: đọc README.md, 02_quy_chuan/NGUYEN_TAC_SUA.md, 02_quy_chuan/GOI_Y_THOAI.md của ngăn sửa.

## PDF 18 - Dụ địch ở chân núi

- Thêm thoại Thánh Thiên/địch đúng cảnh, thể hiện chủ động dụ địch và sự chủ quan của giặc; không cho địch biết trước toàn bộ bẫy.
- Giữ nhận diện Thánh Thiên đã quy định, sửa phục trang quân Lĩnh Nam và rà cờ, ô vàng.

## PDF 19 - Giặc trốn dưới bàn

- Khung dưới đã khoanh: thêm thoại Tào Quyền/Lục Hiến hoảng sợ, tìm cách chuồn; thêm lời nghĩa quân vạch rõ đã bị vây/bắt, cho thấy trí mưu của đội quân Thánh Thiên.
- Rà trang phục lính bắt giặc; giữ hai khung và hành động, không biến cảnh thành trò hề quá mức.

## PDF 20 - Thánh Thiên tuyên tội

- Dàn lại nguyên cụm “Trảm thủ!” cùng dòng, tuyệt đối không để “thủ!” rơi riêng dòng cuối.
- Thay cờ trang này và kiểm đồng bộ cờ trang sau PDF21.
- Giữ mặt Thánh Thiên đồng bộ; rà trang phục lính. Không bổ sung hình chém đầu trực diện.

## PDF 21 - Trang kết đoàn quân Hai Bà

- Thay cờ toàn cảnh, kể cả cờ nhỏ xa; đồng bộ với các trang trước.
- Sửa trang phục nghĩa quân/Hai Bà; giữ hai voi, đoàn quân và bố cục kết Gemini. Nếu có Thánh Thiên, dùng khóa nhận diện mới.
- Thu gọn ô vàng và rà chữ cuối sách; không tự thêm trang hoặc chuyển thành bộ truyện 28 trang.

## Quyền ghi và đầu ra

Chỉ ghi lane này. Mỗi trang cần text/PDF_XX.json (toàn bộ chữ cuối cùng + người nói + quyết định thay đổi); source/PDF_XX.* (nguồn dàn trang/chỉnh sửa có thể tái tạo, ảnh sạch/mask nếu có); output/PDF_XX.png; output/PDF_XX.pdf (một trang cùng khổ nguồn); qa/PDF_XX.json (copy schema TEMPLATE, kiểm thật). Giữ source một thư mục rõ nếu có nhiều layer; không chỉ giao prompt thay cho ảnh sửa. Cuối lane tạo output/LO_TRANG.pdf và HANDOFF.md nêu điều đã sửa, hạn chế, SHA, trang nào BLOCKED.

Đọc thêm `02_quy_chuan/DAU_RA_VA_QA.md` trong ngăn sửa để dùng đúng schema chữ, QA, evidence và trạng thái READY_FOR_COORDINATOR.
