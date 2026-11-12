# Bàn giao Agent5: PDF18–21

Trạng thái: READY_FOR_COORDINATOR. Đây là4trang PDF vật lý18–21 trong bản Gemini21trang; không phải bộ28trang. Không nhận đã được giáo viên duyệt.

## Sản phẩm thật
- output/LO_TRANG.pdf:4trang18,19,20,21 theo thứ tự.
- output/PDF_18..21.png và .pdf: ảnh896×1200, mỗi PDF1trang430,08×576pt.
- text/PDF_XX.json: toàn bộ lời dẫn, người nói, thoại, thay đổi và tọa độ/chữ đỏ.
- source/PDF_XX_art.png: ảnh đã sửa thật bằng image_gen có tham chiếu gốc; source/build_pages.py + fonts/ + JSON tái tạo dàn trang. Chạy `python3 source/build_pages.py` từ lane này.
- source/PDF_XX_provenance.json: tham chiếu/hashes/ảnh giữ lại; *_edit_spec.txt ghi đặc tả thực tế. Sau lần khởi tạo lại phiên, đặc tả được tái lập, không giả là prompt tiếng Anh nguyên văn.
- qa/PDF_XX.json, *_render.png, *_typography.json và THANH_THIEN_CROSS_LANE.png: kiểm và evidence đã mở.

## Những gì đã sửa
|Trang|Kết quả|
|---|---|
|18|2thoại Thánh Thiên/Tào Quyền, dụ giặc nhưng không lộ bẫy; mặt/khăn tang/áo lục/giáp ngắn theo lane4; giữ2khung|
|19|3thoại ở khung bắt giặc; quần áo nghĩa quân cả xa, giữ câu liêm/hai quan giặc; bỏ cờ sinh thêm để giữ cảnh không cờ như gốc|
|20|“Trảm thủ!” cùng dòng; thay cả6cờ trơn; đồng bộ Thánh Thiên và trang phục lính; không thêm cảnh chém|
|21|Cờ trơn cả xa nhỏ; phục trang Hai Bà/nghĩa quân/Thánh Thiên, giữ2voi/ngựa/trống/sông/bình minh; ô vàng và lời kết gọn|

## Đã kiểm
- Mở cả4PNG cuối và4ảnh render PDF; xem chữ/đuôi thoại/mặt/tay/trang phục/cờ/bố cục.
- Xem trực tiếp ảnh khóa lane4 và ảnh ghép đối chiếu mặt18/20/21: PASS theo khóa chung.
- So khớp render LO_TRANG với4PDF riêng: giống từng trang, đủ thứ tự/kích thước.
- check_packet.py, validate_lane.py agent_5 --ready, --staged và git diff --cached --check được chạy trước phát hành; xem WORK_LOG cho các checkpoint.

## Giới hạn/việc coordinator
- Không có trang BLOCKED_ART. Coordinator rà phong cách/nhận diện toàn21trang và ghép bản sách sau khi đủ5lane; agent5 không tự ghép cả21trang.
- PDF20: hình Gemini vốn chỉ thấy3tù binh trong khi lời kể nhắc Tào Quyền/Lục Hiến và3tướng (5người). Giữ nguyên số người/lời kể theo phạm vi sửa, ghi để coordinator cân nhắc riêng, không âm thầm thêm người.
- Nguồn896×1200; không nâng nhãn DPI rồi nhận đã đạt in300DPI. Cờ/phục trang là quy ước minh họa, không tuyên bố khảo chứng.
- Ảnh sửa có xử lý sinh ảnh nên không phải bảo toàn pixel tuyệt đối ngoài vùng sửa; đã giữ và kiểm bố cục/hành động chính.

## Git
Nhánh duy nhất: sua-theo-gop-y-giao-vien. Chỉ ghi04_agents/agent_5/.
ĐÃ PUSH bản tăng chữ: 068afe447d68f2a5b14f6466767665321a572610. Đã fetch lại và kiểm commit là tổ tiên của đầu nhánh remote. PUBLICATION.json ghi SHA các checkpoint sau rebase và chứng cứ trạng thái.
Lượt trước từng bị chặn quyền push; người dùng đã trực tiếp cho phép ở lượt tăng chữ này, nên giới hạn đó đã được giải quyết.

## Bản tăng chữ mới nhất
Theo góp ý trực tiếp của người dùng: lời dẫn4trang cùng21,5px, thoại cùng18px; giữ nguyên nội dung/chữ đỏ. Đã kiểm bằng mắt tất cảPNG/render mới và đo chiều rộng/chiều cao dòng. Nới ngang2bóng thoại PDF19 để tránh sát viền. QA PASS, xem qa/TYPOGRAPHY_REVISION.json. Đã push repo hiện hành và xác minh remote; trạng thái xuất bản xem PUBLICATION.json.
