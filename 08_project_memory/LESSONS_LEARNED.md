---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
book_size: "190mm x 240mm (Bleed: 196mm x 246mm @ 300 DPI)"
target_audience: "Học sinh Lớp 8 - Lớp 10 (13-16 tuổi)"
compartment: "08_project_memory"
agent_author: "ChatGPT / Lead Agent (onboarding và rà soát QA)"
status: "IN_REVIEW"
source_grounding: "59 file tại commit 65c2e5a7cf71a1344be7f916c9b675e4325d31c8 và chỉ dẫn trực tiếp ngày 2026-11-09"
review_date: "2026-11-09"
timezone: "Asia/Ho_Chi_Minh"
---

# Kinh nghiệm thực tế từ lần onboarding đầu

## 1. Đếm bằng Git và gắn commit

**Đã gặp:** yêu cầu xác nhận “59 file” nhưng còn phải tạo tài liệu mới. **Cách làm:** chụp danh mục `git ls-tree` ở commit nền, đếm loại file, lập hash. **Bài học:** số file gốc và số file hiện tại là hai số khác nhau; không tiếp tục nói repo chỉ có 59 file sau khi bổ sung.

## 2. Ảnh scan là căn cứ khi các bản Markdown bất đồng

**Đã gặp:** rồng/khổng tước bị đổi chiều, số voi thành 78, số phát tên không nhất quán và giới tính sư phụ khác mô tả scan. **Cách làm:** xem đủ 10 contact sheets, ghi trang PDF/trang sách/file liên quan vào sổ vấn đề. **Bài học:** một khẳng định được sao chép qua nhiều `.md` chưa trở thành bằng chứng. Khi làm chi tiết, crop trang scan đủ nét rồi mới sửa đồng bộ nguồn phân tích → Bible → storyboard → prompt.

## 3. Đọc đúng vai trò của từng tài liệu

Bible hướng dẫn nhận diện; storyboard khóa cảnh/chữ; prompt điều khiển tranh; thông số chế bản điều khiển hình học. **Đã gặp:** Trưng Nhị lam sẫm ở sheet nhưng đỏ/vàng ở prompt cảnh. **Bài học:** mỗi lần sinh trang cần đối chiếu cả hồ sơ và ảnh đã duyệt, không chỉ copy prompt trang.

## 4. Đọc hết không đồng nghĩa sẵn sàng sản xuất

**Đã gặp:** đầy đủ 28 storyboard và 30 prompt bìa/trang nhưng chưa có sheets được chốt, trang kết vượt đoạn nguồn và safe zone mâu thuẫn. **Bài học:** báo cáo riêng tiến độ đọc, tiến độ quyết định và tiến độ sản phẩm; IN_REVIEW không phải APPROVED.

## 5. Đơn vị và hệ tọa độ phải có tên rõ ràng

**Đã gặp:** khung top=8 mm được mô tả đồng thời nằm trọn trong vùng cách trim 14 mm; CSS cắt ở trim nhưng gọi là sẵn in bleed. **Cách làm:** ghi hệ gốc trim và phép dịch +3 mm sang bleed. **Bài học:** kiểm bằng bất đẳng thức tọa độ và hộp PDF thực, không chỉ nhìn con số 300 DPI. Khi crop raster có chênh lẻ 71 px phải phân 35/36 px có chủ ý.

## 6. Không tin nhãn đếm từ có sẵn

**Đã gặp:** nhãn số từ trong storyboard thấp hơn phép đếm theo khoảng trắng. **Cách làm:** chỉ trích lời dẫn, đếm lại và thống kê cụm/tỷ lệ đỏ. **Bài học:** công bố phương pháp đếm; dùng bản dựng font thật để quyết định có đủ 3–5 dòng. Không xóa tự động các dấu tô đỏ cho đạt tỷ lệ.

## 7. Ví dụ mã trong Markdown chưa là công cụ hoàn chỉnh

**Đã gặp:** ngăn 05 có CSS và hàm regex nhưng không có entrypoint, tài nguyên font, script ghép đủ sách hoặc kiểm hộp in. **Bài học:** chỉ mô tả là bộ khung đặc tả; ở nhiệm vụ lập trình sau phải tạo pipeline chạy được rồi kiểm sản phẩm xuất thực tế.

## 8. Git phải giữ thay đổi nhỏ và bí mật ngoài repo

**Cách làm:** dùng remote HTTPS sạch, nhánh QA và commit tài liệu theo phạm vi; chỉ xem push là xong sau khi đối chiếu SHA remote. Thông tin đăng nhập chỉ dùng tạm cho xác thực, không đưa vào docs hay log. **Bài học:** mỗi lần bàn giao ghi nhánh/commit; nếu push lỗi ghi đúng lỗi, không báo đã đồng bộ.

## 9. Tạo mẫu đầu để duyệt ngoại hình, giữ nguyên bản gốc

**Đã làm:** sheet Trưng Trắc v001 chứa cùng một gương mặt ở tang bào và giáp chiến, tên file có phiên bản, prompt nguyên văn và JSON kèm hash. **Quan sát:** nét mực/chì lên rõ nhưng vùng trống 20% không được giữ toàn bề ngang vì mũ lông vũ. **Bài học:** bảng nhân vật và nền trang truyện có công năng khác nhau; không gọi sheet là trang in sẵn. Đo kích thước thực tế sau sinh, chờ chủ dự án duyệt rồi mới dùng làm tham chiếu. Không tự resize để tạo cảm giác đạt độ phân giải in.
