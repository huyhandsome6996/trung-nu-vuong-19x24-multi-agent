---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
compartment: "05_book_design_and_layout_19x24"
owner_agent: "AGENT-05 (Book Designer & Layout Engineer)"
consumers: ["AGENT-05", "AGENT-06"]
---

# HƯỚNG DẪN SỬ DỤNG NGĂN 05: THIẾT KẾ BÌA, DÀN TRANG & CHẾ BẢN KHỔ 19x24 CM (`05_book_design_and_layout_19x24`)

## 1. Mục đích của Ngăn 05
Ngăn 05 chứa toàn bộ **Thông số Kỹ thuật Thiết kế Đồ họa, Quy chuẩn Chế bản In ấn Khổ 19×24 cm, Thiết kế Bìa Sách (Trước – Gáy – Sau), Tọa độ Khung Dẫn Truyện Giấy Cổ (Narration Box), Quy chuẩn Typography Tiếng Việt và Mã nguồn HTML/CSS/Python Tự động Dàn trang**.

Sau khi `AGENT-03` hoàn thành kịch bản chữ (Ngăn 03) và `AGENT-04` sinh xong bộ tranh nền không chữ (Ngăn 04), `AGENT-05` sẽ sử dụng các tài liệu trong Ngăn 05 này để lắp ghép thành **sách hoàn chỉnh chuẩn in ấn 19×24 cm ở độ phân giải 300 DPI**.

## 2. Danh mục Tài liệu trong Ngăn 05 & Cách Áp dụng

| Tên File Markdown | Nội dung Chuyên môn | Agent Nào Thực thi? | Hướng dẫn Sử dụng Cụ thể |
| :--- | :--- | :--- | :--- |
| `COVER_DESIGN_SPEC_19x24.md` | Bản vẽ kỹ thuật chi tiết cho **Bìa Trước, Gáy Sách và Bìa Sau khổ 19×24 cm**: Tọa độ từng lớp chữ (Typography 4 tầng học từ bìa *An Dương Vương* mẫu `JPG #22`), hiệu ứng viền chữ, vùng an toàn, vùng tràn lề 3mm, khung tóm tắt bìa sau và vị trí mã vạch ISBN. | `AGENT-05` (Book Designer) | Dùng để thiết kế file Bìa rời (`Front_Cover_19x24.pdf`) và Bìa trải toàn bộ (`Full_Cover_Spread_389.5x246mm.pdf`). |
| `PAGE_LAYOUT_TEMPLATES_19x24.md` | Thông số tọa độ chính xác đến từng `mm` và `px` (ở 300 DPI) của **Khung dẫn truyện giấy cổ (Top Parchment Box)**, **3 Mẫu chia khung (Template A, B, C)**, **Bóng thoại (Speech Bubbles)** và quy tắc chọn Font chữ tiếng Việt + tô đỏ từ khóa (`#C81E1E`). | `AGENT-05` (Typesetter) | Dùng làm thông số chuẩn khi dàn 28 trang ruột từ Trang 01 đến Trang 28. |
| `CSS_AND_INDESIGN_AUTOMATION_SPEC.md` | Bộ khung mã nguồn **HTML5/CSS3 Print (`@page { size: 190mm 240mm; }`)** và **Script Python (Pillow / Chromium PDF)** giúp AI Agent tự động ghép ảnh nền + vẽ khung giấy cổ + tô đỏ các từ khóa trong `**...**` và xuất thẳng ra file PDF/JPG chuẩn 19×24 cm! | `AGENT-05` (Automation Engineer) | Chạy trực tiếp trên môi trường máy ảo hoặc CI/CD của GitHub để đóng gói sách tự động. |
