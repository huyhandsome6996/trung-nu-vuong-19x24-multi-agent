# Prompt tiếp quản — copy gửi agent sau

```text
Tiếp quản bộ thiết kế Trưng Nữ Vương v1 tại repo:
https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent
Nhánh có bộ thiết kế đầy đủ: agent-04/art-assets-part-1.

Clone đúng nhánh:
git clone --branch agent-04/art-assets-part-1 --single-branch https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent.git

Đọc theo thứ tự: AGENTS.md → 09_design_system/00_READ_FIRST.md → SOURCE_DECISIONS.md → MASTER_ART_DIRECTION.md → IMAGE_CATALOG.md → PAGE_ASSET_MATRIX.md → AGENT_HANDOFF.md → 08_project_memory/WORK_LOG.md.

Xem pixel ảnh thực, không chỉ đọc prompt. Dùng design_registry.json/crowd_registry.json để tra mã nhân vật/cảnh/đạo cụ, image_jobs.json và JSON cạnh PNG để lấy đúng phiên bản. PROP03 và PROP04 dùng v002, không dùng v001 đã SUPERSEDED. Có30 bảng concept hiện hành,41 hồ sơ người và24 mã mặt tộc trưởng; không gọi đây là30 trang truyện đã hoàn thành.

Giữ mặt, tóc, màu, trang phục theo giai đoạn và đạo cụ. Trưng Nhị lam sẫm; Thi Sách tía/hổ phù; Thánh Thiên lục/khăn tang. Các cảnh truyền thuyết và kết mở rộng không biến thành dữ kiện chính sử không có nguồn. Bảng đền là không gian tưởng niệm biểu tượng, chưa phải ảnh địa điểm thật.

Trước khi vẽ trang: chọn đúng hàng trong PAGE_ASSET_MATRIX, đọc nguyên trang storyboard và các đính chính nguồn, truyền ảnh tham chiếu thực tế. Tranh nền sạch chữ, chừa20% đỉnh; ghép chữ Việt riêng. Trim190×240mm, bleed196×246mm,300DPI ở thành phẩm; concept sheet chưa phải ảnh in. Cụm **...** trong lời dẫn tô đỏ #C81E1E. Dùng layout_tokens cho tọa độ và ngoại lệ mép giấy cổ.

Không tự vẽ lại toàn bộ hồ sơ, không đổi chuẩn giữa các trang. Nếu cần sửa ảnh, tạo phiên bản mới, cập nhật catalog/metadata/nhật ký và nêu trang bị ảnh hưởng. Sau mỗi phần hoàn thành kiểm kỹ thuật/ảnh, commit và push. Không lưu PAT vào repo. Chạy python 09_design_system/validate_design_system.py --complete và git diff --check trước bàn giao trọn bộ.
```

Prompt này chỉ nạp bối cảnh và chuẩn làm việc; chủ dự án sẽ giao phạm vi trang hoặc phần việc tiếp theo. Nếu main chưa có thiết kếv1, không clone main rồi kết luận thiếu tài liệu.
