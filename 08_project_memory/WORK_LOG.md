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

# Nhật ký công việc

## 2026-11-09 — ONBOARDING-001

- **Yêu cầu:** nạp toàn bộ 7 ngăn; giữ form 19×24 cm; chưa tạo ảnh; ghi kết quả và kinh nghiệm lên repo.
- **Căn cứ:** 59 file gốc tại commit `65c2e5a7cf71a1344be7f916c9b675e4325d31c8` và chỉ dẫn trực tiếp của chủ dự án trong phiên.
- **Đã làm:** clone; đọc 26 Markdown + .gitignore; xem 32 ảnh; kiểm dải 58 trang scan và 28 storyboard; đo độ dài/cụm đỏ của lời dẫn; đối chiếu prompt, Bible và thông số bố cục.
- **Kết quả cụ thể:** đủ 7 ngăn, baseline 59 file; phân trang A=14/B=10/C=4; 11 lời dẫn vượt 65 đơn vị cách trắng, 11 trang quá 5 cụm đỏ, 14 trang quá tỷ lệ đỏ 35%. Phát hiện chênh lệch nguồn và quy chuẩn; xem [sổ vấn đề](../06_qa_validation_and_delivery/ONBOARDING_ISSUES.md).
- **Hồ sơ tạo mới:** báo cáo sẵn sàng, manifest/hash, bảng kiểm, danh mục vấn đề ở 06; form ở 05; README/nhật ký/quyết định/kinh nghiệm ở 08.
- **Giới hạn:** không có PDF gốc trong repo; chưa xác minh chính sử ngoài tài liệu dự án; chưa tạo ảnh hoặc thực thi chế bản.
- **Bàn giao:** chủ dự án chọn khóa 10 sheets hoặc ưu tiên bìa/trang 01; cần xử lý các vấn đề ảnh hưởng đầu ra trước sản xuất phần tương ứng.
- **Git:** bản cập nhật chuẩn bị trên `agent-06/qa-review`. Xem `git log` để lấy SHA của commit chứa chính nhật ký này; SHA không tự chèn vào file cùng commit. Trạng thái remote phải được xác nhận sau push, không suy ra từ dòng nhật ký.

## 2026-11-09 — ART-001 / Bắt đầu bảng nhân vật

- **Yêu cầu mới:** chủ dự án yêu cầu bắt đầu làm truyện sau onboarding; tiếp tục tuân thủ nguyên tắc nhân vật trước trang truyện.
- **Đã làm:** xem lại Bible, prompt Trưng Trắc và ảnh mẫu ngăn 07; sinh một sheet hai bộ trang phục bằng công cụ tạo ảnh tích hợp.
- **Đầu ra:** [Trưng Trắc v001](../assets_generated/characters/CHAR_01_Trung_Trac_v001.png), [metadata](../assets_generated/characters/CHAR_01_Trung_Trac_v001.json), [prompt và kiểm tra](../04_art_direction_and_image_prompts/production_logs/CHAR_01_Trung_Trac_v001.md).
- **Kiểm tra:** PNG giải mã được; hai khuôn mặt tương đồng; đủ hình toàn thân và đạo cụ; quan sát chưa thấy chữ hoặc watermark. Ảnh gốc 1122×1402 px, chưa gắn nhãn in 300 DPI.
- **Giới hạn:** mũ bên phải đi vào vùng 20% đỉnh; sheet không dùng làm trang ruột; chưa có góc quay sau/nghiêng; chưa được chủ dự án duyệt.
- **Tiến độ:** 1/10 sheets tạo, 0/10 duyệt; 0/28 trang truyện; các vấn đề onboarding chưa tự coi là được giải quyết.
- **Git:** nhánh `agent-04/art-assets-part-1`, kế thừa hồ sơ onboarding; commit và trạng thái push đối chiếu qua Git. Không có token trong ảnh, metadata hoặc tài liệu.
- **Bước tiếp:** chủ dự án duyệt/sửa Trưng Trắc trước khi dùng làm tham chiếu; tiếp tục các bảng theo cùng chất liệu.

## Mẫu ghi tiếp theo

- Mã việc / ngày / người thực hiện.
- Yêu cầu và nguồn đang dùng (file, phiên bản, trang).
- Đầu ra cụ thể và đường dẫn.
- Kiểm tra đã chạy, kết quả, giới hạn.
- Vấn đề còn mở và quyết định cần có.
- Bước tiếp theo, nhánh và commit bàn giao.
