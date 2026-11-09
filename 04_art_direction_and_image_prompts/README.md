---

> Vận hành hiện hành: [START_HERE](../START_HERE.md) → [WorkflowA–Z](../10_agent_workflow/WORKFLOW_A_TO_Z.md). Chỉ làm trên main; nếu hướng dẫn cũ bên dưới nói chia nhánh/PR, dùng giao thức main ởNgăn10.
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
compartment: "04_art_direction_and_image_prompts"
owner_agent: "AGENT-04 (Art Director & Prompt Engineer)"
consumers: ["AGENT-04", "AGENT-05", "AGENT-06"]
---

# HƯỚNG DẪN SỬ DỤNG NGĂN 04: CHỈ ĐẠO MỸ THUẬT & KHO PROMPT TẠO ẢNH (`04_art_direction_and_image_prompts`)

## 1. Mục đích của Ngăn 04
Ngăn 04 cung cấp toàn bộ **Cẩm nang Mỹ thuật (Visual Style Bible)**, **Prompt Thiết kế Nhân vật gốc (Character Turnaround Prompts)** và **Thư viện Prompt Tạo Ảnh Từng Trang (Bìa Trước + Bìa Sau + 28 Trang Truyện)** để bất kỳ AI Agent tạo ảnh nào (sử dụng Midjourney v6.1, Flux.1 Pro, Google Imagen 3, hoặc Stable Diffusion XL) có thể sinh ra bộ tranh đồng nhất 100% với phong cách của 22 bức ảnh `.jpg` mẫu (*Truyền thuyết An Dương Vương*).

## 2. Danh mục Tài liệu trong Ngăn 04 & Hướng dẫn Thực thi

| Tên File Markdown | Nội dung Trọng tâm | Agent Nào Sử dụng? | Quy trình Thực thi Bắt buộc |
| :--- | :--- | :--- | :--- |
| `VISUAL_STYLE_BIBLE.md` | Giải mã ADN mỹ thuật từ bộ ảnh `.jpg` mẫu: Kỹ thuật đi nét mực đen đan chéo (ink cross-hatching), chất liệu màu chì/màu nước cổ điển, bảng màu hào hùng dân tộc, kiến trúc và phục trang thời Hai Bà Trưng. | `AGENT-04`, `AGENT-05`, `AGENT-06` | Đọc trước tiên để gắn chuỗi **Master Style Prefix/Suffix** vào mọi câu lệnh tạo ảnh. |
| `CHARACTER_DESIGN_PROMPTS.md` | Bộ Prompt chuẩn tạo **10 Bảng Tham chiếu Nhân vật (Character Reference Sheets)** trước khi vẽ các trang truyện. | `AGENT-04` (Image Generator) | **BẮT BUỘC chạy bước này trước khi vẽ Trang 01–28:** Sinh ra 10 ảnh nhân vật gốc rồi truyền ID ảnh vào tham số `image_references` (hoặc `--cref` trong Midjourney) khi vẽ các trang truyện để giữ nguyên gương mặt và giáp trụ. |
| `COVER_AND_PAGE_PROMPTS_LIBRARY.md` | Bộ Prompt chi tiết cho **Bìa Trước, Bìa Sau và toàn bộ 28 Trang Truyện** (khớp 1-1 với Kịch bản phân cảnh ở Ngăn 03). | `AGENT-04` (Image Generator) | Copy trực tiếp từng Prompt, kết hợp với ảnh tham chiếu nhân vật tương ứng để sinh ảnh tỷ lệ `3:4` hoặc `4:5` (chuẩn khổ sách 19×24cm). |

## 3. Ba Nguyên tắc Vàng Khi Sinh Ảnh bằng AI (Golden Generation Rules)
1. **Luôn tạo ảnh KHÔNG CHỨA CHỮ (`clean composition, text-free, no speech bubbles, no watermarks`):** Các mô hình sinh ảnh thường làm hỏng dấu tiếng Việt nếu để AI tự vẽ chữ vào ảnh. Vì vậy, `AGENT-04` chỉ sinh **tranh minh họa nền sạch chữ (có chừa 20% vùng thoáng ở đỉnh trang)**, sau đó `AGENT-05` sẽ dùng code/công cụ dàn trang ở Ngăn 05 để đặt Khung giấy cổ và chữ tiếng Việt sắc nét chuẩn in ấn 300 DPI lên trên!
2. **Luôn giữ vùng Đỉnh Trang thoáng (Top 20% Safe Headroom):** Trong mọi Prompt trang ruột đều đã cài sẵn cụm từ *"leave generous sky/ceiling negative space in the top 20% of the vertical frame for a narration scroll box"* để khi đặt khung dẫn truyện không bao giờ đè lên đầu nhân vật.
3. **Sử dụng Ảnh Mẫu Ngăn 07 làm Style Reference (`--sref` / `image_references`):** Khuyến khích truyền kèm 1–2 bức ảnh trong `07_reference_assets/sample_an_duong_vuong_sorted/` (ví dụ `06_Page_06.jpg` cho cảnh chiến trận, `01_Page_01.jpg` cho đại cảnh thành trì) làm Style Reference để AI khóa đúng chất liệu nét mực và hạt màu cổ điển.
