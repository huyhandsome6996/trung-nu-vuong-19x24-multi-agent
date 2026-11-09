# GIAO THỨC ĐIỀU PHỐI ĐA TÁC TỬ (MULTI-AGENT ORCHESTRATION & WORKFLOW GUIDE)

Tài liệu này quy định kiến trúc vận hành của hệ thống AI Agents cùng làm việc trên GitHub để sản xuất hoàn chỉnh bộ truyện cổ tích lịch sử **TRƯNG NỮ VƯƠNG (Khổ 19×24 cm)** từ nguyên liệu gốc đến file PDF chế bản in ấn.

## 1. Sơ đồ Vai trò 6 Chuyên gia AI Agent (Agent Personas & Scopes)

Để tránh chồng chéo nhiệm vụ và đảm bảo chất lượng xuất bản cao nhất, dự án được phân công cho **6 vai trò Agent chuyên biệt**:

| Mã Agent | Tên Vai trò (Role) | Ngăn Đọc Chính (Input) | Ngăn Thực thi & Ghi (Output) | Nhiệm vụ Cốt lõi |
| :--- | :--- | :--- | :--- | :--- |
| **AGENT-01** | **Source Archivist & Visual Analyst** *(Phân tích Tư liệu & Giải phẫu Mẫu)* | `07_reference_assets/` + File PDF/JPG gốc | `01_source_material_analysis/` | Trích xuất văn bản 58 trang PDF, ghi nhận toàn bộ dấu ngoặc vuông `[...]` và gạch chân; phân tích giải phẫu 22 trang JPG mẫu *An Dương Vương*. |
| **AGENT-02** | **Historical & Literary Adapter** *(Chuyển thể Văn học & Cố vấn Sử học)* | `01_source_material_analysis/` | `02_historical_fairy_tale_adaptation/` | Định hình giọng văn cổ tích lịch sử hào hùng cho học sinh lớp 8–10; xây dựng Hồ sơ Nhân vật, Trang phục, Phe phái (Character & Faction Bible). |
| **AGENT-03** | **Storyboard & Script Architect** *(Biên kịch Phân cảnh Từng Trang)* | `01_.../` + `02_.../` | `03_storyboards_and_scripts/` | Chuyển hóa Hồi 7 & Hồi 8 thành kịch bản phân cảnh 28 trang ruột + Bìa; viết lời dẫn (30–65 từ/trang), đánh dấu từ khóa tô đỏ, viết lời thoại và mô tả góc máy. |
| **AGENT-04** | **Art Director & Prompt Engineer** *(Chỉ đạo Mỹ thuật & Kỹ sư Prompt AI)* | `02_.../` + `03_.../` + `07_.../` | `04_art_direction_and_image_prompts/` | Thiết lập Style Guide nét vẽ mực đen + màu cổ điển; viết Prompt tạo Character Sheets khóa nhân vật và bộ Prompt chi tiết cho Bìa + 28 trang truyện. |
| **AGENT-05** | **Book Designer & Layout Engineer** *(Thiết kế Sách & Chế bản 19×24 cm)* | `03_.../` + `04_.../` + `PROJECT_SPECS_19x24.md` | `05_book_design_and_layout_19x24/` | Thiết kế Bìa Trước - Gáy - Bìa Sau khổ 19×24cm; lắp ghép tranh minh họa, vẽ khung dẫn truyện giấy cổ, tô đỏ từ khóa, đặt bóng thoại và xuất file in 300 DPI. |
| **AGENT-06** | **Quality Assurance & Print Auditor** *(Kiểm định Chất lượng & Xuất bản)* | Toàn bộ các ngăn `01` -> `05` | `06_qa_validation_and_delivery/` | Kiểm duyệt tính chính xác lịch sử, độ đồng nhất gương mặt/trang phục nhân vật, lỗi chính tả tiếng Việt, vùng tràn lề (bleed 3mm) và vùng an toàn (safe zone). |

## 2. Lộ trình 6 Bước Cụ thể để Tạo thành Bộ Truyện Cổ tích Lịch sử Hào hùng (End-to-End Production Pipeline)

Bất kỳ nhóm Agent nào tiếp nhận dự án này sẽ thực thi tuần tự hoặc song song có kiểm soát theo **6 giai đoạn chuẩn** dưới đây:

