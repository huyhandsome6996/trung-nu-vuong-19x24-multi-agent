---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
compartment: "03_storyboards_and_scripts"
owner_agent: "AGENT-03 (Storyboard & Script Architect)"
consumers: ["AGENT-04", "AGENT-05", "AGENT-06"]
---

# HƯỚNG DẪN SỬ DỤNG NGĂN 03: KỊCH BẢN PHÂN CẢNH CHI TIẾT TỪNG TRANG (`03_storyboards_and_scripts`)

## 1. Mục đích của Ngăn 03
Ngăn 03 chứa **Toàn bộ Kịch bản Phân cảnh Chi tiết Từng Trang (Page-by-Page Storyboards & Final Text Scripts)** đã được biên soạn hoàn chỉnh từ 58 trang `TRƯNG NỮ VƯƠNG.pdf` và thiết kế theo đúng khuôn mẫu của 22 bức ảnh `.jpg` *Truyền thuyết An Dương Vương*.

Bất kỳ AI Agent nào bước vào Ngăn 03 sẽ có ngay trong tay:
- Cấu trúc tổng thể cuốn sách in khổ **19×24 cm** (**32 trang chuẩn in ấn offset**, bao gồm 28 trang truyện minh họa + 4 trang Bìa/Phụ lục).
- Nguyên văn **Lời dẫn truyện (Narration Box)** của từng trang từ Trang 01 đến Trang 28, trong đó các từ khóa cần **TÔ MÀU ĐỎ (`#C81E1E`)** đã được đánh dấu `**in đậm**` rõ ràng.
- Nguyên văn **Lời thoại nhân vật (Speech Bubbles)** trên từng trang.
- Chỉ dẫn bố cục khung hình (**Template A / B / C**) và mô tả chi tiết Tiền cảnh – Trung cảnh – Hậu cảnh của từng trang.

## 2. Danh mục Tài liệu trong Ngăn 03 & Cách Sử dụng

| Tên File Markdown | Nội dung Trọng tâm | Agent Nào Sử dụng? | Nhiệm vụ Cụ thể với File |
| :--- | :--- | :--- | :--- |
| `BOOK_STRUCTURE_AND_PACING.md` | Sơ đồ cấu trúc cuốn sách 32 trang khổ 19×24cm (Chia tay sách in offset, phân bổ nhịp điệu kịch tính qua 4 chương nhỏ từ Hồi 7 & Hồi 8). | `AGENT-03`, `AGENT-05` (Dàn trang), `AGENT-06` (QA) | Dùng để kiểm soát số trang chẵn/lẻ (Trang Trái - Verso / Trang Phải - Recto) và vị trí các trang cao trào mở đôi. |
| `STORYBOARD_PART_1_HOI_7_CHU_DIEN.md` | **Kịch bản chi tiết Trang 01 đến Trang 14** (Chuyển thể trọn vẹn **Hồi thứ Bảy**: Âm mưu Luy Lâu -> Huyền tích Vua Hùng & họ Phùng -> Mật thư Trưng Trắc -> Trận tử chiến của Thi Sách ở Chu Diên -> Lời thề Cổ Lôi sơn trang). | `AGENT-04` (Sinh ảnh), `AGENT-05` (Ghép chữ & dàn trang) | `AGENT-04` đọc phần *Mô tả Khung hình* để sinh ảnh nền; `AGENT-05` copy nguyên văn phần *Text Khung Dẫn Truyện* và *Bóng Thoại* để chế bản lên trang 19×24cm. |
| `STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md` | **Kịch bản chi tiết Trang 15 đến Trang 28** (Chuyển thể trọn vẹn **Hồi thứ Tám**: Pháp trường Luy Lâu -> Đại lễ Tế cờ và Lời thề Hát Môn dậy sóng Nhị Hà -> Nữ tướng Thánh Thiên tụ nghĩa -> Đại thắng khe Mãng Xà trảm Tào Quyền). | `AGENT-04` (Sinh ảnh), `AGENT-05` (Ghép chữ & dàn trang) | Thực hiện tương tự Phần 1 cho 14 trang nửa sau của cuốn sách. |

## 3. Quy tắc Đọc Ký hiệu Trong Kịch bản Phân cảnh
- Trong mục **Text Khung Dẫn Truyện (Top Narration Box)**:
  - Các chữ viết thường: Hiển thị bằng màu **Đen than (`#1A1A1A`)**.
  - Các chữ nằm trong cặp dấu sao đôi `**...**`: **BẮT BUỘC hiển thị bằng màu Đỏ son (`#C81E1E`)** giống hệt phong cách tô đỏ từ khóa trong 22 ảnh mẫu `.jpg` *An Dương Vương*.
- Trong mục **Loại Bố Cục (Layout Template)**:
  - `Template A (Full-Page Splash)`: 1 tranh toàn trang + 1 khung dẫn ở đỉnh.
  - `Template B (2-Panel Split)`: 2 khung tranh chia ngang/chéo + 1 khung dẫn ở đỉnh (+ bóng thoại nếu có).
  - `Template C (Multi-Panel / Inset Zoom)`: 2–3 khung tranh + khung tròn phóng cận cảnh chi tiết + bóng thoại.
