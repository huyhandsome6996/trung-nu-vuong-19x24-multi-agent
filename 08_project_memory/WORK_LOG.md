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

## 2026-11-09 — DESIGN-002 / Bộ thiết kế toàn bộ

- **Ủy nhiệm:** chủ dự án yêu cầu tự triển khai thiết kế đầy đủ, chi tiết thành phần, thống nhất và có hướng dẫn cho agent sau; không cần hỏi lại từng lựa chọn mỹ thuật thông thường.
- **Phạm vi:** 41 hồ sơ nhân vật; 12 bối cảnh; 36 nhóm đạo cụ/phương tiện; 4 động vật; 28 trang có bảng phụ thuộc; bộ SVG cho layout và token máy đọc.
- **Đã làm ở checkpoint đầu:** registry/profiles, prompt cho27 ảnh bổ sung, hướng dẫn nhập dự án, tóm tắt truyện2phút, quy chuẩn nét/màu/diễn xuất, sửa8 tài liệu cũ theo scan và hướng nhận diện.
- **Hình đang làm:** ảnh đã tạo được lưu dần có PNG/JSON/hash; xem IMAGE_CATALOG để có số thực tế, không lấy tổng số kế hoạch làm số hoàn thành.
- **Bản chuẩn sử dụng:** DESIGN_BASELINE để agent tiếp tục bản nháp nhất quán; chưa tự ghi chủ dự án duyệt từng ảnh hoặc ảnh in300DPI.
- **Kiểm:** validator kiểm ID, liên kết, file, kích thước/hash; `git diff --check`. Kết quả thị giác và giới hạn sẽ ghi riêng ở QA_DESIGN_REPORT khi đóng bộ.
- **Giới hạn còn lại:** biên tập lời dẫn dài, nguồn phần kết27–28, địa điểm đền, font/ICC/gáy in thuộc bước dựng sách tiếp theo.

### DESIGN-002 — Đóng bộ v1

- Hoàn thành30 bảng hiện hành:17 casting cho41 hồ sơ,1 turnaround,5 bối cảnh,4 đạo cụ,1 quân đội,1 động vật,1 bộ24 mặt tập thể.
- Đã thêm E13/E14 để trang28 có concept nền riêng; E14 là công trình tưởng niệm biểu tượng, không dùng làm ảnh xác minh một di tích thật.
- Sửa ảnh có mục tiêu: PROP04 v001→v002 (bỏ đèn kính/chi tiết yên ngoài thiết kế); PROP03 v001→v002 (huyết sâm đỏ đồng nhất). Giữ ảnh cũ, đánh SUPERSEDED và cập nhật album.
- Registry có41 người,24 mã tộc trưởng tập thể,14 cảnh,36 nhóm đạo cụ,4 động vật. Ma trận bao phủ28 trang; chưa sinh trang truyện.
- Mỗi ảnh mới có prompt, reference_paths thực tế, metadata kích thước/hash. Album30 preview nhẹ, bấm mở gốc; có HTML tìm theo tên/mã và nhóm; không dùng thư viện ngoài.
- Đã xem các bảng hình và khuôn SVG; chạy validator và kiểm link/file/hash. HTML chưa kiểm thị giác Chromium do thiếu binary, đã kiểm asset/cú pháp.
- Tiếp nhận từ `09_design_system/00_READ_FIRST.md` → SOURCE_DECISIONS → IMAGE_CATALOG → PAGE_ASSET_MATRIX → AGENT_HANDOFF. Chuẩn v1 dùng làm bản nháp theo ủy nhiệm, không tự ghi chủ dự án duyệt từng ảnh.
- Git: checkpoint đầu `00b65f2`; bản đóng bộ có commit tiếp theo trên `agent-04/art-assets-part-1`. Xem git log/remote để xác nhận SHA, không nhúng SHA của chính file này vào cùng commit.

## WORKFLOW-003 — Chuẩn hóa repo/main và vận hành A–Z (09/11/2026)

- Yêu cầu: tập trung main, một lối vào cho agent clone và thực hiện A–Z, có phục hồi sau ngắt phiên.
- Hợp nhất fast-forward toàn bộ lịch sử thiết kế/QA vào main, giữ nguồn và ảnh; thay hướng dẫn branch/PR đang vận hành. Các nhánh cũ chỉ dọn sau khi kiểm main remote chứa đủ commit.
- Tạo START_HERE, cập nhật AGENTS/README, thêm Ngăn 10 với quy trình, prompt giao agent, queue 125 task, ma trận công cụ/đầu ra, phục hồi và đổi phiên bản. Tạo packet PAGE01_TEXT thật với nguồn chữ và đường dẫn/hash ảnh ứng viên active.
- Thêm CLI doctor/status/next/packet/start/checkpoint/block/unblock/finish/reopen/check; evidence và dependency có kiểm. Thêm helper HTML proof từ chữ locked/ảnh/font thật, không tự coi là file in.
- Thêm check_repo, requirements, mẫu cấu hình GitHub Actions kiểm main (chưa kích hoạt) và 8 kiểm thử logic phục hồi/phụ thuộc/report/hash/stale source/ảnh native/path/keyword. Tests chạy đạt; check workflow/design/link/hash/whitespace đã đạt. GitHub từ chối kích hoạt CI vì PAT thiếu workflow scope; mẫu YAML được giữ ở Ngăn 10, không có workflow hoạt động. Bộ kiểm tra local đã chạy đạt.
- Sửa BOOK_STRUCTURE còn sót “78 voi” thành 8 voi đực da xám ở Hát Môn; không sửa 32 JPG nguồn. Đánh dấu riêng phân biệt QA pass/USER_APPROVED/PRINT_READY ở các đặc tả cũ.
- Phạm vi hoàn thành là hạ tầng vận hành và hợp nhất, chưa sinh 28 trang truyện hoặc file in. Queue ban đầu vẫn 2 baseline done, 122 todo, SOURCE_EPILOGUE blocked; bước tiếp PAGE01_TEXT. Thiếu công cụ/dữ liệu thì block đúng bước, không tự bịa kết quả.

- Giới hạn push đã xử lý: lần push đầu bị GitHub từ chối vì tạo workflow mà PAT không có workflow scope. Chuyển YAML thành mẫu trong Ngăn 10, sửa commit local chưa công bố để không yêu cầu quyền đó; không tìm cách vượt kiểm soát quyền GitHub.

### Kết quả đồng bộ WORKFLOW-003

- Main remote đã nhận commit3fec447, SHA local/remote khớp. Hai nhánh agent-04/art-assets-part-1 và agent-06/qa-review đã được xác nhận là tổ tiên của main rồi xóa trên remote và local; toàn bộ lịch sử vẫn nằm trong main.
- Tạo một bản clone sạch từ commit main đã lưu, chạy check_repo và8tests đều đạt; next chọn PAGE01_TEXT, packet sinh lại không làm bẩn working tree. Đây là kiểm bản clone local, không phải khẳng định đã tải và kiểm trên mọi máy.
- CI tự động chưa kích hoạt do token thiếu workflow scope; mẫu cấu hình sẵn ở Ngăn10. Các lệnh kiểm local dùng được đầy đủ.
