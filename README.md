# DỰ ÁN TRUYỆN CỔ TÍCH LỊCH SỬ HÀO HÙNG: TRƯNG NỮ VƯƠNG (KHỔ 19x24 CM)

> **Bộ thiết kế tổng thể hiện hành:** mở [Ngăn09 — Xem và dùng thiết kế](09_design_system/00_READ_FIRST.md) hoặc [Album hình](09_design_system/IMAGE_CATALOG.md). Bao gồm41 hồ sơ nhân vật,14 bối cảnh,36 nhóm đạo cụ,4 động vật, quy chuẩn layout và hướng dẫn cho agent; tiến độ ảnh thực tế ghi trong album.
> **Hệ thống Kho lưu trữ & Điều phối Đa Tác Tử (Multi-Agent GitHub Repository)**
> **Chủ đề:** Chuyển thể Hồi thứ Bảy & Hồi thứ Tám tiểu thuyết lịch sử *Trưng Nữ Vương* (nhà văn Phùng Văn Khai) thành bộ truyện tranh cổ tích lịch sử hào hùng theo chuẩn bố cục mẫu *Truyền thuyết An Dương Vương*.
> **Đối tượng độc giả mục tiêu:** Học sinh THCS & THPT từ Lớp 8 đến Lớp 10 (13 – 16 tuổi).
> **Khổ sách tiêu chuẩn xuất bản:** **19cm × 24cm** (Khổ thành phẩm: `190mm × 240mm` | Khổ tràn lề Bleed: `196mm × 246mm` | Độ phân giải: `300 DPI`).

## 1. Bối cảnh & Mục tiêu Tối thượng của Dự án

Dự án này xây dựng một bộ sách truyện cổ tích lịch sử minh họa chất lượng xuất bản chuyên nghiệp, kế thừa:
1. **Nội dung cốt lõi từ tài liệu gốc `TRƯNG NỮ VƯƠNG.pdf` (58 trang scan, tương ứng trang sách 212–269):** Bao gồm trọn vẹn **Hồi thứ Bảy** (*Tiên phát chế nhân, Tô Thái thú giết hại Thi Sách / Quyết giương cờ nghĩa, Trưng phu nhân nổi trận lôi đình*) và **Hồi thứ Tám** (*Đắp đàn hội tướng, cửa Hát Môn dậy sóng Nhị Hà / Chia binh mật phục, núi Phượng Hoàng trảm thủ Tào Quyền*). Đặc biệt, bản PDF gốc đã có các dấu **ngoặc vuông `[ ... ]` và đường gạch chân bằng bút** do người biên tập đánh dấu sẵn những trường đoạn kịch tính nhất cần đưa vào truyện.
2. **Bố cục thiết kế & ngôn ngữ thị giác từ 22 file ảnh `.jpg` mẫu (*Truyền thuyết An Dương Vương - Chiếc nỏ thần, thành Cổ Loa và mối tình bi kịch của Mỵ Châu - Trọng Thủy*):** Học hỏi triệt để cách thiết kế Bìa sách đa tầng, cách đặt Khung dẫn truyện giấy cổ (Narration Scroll Box) ở đầu trang với các **từ khóa tô đỏ (`#C81E1E`)** nhấn mạnh cảm xúc, cách chia khung truyện (Splash Page toàn trang, Split 2 khung ngang/chéo, Multi-panel 3 khung kèm bóng thoại và khung zoom tròn), cùng nét vẽ mực đen tỉa nét kết hợp tô màu cổ điển giàu chiều sâu.
3. **Định hướng thẩm mỹ & giáo dục cho học sinh Lớp 8 – Lớp 10:** Mang âm hưởng **cổ tích lịch sử hào hùng, tự hào dân tộc**, kết hợp nhuần nhuyễn yếu tố huyền sử linh thiêng (giấc mộng đôi khổng tước đầu thai của dòng họ Phùng, Thánh Đóng & Tản Viên Sơn Thánh thời Hùng Duệ Vương, khói hương quyện linh khí Hùng Vương tại đàn thề Hát Môn) với khí phách bi tráng của cuộc khởi nghĩa Hai Bà Trưng mùa xuân năm 40 SCN.

## 2. Sơ đồ Kiến trúc 7 Ngăn (Compartment Architecture)

Kho lưu trữ được chia thành **7 ngăn độc lập nhưng liên thông chặt chẽ**, mỗi ngăn đều có file `README.md` riêng đóng vai trò là **Bản Giao việc & Hướng dẫn Sử dụng (Standard Operating Procedure - SOP)** cho bất kỳ AI Agent hoặc thành viên nào truy cập:

