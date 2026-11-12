# Bàn giao Agent 1 — PDF01–05

Trạng thái: READY_FOR_COORDINATOR. Hoàn thành 5/5 trang, không có BLOCKED_ART. Đây là lô 5 trang vật lý của PDF Gemini 21 trang, tính bìa là 01; không phải bộ sản xuất 28 trang cũ.

## Sản phẩm thật

- `output/PDF_01.png` … `PDF_05.png`: 896 × 1200 px.
- `output/PDF_01.pdf` … `PDF_05.pdf`: một trang mỗi file, MediaBox 430,08 × 576 pt.
- `output/LO_TRANG.pdf`: 5 trang theo thứ tự 01–05, cùng khổ nguồn.
- `text/PDF_XX.json`: toàn bộ chữ cuối, người viết thư/người nói nếu có và quyết định sửa.
- `source/PDF_XX/`: ảnh sửa thật từ image_gen.imagegen, prompt, provenance/hash tham chiếu, ảnh ghép, mask, layout từng dòng; `source/build_pages.py` và font đính kèm tái tạo dàn trang.
- `qa/PDF_XX.json`: kết quả từng yêu cầu và ảnh render Poppler đã mở kiểm.

## Điều đã sửa

|Trang|Sửa|
|---|---|
|01|Tất cả cờ lớn/nhỏ đỏ đất trơn; trang phục/khăn lính; giữ nguyên tiêu đề, phụ đề và câu dẫn.|
|02|Bỏ nhãn/dấu *; thuật ngữ trong ngoặc kép; chú giải đủ nghĩa, in nghiêng; ô vàng gọn, giữ tranh quân Hán gốc.|
|03|Thành phía sau đôi nhân vật → ruộng lúa/trâu; trang phục và ô vàng; giữ lời dẫn và ba khung.|
|04|Phùng Công Lực ở hai chỗ đại từ ông; Nay vợ chồng Phùng Thị Chính; theo Thi Sách và Trưng Trắc; rà cờ/trang phục hồi tưởng.|
|05|Một hôm, chim câu…; mật thư và 27/70/8 giữ nguyên; ô vàng, trang phục, cờ gần/xa.|

Không thêm bóng thoại. Không đổi cốt truyện hoặc dùng thiết kế cũ làm nền. Phần tranh được chỉnh bằng tham chiếu gốc, rồi chọn vùng bằng mask; chữ mới dùng font Việt thật.

## Git và phạm vi

Nhánh duy nhất: `sua-theo-gop-y-giao-vien`. Toàn bộ thay đổi thuộc `11_sua_theo_gop_y_giao_vien/04_agents/agent_1/`.

SHA checkpoint hoàn tất tranh/chữ PDF05: `5393dfb388a56d483f23ca09d6e7625526be597d`. Năm checkpoint từng trang nằm ở `qa/CHECKPOINT_COMMITS.json`. Commit bàn giao sau checkpoint chứa trạng thái READY, lô PDF và tài liệu này. Các SHA này là checkpoint lịch sử của clone tạm đã mất; bản khôi phục có commit xuất bản mới dưới đây.

## QA và giới hạn

Đã mở đủ PNG sửa và ảnh render PDF bằng Poppler. Chữ trích xuất PDF02–05 khớp hoàn toàn JSON khi chuẩn hoá khoảng trắng; bìa giữ chữ raster gốc và đã đọc kiểm. Các kiểm kỹ thuật cuối được ghi trong `qa/TECHNICAL_CHECKS.md`.

Coordinator còn phải rà liên lane về cờ/trang phục và nhận diện trước ghép 21 trang; mục liên lane PENDING được giữ rõ trong STATUS/QA. Lô này không có Thánh Thiên để đối chiếu lane 4/5.

Nguồn tranh 896 × 1200 px, khoảng 150 ppi ở khổ PDF này; không tuyên bố đạt in 300 DPI. Cờ và trang phục theo quy ước minh hoạ/tài liệu người dùng, không phải chứng nhận khảo cổ. Chi tiết nét bút trong vùng sửa sinh có thể khác ảnh gốc; vùng ngoài mask giữ JPEG gốc. PASS là QA của agent, chưa phải giáo viên duyệt.

## Xuất bản GitHub đã xác nhận

Người dùng đã trực tiếp cho phép push. Commit nội dung `7280294e974c89010e0b50d2fe7ad421907d3092` đã có trên nhánh `sua-theo-gop-y-giao-vien`; đã fetch và kiểm tổ tiên thành công. Chi tiết ở `qa/PUBLISH.json`.

Clone tạm cũ đã mất khi môi trường làm mới; 77 tệp lane được khôi phục nguyên byte từ ZIP bàn giao và ghi bằng commit mới. PDF lô giữ SHA256 `69839cdf7ca4e19aef78eab00114bc7b26c30c80795cd4af2cd160f884ddc36c`. Giữ nguyên công việc agent_4 trên remote. Các đối tượng commit cũ không có trong ZIP, SHA cũ chỉ dùng truy nguyên lịch sử.