### Giai đoạn 1: Khai thác Tư liệu & Khóa Chuẩn Tham chiếu (Data Ingestion & Reference Locking)
- **Đầu vào:** File `TRƯNG NỮ VƯƠNG.pdf` (58 trang) và 22 ảnh `.jpg` mẫu trong `07_reference_assets/`.
- **Hành động:**
  1. Đối chiếu bản giải mã từng trang trong `01_source_material_analysis/PDF_PAGE_BY_PAGE_ANNOTATIONS.md` để nắm bắt mạch truyện Hồi 7 (Bi kịch thành Luy Lâu - Huyền sử họ Phùng - Trận tử chiến Chu Diên của Thi Sách - Đêm Cổ Lôi sơn trang) và Hồi 8 (Pháp trường Nguyễn Huyền & Trưng Định - Đàn thề Hát Môn của Hai Bà Trưng - Nữ tướng Thánh Thiên đại phá Tào Quyền tại núi Phượng Hoàng).
  2. Học thuộc 3 mẫu bố cục trang (Template A: Splash toàn trang, Template B: Chia 2 khung ngang/chéo, Template C: Chia 3 khung kèm Zoom tròn & bóng thoại) trong `01_source_material_analysis/JPG_SAMPLE_LAYOUT_DECONSTRUCTION.md`.
- **Tiêu chuẩn hoàn thành (Gate 1):** Mọi Agent nắm rõ câu chuyện Trưng Nữ Vương không được viết lan man mà phải bám sát các đoạn đã đánh dấu `[ ... ]` trong PDF gốc.

### Giai đoạn 2: Thiết lập Thế giới Truyện & Hồ sơ Nhân vật Chuẩn Lứa tuổi Lớp 8–10 (Worldbuilding & Character Locking)
- **Đầu vào:** Dữ liệu Ngăn 01.
- **Hành động:**
  1. Áp dụng `02_historical_fairy_tale_adaptation/GRADE_8_10_TONE_AND_STYLE_GUIDE.md` để chuyển hóa văn phong tiểu thuyết chương hồi sang văn phong **Truyện cổ tích lịch sử hào hùng**: câu văn cô đọng, giàu nhịp điệu sử thi, làm nổi bật các yếu tố huyền thoại (chim khổng tước vàng, Thánh Đóng - Tản Viên, bảo kiếm gia truyền Dương thị, giáp Lạc Hầu đính hổ phù, khói hương tụ khí thiêng Hùng Vương) và chuyển hóa các cảnh chiến trận đẫm máu thành hình ảnh bi tráng, oai hùng phù hợp tâm lý học sinh 13–16 tuổi.
  2. Khóa bảng thiết kế ngoại hình nhân vật trong `02_historical_fairy_tale_adaptation/CHARACTER_BIBLE_AND_FACTIONS.md` và `04_art_direction_and_image_prompts/CHARACTER_DESIGN_PROMPTS.md`.
- **Tiêu chuẩn hoàn thành (Gate 2):** Sinh xong bộ ảnh tham chiếu nhân vật gốc (Master Character Sheets) cho 10 nhân vật trọng tâm (Trưng Trắc, Trưng Nhị, Thi Sách, Thánh Thiên, Đô Năng Tế, Cẩm Nương, Đinh Lương, Phùng Thị Chính, Tô Định, Lữ Thạch/Tào Quyền) để dùng làm `image_references` xuyên suốt toàn bộ các trang sau.

### Giai đoạn 3: Chốt Kịch bản Phân cảnh & Lời dẫn Tô Đỏ Từng Trang (Storyboarding & Red-Keyword Scripting)
- **Đầu vào:** Ngăn 02 và Ngăn 03 (`BOOK_STRUCTURE_AND_PACING.md`).
- **Hành động:**
  1. Kiểm tra và tinh chỉnh kịch bản 28 trang truyện trong `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md` (Trang 01–14) và `STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md` (Trang 15–28).
  2. Đảm bảo mỗi trang chỉ có **1 Khung dẫn truyện (Narration Box)** ở đầu trang dài 3–5 dòng (35–65 chữ), trong đó các cụm từ mang sức nặng lịch sử hoặc cảm xúc cao trào được đánh dấu `**tô đỏ**` (`#C81E1E`) đúng theo tỷ lệ 20%–35% tổng số chữ của khung dẫn (học chính xác từ 22 ảnh mẫu *An Dương Vương*).
- **Tiêu chuẩn hoàn thành (Gate 3):** Kịch bản 28 trang + Bìa trước + Bìa sau hoàn tất 100% phần chữ (Text-Lock), không còn bất kỳ placeholder nào.