| Thứ tự | Tên Ngăn (Thư mục) | Vai trò Chức năng | Agent Chịu trách nhiệm Chính |
| :--- | :--- | :--- | :--- |
| **Gốc** | `/` (Root Directory) | Điều phối tổng thể, giao thức Multi-Agent, thông số kỹ thuật khổ sách 19×24cm. | `Orchestrator / Lead Agent` |
| **Ngăn 01** | `01_source_material_analysis/` | Phân tích toàn diện 58 trang PDF (bao gồm toàn bộ các dấu ngoặc `[...]` & gạch chân) và mổ xẻ bố cục 22 ảnh JPG mẫu. | `Agent 01: Archivist & Visual Analyst` |
| **Ngăn 02** | `02_historical_fairy_tale_adaptation/` | Quy chuẩn chuyển thể văn học cho lứa tuổi lớp 8–10, xử lý chất cổ tích hào hùng, và Hồ sơ Nhân vật (Character Bible). | `Agent 02: Literary Adapter & Historian` |
| **Ngăn 03** | `03_storyboards_and_scripts/` | Kịch bản phân cảnh chi tiết từng trang (28 trang ruột + Bìa) cho Hồi 7 & Hồi 8: lời dẫn, từ khóa tô đỏ, thoại, mô tả khung hình. | `Agent 03: Storyboard & Scriptwriter` |
| **Ngăn 04** | `04_art_direction_and_image_prompts/` | Style Guide mỹ thuật, Prompt tạo Character Sheets đồng nhất, và bộ Prompt tạo ảnh Bìa + 28 trang ruột. | `Agent 04: Concept & Prompt Engineer` |
| **Ngăn 05** | `05_book_design_and_layout_19x24/` | Thiết kế kỹ thuật Bìa sách (Trước, Gáy, Sau), lưới dàn trang 19×24cm, quy chuẩn Typography và mã hóa tự động dàn trang. | `Agent 05: Book Designer & Typesetter` |
| **Ngăn 06** | `06_qa_validation_and_delivery/` | Bảng kiểm chất lượng 3 lớp (Sử học - Mỹ thuật - Chế bản 300 DPI) và giao thức làm việc nhóm trên GitHub. | `Agent 06: QA & Print Inspector` |
| **Ngăn 07** | `07_reference_assets/` | Kho lưu trữ 22 ảnh `.jpg` mẫu đã sắp xếp đúng thứ tự trang (`00` -> `21`) và 10 bảng tổng hợp (Contact Sheets) 58 trang PDF. | `All Agents (Read-Only Reference)` |

## 3. Hướng dẫn Đọc Nhanh cho AI Agent Khi Mới Truy cập Repo (Quick-Start Protocol)

Bất kỳ AI Agent nào khi được khởi chạy trên kho lưu trữ này **BẮT BUỘC** thực hiện theo thứ tự 4 bước sau trước khi sinh nội dung hoặc viết code:

1. **Bước 1 — Đọc Điều phối & Thông số Kỹ thuật (Tại thư mục gốc):**
   - Đọc `AGENT_ORCHESTRATION_GUIDE.md` để xác định vai trò của mình trong chuỗi 6 Agent, hiểu định dạng đầu vào/đầu ra và lộ trình 6 giai đoạn sản xuất.
   - Đọc `PROJECT_SPECS_19x24.md` để khóa cứng các thông số khổ sách `190mm × 240mm`, vùng tràn lề `3mm`, vùng an toàn `12mm–15mm` và tỷ lệ khung hình.
2. **Bước 2 — Nạp Tri thức Nguồn & Mẫu Thiết kế (Tại Ngăn 01 & Ngăn 07):**
   - Đọc `01_source_material_analysis/PDF_CONTENT_DEEP_ANALYSIS.md` và `01_source_material_analysis/PDF_PAGE_BY_PAGE_ANNOTATIONS.md` để nắm toàn bộ cốt truyện 58 trang PDF cùng những đoạn được đánh dấu `[ ... ]`.
   - Đọc `01_source_material_analysis/JPG_SAMPLE_LAYOUT_DECONSTRUCTION.md` kết hợp xem ảnh thực tế trong `07_reference_assets/sample_an_duong_vuong_sorted/` để hiểu cách mẫu *An Dương Vương* bố trí khung chữ, tô đỏ từ khóa và chia khung tranh.
3. **Bước 3 — Đi tới Ngăn Chuyên môn được Giao:**
   - Mở file `README.md` nằm ngay trong ngăn nhiệm vụ của mình (`02_...` đến `06_...`) và tuân thủ tuyệt đối hướng dẫn sử dụng của ngăn đó.
4. **Bước 4 — Tự Kiểm định Trước khi Bàn giao (Tại Ngăn 06):**
   - Đối chiếu kết quả đầu ra với `06_qa_validation_and_delivery/QA_CHECKLIST_HISTORICAL_ART_PRINT.md` trước khi tạo Pull Request hoặc đóng gói thành phẩm.

## 4. Hồ sơ tiếp quản và tiến độ ngày 09/11/2026

Đã kiểm kê và đọc đủ **59 file gốc** (26 Markdown, 32 JPG, 1 `.gitignore`) tại commit `65c2e5a7cf71a1344be7f916c9b675e4325d31c8`. Các tài liệu bổ sung làm tăng tổng số file; số 59 chỉ áp dụng cho commit nền.

- [Báo cáo sẵn sàng dự án](06_qa_validation_and_delivery/PROJECT_READINESS_REPORT.md).
- [Kiểm kê nguồn và SHA-256](06_qa_validation_and_delivery/SOURCE_INVENTORY_BASELINE.md).
- [Kết quả kiểm tra onboarding](06_qa_validation_and_delivery/ONBOARDING_AUDIT_2026-11-09.md).
- [Vấn đề cần giải quyết trước sản xuất](06_qa_validation_and_delivery/ONBOARDING_ISSUES.md).
- [Form đầu ra tổng hợp](05_book_design_and_layout_19x24/STANDARD_OUTPUT_CONTRACT.md).
- [Ngăn 08: Nhật ký, quyết định và kinh nghiệm](08_project_memory/README.md).

**Trạng thái cập nhật:** bộ thiết kế v1 đã có30 bảng hình,41 hồ sơ nhân vật,24 mặt tộc trưởng tập thể,14 bối cảnh,36 nhóm đạo cụ và4 động vật. [Xem album](09_design_system/IMAGE_CATALOG.md). Đây là chuẩn thiết kế để làm bản nháp; chưa coi là28 trang truyện hoặc sách sẵn in.
