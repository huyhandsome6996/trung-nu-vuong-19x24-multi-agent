# Hướng dẫn tiếp quản dự án

- Bắt đầu tại `09_design_system/00_READ_FIRST.md`, `SOURCE_DECISIONS.md`, `AGENT_HANDOFF.md` và `08_project_memory/WORK_LOG.md`.
- Chỉ dẫn trực tiếp mới nhất của chủ dự án ưu tiên hơn hồ sơ cũ. Tôn trọng phạm vi thiết kế hoặc trang truyện được giao.
- Tư liệu nguồn ngăn07 giữ nguyên. Với mâu thuẫn đã đối chiếu, dùng SOURCE_DECISIONS; không copy lại lỗi “hai nữ sư phụ”, 78 voi hay ba mũi tên đồng thời.
- Nhân vật, bối cảnh và đạo cụ dùng mã trong `design_registry.json`; dùng ảnh tham chiếu thật từ IMAGE_CATALOG khi sinh ảnh, không chỉ đọc mô tả chữ.
- Giữ Trưng Nhị lam sẫm, Thi Sách tía/hổ phù ngực, Thánh Thiên lục/khăn tang. Không dùng mặt Trưng Trắc cho mọi nhân vật nữ.
- Tạo bản nháp trang sau khi chọn bộ tham chiếu hiện hành; DESIGN_BASELINE không phải tuyên bố chủ dự án đã duyệt từng ảnh. Không tự gắn APPROVED hoặc print-ready.
- Ảnh nền không chữ; chữ Việt ghép riêng, cụm sao đôi trong lời dẫn tô #C81E1E. Khổ và safe text theo layout_tokens, ghi rõ ngoại lệ mép trang trí giấy cổ.
- Trang27–28 là đoạn kết mở rộng cần nguồn bổ sung; không tự coi minh họa tưởng tượng là ảnh đúng một ngôi đền cụ thể.
- Không ghi đè ảnh đã có; tạo v002, ghi prompt, nguồn tham chiếu, kích thước/hash và ảnh hưởng các trang khi thay đổi.
- Trước commit chạy `python 09_design_system/validate_design_system.py` và `git diff --check`; bàn giao trọn bộ ảnh dùng thêm `--complete`. Kiểm kỹ thuật không thay kiểm thị giác.
- Cập nhật WORK_LOG, LESSONS_LEARNED và commit/push sau từng phần hoàn thành. Không lưu PAT hoặc mật khẩu vào repo.
