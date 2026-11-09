# PAGE11_QA — Trang11: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE11_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 11

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 63; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 11 — KHÍ TIẾT BẤT KHUẤT TRÊN PHÁP TRƯỜNG LUY LÂU
- **Nguồn PDF:** Trang 26–29 (Trang sách 237–240).
- **Loại Bố Cục:** `Template A (Full-Page Splash: Hai bậc trưởng giả Nguyễn Huyền và Trưng Định cười lớn giữa pháp trường Luy Lâu lúc rạng đông)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 57 từ):**
  > Tờ mờ sáng tại cổng Bắc thành **Luy Lâu**, giặc Hán đem **Thần y Nguyễn Huyền** và **Huyện lệnh Trưng Định** ra pháp trường nhằm khuất phục lòng dân. Thế nhưng trước lưỡi đao bạo tàn, hai bậc trượng phu vẫn **ung dung bàn chuyện thiên mệnh đất Nam**, rồi **ngửa cổ cười vang** đón nhận cái chết để thức tỉnh muôn dân!
- **Bóng Thoại (Speech Bubble):**
  - *Trưng Định:* "Cái chết của ta và huynh hôm nay chính là hiệu lệnh báo ngày tàn của bọn giặc phương Bắc!"
  - *Nguyễn Huyền:* "Nếu có kiếp sau làm người Giao Chỉ, xin lại được kết nghĩa huynh đệ cùng Trưng huynh!"
- **Mô tả Khung hình (Visual Composition):**
  - Bố cục hất từ dưới lên: Trên đài gỗ cao trước cổng thành Luy Lâu mờ sương, hai vị trưởng giả râu tóc bạc trắng là Nguyễn Huyền và Trưng Định đứng thẳng người bên cột gỗ, gương mặt rạng ngời khí phách ngửa cổ cười sảng khoái; bên dưới là đám lính Hán cầm giáo đang run sợ trước uy thần của hai ông, còn trên bầu trời phương Nam một vệt nắng đỏ rực đang bừng lên.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR06](../../../assets_generated/design_system/CHAR06_v001.png): `assets_generated/design_system/CHAR06_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP03](../../../assets_generated/design_system/PROP03_v002.png): `assets_generated/design_system/PROP03_v002.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại production_state.json. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- historical: kiểm thật và ghi pass khi có bằng chứng.
- art: kiểm thật và ghi pass khi có bằng chứng.
- language: kiểm thật và ghi pass khi có bằng chứng.
- print_geometry: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
