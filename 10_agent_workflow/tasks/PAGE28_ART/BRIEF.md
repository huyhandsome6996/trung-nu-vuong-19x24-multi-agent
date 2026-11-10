# PAGE28_ART — Trang28: tạo và kiểm tranh nền

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `art`. Trạng thái: `todo`. Phụ thuộc: PAGE28_TEXT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Lấy text đã khóa từ evidence bước TEXT. Xem các sheet liên quan; soạn prompt cuối theo cảnh, ghi actual_references và hash. Tạo ảnh bằng công cụ sinh ảnh, nền không chữ, không bóng thoại, chừa20% đỉnh; dùng đúng A/B/C. Kiểm mặt, phục trang, tay/chân/vũ khí và hành động. Lưu PNG native có phiên bản và metadata theo templates/RAW_IMAGE_METADATA.json. Không resize rồi khai native300DPI.

## Trang 28

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 60; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 28 — TRƯNG NỮ VƯƠNG & BẢN ANH HÙNG CA MUÔN ĐỜI BẤT DIỆT (TRANG KẾT)
- **Nguồn bổ sung:** HIST01 hỗ trợ65huyện thành/xưng vương/Mê Linh; HERITAGE01–02 hỗ trợ truyền thống tưởng niệm; xem10_agent_workflow/tasks/SOURCE_EPILOGUE, truy cập09/11/2026.
- **Loại Bố Cục:** `Template A (Full-Page Monumental Finale Splash: Trưng Nữ Vương lên ngôi tại Mê Linh và lớp học sinh tưởng niệm trong montage biểu tượng)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 60 tiếng theo khoảng trắng):**
  > Giải phóng **sáu mươi lăm thành trì**, **Trưng Trắc** lên ngôi **Trưng Nữ Vương**, đóng đô tại **Mê Linh**. Gần **hai ngàn năm lịch sử** qua đi, người Việt vẫn nhớ **Hai Bà Trưng**. Trong truyện, **Thi Sách**, **Thánh Thiên** và lời thề ở **cửa Hát Môn** cùng nhắc chúng ta về lòng yêu nước và ý chí tự chủ.
- **Bóng Thoại (Speech Bubble):** Không có.
- **Mô tả Khung hình (Visual Composition):**
  - Bố cục 2 tầng hòa quyện giữa Lịch sử và Hiện tại (tương tự trang kết `JPG #01` của bộ mẫu *An Dương Vương*):
    - *Tầng trên:* Hình ảnh **Trưng Nữ Vương** uy nghiêm trong long bào Lạc Việt đứng trên đài cao kinh đô Mê Linh dưới ánh mặt trời rực rỡ và đàn chim Lạc vàng bay lượn.
    - *Tầng dưới:* Thế hệ học sinh hôm nay đọc sách và tưởng niệm tiền nhân trước một công trình biểu tượng E14 trong sắc xuân. Không ghi “Mê Linh–Hát Môn” như một ngôi đền duy nhất; E14 không đại diện bản sao di tích. Hai đền thật được phân biệt trong phụ lục.


> Đính chính thiết kế 09/11/2026: áp dụng đối chiếu scan và chuẩn nhận diện tại `09_design_system/SOURCE_DECISIONS.md`; xem hồ sơ v1 trước khi dùng prompt cũ.
- **Giới hạn hình ảnh:** Lễ đăng quang, chim Lạc và E14 là biểu tượng nghệ thuật; không gọi là phục dựng nghi lễ hoặc kiến trúc di tích thật.

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR02](../../../assets_generated/design_system/CHAR02_v001.png): `assets_generated/design_system/CHAR02_v001.png`
- [CHAR04](../../../assets_generated/design_system/CHAR04_v001.png): `assets_generated/design_system/CHAR04_v001.png`
- [ENV05](../../../assets_generated/design_system/ENV05_v001.png): `assets_generated/design_system/ENV05_v001.png`
- [PROP02](../../../assets_generated/design_system/PROP02_v001.png): `assets_generated/design_system/PROP02_v001.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại `10_agent_workflow/parallel/agent_b/production_state.json`. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- actual_refs: kiểm thật và ghi pass khi có bằng chứng.
- character_consistency: kiểm thật và ghi pass khi có bằng chứng.
- no_text: kiểm thật và ghi pass khi có bằng chứng.
- top_clearance: kiểm thật và ghi pass khi có bằng chứng.
- anatomy: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
