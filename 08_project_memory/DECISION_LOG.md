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

# Sổ quyết định

| Mã | Quyết định / căn cứ | Phạm vi | Trạng thái |
| --- | --- | --- | --- |
| D-001 | Chủ dự án yêu cầu nạp toàn bộ repo, chưa tạo ảnh đến khi có lệnh. | Phiên onboarding chỉ đọc, đối chiếu, ghi hồ sơ và cập nhật GitHub. | Đang áp dụng. |
| D-002 | Chủ dự án yêu cầu việc hoàn thành phải cập nhật repo, tạo ngăn kinh nghiệm và tận dụng Markdown. | Bổ sung ngăn vận hành 08, hồ sơ QA ở 06, form ở 05; giữ 7 ngăn gốc. | Đã thực hiện ở bản thay đổi này. |
| D-003 | Giao thức repo dành `main` cho nội dung được duyệt và có nhánh `agent-06/qa-review`. | Bản onboarding trạng thái IN_REVIEW đưa lên nhánh QA để xem xét; chưa sửa nguồn hoặc tự nhập main. | Đã chọn nhánh. |
| D-004 | Kết quả kiểm kê Git: 59 file = 26 MD + 32 JPG + .gitignore. | Mọi xác nhận “59 file” phải gắn commit nền; tổng file tăng khi bổ sung tài liệu. | Đã kiểm chứng. |
| D-005 | Chỉ dẫn trực tiếp yêu cầu 10 bảng nhân vật, tạo/chốt trước trang 01–28. | Đề xuất bắt đầu bằng khóa hồ sơ và sheets; không tự tạo bìa/trang trước khi được chọn bước. | Chờ lệnh tạo ảnh. |
| D-006 | Phát hiện mâu thuẫn có bằng chứng scan và hình học. | Ghi sổ vấn đề; không sửa dây chuyền nguyên tác/storyboard/prompt trong nhiệm vụ onboarding. | Chờ xử lý ở nhiệm vụ kế tiếp. |
| D-007 | Chủ dự án yêu cầu bắt đầu sau onboarding. Chọn bước đầu có thể duyệt độc lập theo thứ tự character-first: Trưng Trắc với hai giai đoạn phục trang. | Đã sinh v001 và ghi IN_REVIEW; chưa coi lệnh bắt đầu là phê duyệt ngoại hình. | Đã tạo, chờ duyệt ảnh. |

Khi thay quyết định: ghi mã mới, ngày, người quyết định, tài liệu/ảnh ảnh hưởng và quyết định nào được thay thế. Không ghi một đề xuất thành quyết định chủ dự án đã phê duyệt.

## D-008 — Ủy nhiệm thiết kế tổng thể

Ngày09/11/2026 chủ dự án muốn agent chủ động thiết kế đầy đủ và bàn giao cho agent sau, không yêu cầu họ tự đọc truyện rồi quyết từng chi tiết. Chọn bộ30 bảngv1 làm DESIGN_BASELINE; tách trạng thái này với phê duyệt từng ảnh và trạng thái file in. Mở rộng10 bảng casting ban đầu lên17 để bao phủ các vai thiếu;24 mã mặt tập thể lưu riêng, không đổi thành tên nhân vật bịa thêm.

## D-009 — Chỉnh theo bằng chứng và kiểm hình

Dùng scan để sửa giới tính Đô sư phụ, số voi, chiều hóa rồng/khổng tước và mười phát tên. Dùng ảnh sinh thực tế để cập nhật màu khăn tộc trưởng, không giả định prompt đã được tuân thủ hoàn toàn. Hai bản đạo cụv002 thay bảnv001, giữ v001 trong repo để truy vết.

## D-010 — Phần kết và trang trí

E13/E14 được thiết kế như concept kết mở rộng; không tự khẳng định một ngôi đền hư cấu là đền thật. Giữ tọa độ mép giấy cổ như trang trí, chữ nằm trong vùng an toàn riêng. Nguồn phần kết và thông số nhà in phải kiểm ở bước xuất sách.
