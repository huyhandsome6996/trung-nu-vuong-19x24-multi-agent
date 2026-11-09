# PAGE05_QA — Trang05: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE05_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 05

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 57; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 05 — CÁNH CHIM CÂU ĐƯA MẬT THƯ KHẨN CỦA TRƯNG TRẮC
- **Nguồn PDF:** Trang 12–13 (Trang sách 223–224).
- **Loại Bố Cục:** `Template C (Khung trên chim câu bay tới - Khung giữa Zoom bức thư trên lụa/giấy - Khung dưới Thi Sách ra lệnh khẩn)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 53 từ):**
  > Đúng lúc ấy, một cánh **chim câu đưa thư** từ hướng Mê Linh lao nhanh vào phủ. Mở bức mật thư còn tươi nét mực của phu nhân **Trưng Trắc**, **Thi Sách** bàng hoàng biết tin cha vợ là **Trưng Định** đã bị Tô Định bắt giam, và đại quân giặc đang **kéo thẳng xuống Chu Diên**!
- **Bóng Thoại (Speech Bubble / Khung thư trích dẫn):**
  - *Mật thư của Trưng Trắc:* "Tô Định đã bắt giữ cha thiếp tại Luy Lâu... Nay thiếp không thể nhịn nhục được nữa, thề không đội trời chung với giặc phương Bắc!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Con chim bồ câu trắng vỗ cánh đáp xuống tay Đinh Lương; Thi Sách biến sắc mặt khi đọc mảnh thư.
  - *Khung dưới:* Thi Sách dõng dạc hạ lệnh cho Phùng Thị Chính lập tức dẫn 27 thị vệ rút về Mê Linh bảo vệ Trưng Trắc và hội kiến hai vị sư phụ Đô Năng Tế – Cẩm Nương.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR03](../../../assets_generated/design_system/CHAR03_v001.png): `assets_generated/design_system/CHAR03_v001.png`
- [CHAR05](../../../assets_generated/design_system/CHAR05_v001.png): `assets_generated/design_system/CHAR05_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP02](../../../assets_generated/design_system/PROP02_v001.png): `assets_generated/design_system/PROP02_v001.png`
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
