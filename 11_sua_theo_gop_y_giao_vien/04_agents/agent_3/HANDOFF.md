# Bàn giao Agent 3 — PDF10–14

Trạng thái: READY_FOR_COORDINATOR. Không có BLOCKED_ART. Chỉ thay file trong lane agent_3 trên nhánh sua-theo-gop-y-giao-vien.

## Sản phẩm thật

- `output/LO_TRANG.pdf`:5trang đúng thứ tự PDF10–14, MediaBox430,08×576pt.
- Mỗi trang có `output/PDF_XX.png`896×1200px, `output/PDF_XX.pdf`, `text/PDF_XX.json` đầy đủ lời dẫn/thoại/người nói, `qa/PDF_XX.json`, ảnh render kiểm riêng.
- `source/PDF_XX/art_master.png`:ảnh ART đã chỉnh bằng image_gen có gốc Gemini làm tham chiếu; `edit_recipe.json` ghi prompt thực dùng, `layout.json` vị trí/dòng/font, `provenance.json` hash nguồn/đầu ra.
- `source/build_pages.py` và font kèm giấy phép tái tạo dàn chữ/PDF/PNG từ ART đã lưu; `source/assemble_lane.py` tái tạo PDF lô. Tạo ảnh lại từ prompt có tính ngẫu nhiên; tái xuất từ ART đã lưu không phụ thuộc gọi AI.

## Nội dung sửa

|Trang|Kết quả|
|---|---|
|10|Cờ đỏ đất trơn, phục trang nghĩa quân, ô dẫn gọn.|
|11|Thu ô dẫn từ khoảng310 còn178px; cờ quân Hán xám than; giữ giáp Hán và cổng thành.|
|12|Sửa quân Lĩnh Nam cả hai khung, cờ trơn, giữ tang phục và kiếm Trưng Trắc.|
|13|Phượng Hoàng cùng dòng, thống nhất Tào Quyền theo nguồn; thêm3thoại bàn kế/đường lui dự phòng; phân biệt quân Lĩnh Nam và Hán.|
|14|Rà toàn bộ cờ trên đàn/bờ/thuyền/sau Hai Bà; thêm2lời khấn chuyển thể, giữ đàn/sông/hai khung; sửa lẻ dòng non sông/chẳng lui.|

## Kiểm đã thực hiện

- Mở trực tiếp5JPEG gốc,5ảnh khoanh,4ảnh tham khảo; không dùng hình thiết kế cũ.
- Mở5PNG đầu ra và5render PDF bằng mắt; PDF14 đã mở lại sau sửa lẻ dòng.
- Kiểm chữ trích xuất từ PDF khớp lời dẫn và mọi câu thoại trong JSON.
- Render5trang lô so khớp byte pixel với5PDF riêng, tất cả khớp.
- `check_packet.py`:PASS. `validate_lane.py agent_3 --staged`:PASS ở từng checkpoint. `git diff --cached --check`:PASS. Kiểm `--ready` được ghi ở checkpoint bàn giao.

## Giới hạn và việc coordinator cần rà

- Kiểm nhận diện Hai Bà/trang phục liên lane còn PENDING. Không tuyên bố toàn truyện đã đồng bộ/giáo viên đã duyệt.
- PDF14 giữ nguyên lời dẫn Gemini “cờ ngũ sắc”, “8 thớt voi trắng”, “hơn100chiến thuyền” theo phạm vi sửa; hình cờ áp quy ước đỏ đất chung. Nguồn truyện cũ ghi voi đực da xám. Coordinator quyết định nếu mở rộng sửa lời dẫn, không tự đổi sự kiện/số lượng ở lane này.
- Chỉ thị sửa cờ/trang phục là quy ước minh họa, không phải xác nhận khảo cổ.
- Nguồn896×1200px; ART chỉnh1084×1451px không đồng nghĩa chi tiết gốc đạt300DPI. Giữ khổ PDF gốc.
- Chỉnh sinh ảnh có thể đổi nét nhỏ ngoài vùng sửa; đã kiểm giữ bố cục/nhân vật/hành động chính, không khẳng định pixel nguyên vẹn tuyệt đối.

## Commit checkpoint

```text
9bd381a sua giao vien: agent_3 kiem xong PDF14
9457222 sua giao vien: agent_3 kiem xong PDF13
4495f1a sua giao vien: agent_3 kiem xong PDF12
35fcbf6 sua giao vien: agent_3 kiem xong PDF11
9bc4e74 sua giao vien: agent_3 kiem xong PDF10 va chuan bi chu 10-14
```

Commit bàn giao là commit chứa HANDOFF này (xem git log). Chỉ báo đã push sau khi xác minh commit là tổ tiên của đầu nhánh remote.

## Trạng thái xuất bản remote

Người dùng đã cấp xác thực và yêu cầu push ngày12/11/2026. Đã khôi phục các commit từ bundle lên sau commit Agent4 trên đúng nhánh; chỉ thay lane agent_3. Đang đẩy bằng fetch/rebase/push thông thường, không force-push. Kết quả xác minh sẽ ghi sau khi commit thực sự có trên remote.
