---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
compartment: "02_historical_fairy_tale_adaptation"
owner_agent: "AGENT-02 (Historical & Literary Adapter)"
consumers: ["AGENT-03", "AGENT-04", "AGENT-06"]
---

# HƯỚNG DẪN SỬ DỤNG NGĂN 02: CHUYỂN THỂ VĂN HỌC & CẨM NANG NHÂN VẬT LỚP 8–10 (`02_historical_fairy_tale_adaptation`)

## 1. Mục đích của Ngăn 02
Ngăn 02 đóng vai trò là **Bộ lọc Chuyển thể Văn học, Sư phạm & Sử học (Literary & Pedagogical Adaptation Layer)** nằm giữa tư liệu thô của tiểu thuyết *Trưng Nữ Vương* (Ngăn 01) và Kịch bản phân cảnh từng trang (Ngăn 03).

Tại sao các AI Agent bắt buộc phải đi qua Ngăn 02?
- Văn bản gốc trong `TRƯNG NỮ VƯƠNG.pdf` là tiểu thuyết lịch sử chương hồi dài 58 trang với nhiều đoạn nghị luận chính trị, tên chức quan Hán – Việt đan xen và những cảnh giao chiến khốc liệt.
- Trong khi đó, sản phẩm đầu ra của chúng ta là **Bộ Truyện Cổ tích Lịch sử Hào hùng khổ 19×24 cm dành cho học sinh từ Lớp 8 đến Lớp 10 (13–16 tuổi)**, học theo cấu trúc kể chuyện súc tích, giàu tính biểu tượng của bộ mẫu *Truyền thuyết An Dương Vương*.
- Do đó, Ngăn 02 thiết lập bộ quy tắc ngôn ngữ, nhịp điệu, tâm lý lứa tuổi và hồ sơ thiết kế nhân vật (Character Bible) để mọi Agent viết lời dẫn và vẽ tranh đều đồng bộ 100%.

## 2. Danh mục Tài liệu trong Ngăn 02 & Hướng dẫn Thực thi

| Tên File Markdown | Nội dung Trọng tâm | Agent Nào Cần Đọc & Thực thi? | Hướng dẫn Áp dụng Cụ thể |
| :--- | :--- | :--- | :--- |
| `GRADE_8_10_TONE_AND_STYLE_GUIDE.md` | Quy chuẩn giọng văn **Cổ tích Lịch sử Hào hùng** cho học sinh lớp 8–10: Công thức pha trộn chất Huyền sử (Cổ tích) + Chính sử (Hào hùng), quy tắc cô đọng văn bản từ 58 trang PDF xuống 28 trang truyện, quy tắc chọn từ khóa tô đỏ và cách xử lý cảnh bi tráng. | `AGENT-03` (Biên kịch), `AGENT-04` (Mỹ thuật), `AGENT-06` (Kiểm định) | Áp dụng trực tiếp khi viết lời dẫn trong Khung giấy cổ (Narration Box) và Bóng thoại (Speech Bubbles). Tuyệt đối tuân thủ giới hạn 35–65 từ/khung dẫn và bảng từ vựng sử thi. |
| `CHARACTER_BIBLE_AND_FACTIONS.md` | Hồ sơ chi tiết về **20+ nhân vật & bộ tộc** xuất hiện trong Hồi 7 & Hồi 8: Vai trò lịch sử, tính cách, ngoại hình, trang phục, vũ khí biểu tượng, bảng màu nhận diện và mối quan hệ. | `AGENT-03` (Biên kịch), `AGENT-04` (Prompt/Concept Art), `AGENT-05` (Dàn trang) | Dùng để giữ tính nhất quán tuyệt đối (Consistency) về trang phục, vũ khí, tuổi tác và xưng hô của nhân vật từ trang đầu đến trang cuối. |

## 3. Quy trình 3 Bước Dành cho AI Agent Khi Làm việc tại Ngăn 02
1. **Bước 1:** Đọc `GRADE_8_10_TONE_AND_STYLE_GUIDE.md` để nắm vững công thức viết câu dẫn truyện 3 nhịp (*Bối cảnh/Biến cố -> Hành động anh hùng -> Ý nghĩa/Khí phách dân tộc*) và quy tắc tô đỏ từ khóa.
2. **Bước 2:** Tra cứu `CHARACTER_BIBLE_AND_FACTIONS.md` trước khi viết bất kỳ câu thoại hay mô tả ngoại hình nhân vật nào để đảm bảo đúng trang phục (ví dụ: Thi Sách mặc trường bào gấm tía đính hổ phù của Lạc Hầu khi tử chiến; Trưng Trắc và Thánh Thiên mặc giáp chiến kết hợp khăn tang trắng khi phất cờ báo thù).
3. **Bước 3:** Chuyển sang Ngăn 03 (`03_storyboards_and_scripts/`) để triển khai kịch bản từng trang.