### Giai đoạn 4: Sinh Minh họa Mỹ thuật Đồng nhất Khổ 19×24 cm (Visual Asset Generation)
- **Đầu vào:** Bộ Prompt tại `04_art_direction_and_image_prompts/COVER_AND_PAGE_PROMPTS_LIBRARY.md` và Master Character Sheets.
- **Hành động:**
  1. `AGENT-04` gọi công cụ tạo ảnh theo tỷ lệ chuẩn gần nhất với khổ 19×24cm (`aspect_ratio: "3:4"` hoặc `"4:5"`, sau đó căn chỉnh vào khung `196mm × 246mm` có tràn lề 3mm ở `300 DPI` = `2315 × 2906 px`).
  2. **Quy tắc Bất di Bất dịch khi tạo ảnh nền:** Luôn tạo ảnh minh họa **KHÔNG CHỨA CHỮ (Clean, Text-Free Illustration)** nhưng **chừa sẵn vùng không gian thoáng (Negative Space / Sky / Ceiling / Upper Backdrop) chiếm 18%–22% ở phía trên cùng của bức tranh** để `AGENT-05` đặt Khung dẫn truyện giấy cổ (Narration Scroll Box) lên mà không che mất đầu hoặc khuôn mặt nhân vật!
  3. Truyền tham chiếu ảnh (`image_references`) của nhân vật đã khóa ở Giai đoạn 2 vào từng lần sinh trang mới để giữ nguyên gương mặt, mũ lông vũ, áo giáp và màu sắc trang phục.
- **Tiêu chuẩn hoàn thành (Gate 4):** Đủ bộ tranh gốc độ phân giải cao cho Bìa Trước, Bìa Sau và 28 trang ruột, đúng phong cách nét mực đen tỉa chi tiết kết hợp màu cổ điển hào hùng.

### Giai đoạn 5: Chế bản Dàn trang, Đóng Khung Giấy Cổ & Thiết kế Bìa 19×24 cm (Typesetting & Book Assembly)
- **Đầu vào:** Tranh minh họa từ Giai đoạn 4 + Text kịch bản từ Ngăn 03 + Thông số tại `05_book_design_and_layout_19x24/`.
- **Hành động:**
  1. Áp dụng `05_book_design_and_layout_19x24/COVER_DESIGN_SPEC_19x24.md` để dựng **Bìa Trước, Gáy Sách và Bìa Sau** khổ 19×24cm với hệ thống Typography 4 tầng (Tầng 1: Dòng tít phụ trên dải lụa vàng; Tầng 2: Đại tự **"TRƯNG NỮ VƯƠNG"** màu đỏ son viền vàng kim nổi khối; Tầng 3: Phụ đề trong khung mây cổ; Tầng 4: Tên chương/nhân vật chính).
  2. Áp dụng `PAGE_LAYOUT_TEMPLATES_19x24.md` và `CSS_AND_INDESIGN_AUTOMATION_SPEC.md` để ghép tranh vào trang `190mm × 240mm` (cộng `3mm` bleed), chồng lớp Khung dẫn truyện giấy cổ viền mực rách ở đỉnh trang, định dạng chữ tiếng Việt có dấu chuẩn xác (chữ thường màu đen than `#1A1A1A`, từ khóa in đậm màu đỏ son `#C81E1E`), và thêm bóng thoại trắng viền đen cho các trang thuộc Template B/C.
- **Tiêu chuẩn hoàn thành (Gate 5):** Xuất ra bộ file ảnh hoàn chỉnh từng trang (`.jpg`/`.png` 300 DPI) và file sách tổng hợp `TRUNG_NU_VUONG_19x24_PRINT_READY.pdf`.

### Giai đoạn 6: Kiểm định Chất lượng 3 Lớp & Nghiệm thu (3-Tier QA & Release)
- **Đầu vào:** File PDF và bộ ảnh trang hoàn chỉnh từ Giai đoạn 5.
- **Hành động:**
  1. `AGENT-06` chạy kiểm tra tự động và kiểm tra thị giác (Visual Critique) dựa trên `06_qa_validation_and_delivery/QA_CHECKLIST_HISTORICAL_ART_PRINT.md`.
  2. Nếu phát hiện lỗi (ví dụ: khung chữ đè vào mặt nhân vật, sai chính tả tiếng Việt, lệch kích thước 19×24cm, sai chi tiết lịch sử), trả về đúng Agent phụ trách để sửa (Re-render) trước khi đóng gói phát hành.

## 3. Quy ước Giao tiếp Giữa các Agent (Inter-Agent Handoff Format)

Khi một Agent tạo mới hoặc cập nhật một tài liệu hay tác phẩm trong bất kỳ ngăn nào, hãy gắn khối Metadata chuẩn YAML ở đầu file (hoặc trong file `.json` đi kèm ảnh) theo mẫu sau để các Agent tiếp theo đọc hiểu ngay lập tức:

```yaml
---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
book_size: "190mm x 240mm (Bleed: 196mm x 246mm @ 300 DPI)"
target_audience: "Học sinh Lớp 8 - Lớp 10 (13-16 tuổi)"
compartment: "03_storyboards_and_scripts"
agent_author: "AGENT-03 (Storyboard & Script Architect)"
status: "READY_FOR_PRODUCTION" # DRAFT | IN_REVIEW | READY_FOR_PRODUCTION | APPROVED
source_grounding: "TRƯNG NỮ VƯƠNG.pdf (Pages 1-58 / Book Pages 212-269) & 22 Sample JPGs"
---
```
