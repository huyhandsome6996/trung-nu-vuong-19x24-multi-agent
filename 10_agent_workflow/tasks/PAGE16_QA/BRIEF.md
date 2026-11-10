# PAGE16_QA — Trang16: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE16_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 16

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 71; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 16 — ĐẠI CẢNH ĐÀN THỀ HÁT MÔN BÊN DÒNG SÔNG NHỊ HÀ
- **Nguồn PDF:** Trang 39–40 (Trang sách 250–251).
- **Loại Bố Cục:** `Template A (Full-Page Grand Panorama Splash: Toàn cảnh Đàn thề Hát Môn uy nghiêm bên ngã ba sông)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 58 từ):**
  > Buổi sáng mùa xuân năm 40, tại bãi bồi mênh mông nơi **cửa sông Hát Môn** giao hòa cùng **sông Nhị Hà**, một **đàn tế cao hơn hai trượng** được dựng lên uy nghiêm. Xung quanh kỳ đài là **chín mươi chín lá cờ ngũ sắc**, **tám thớt voi đực da xám, ngà trắng**, hàng ngàn kỵ binh, cung thủ và **một trăm sáu mươi chiến thuyền** rợp bóng cờ đào.
- **Bóng Thoại (Speech Bubble):** Không có (dành trọn không gian cho đại cảnh lịch sử hào hùng).
- **Mô tả Khung hình (Visual Composition):**
  - Đại cảnh toàn trang hoành tráng bậc nhất cuốn sách: Chính giữa bãi bồi ngã ba sông Hát Giang – Nhị Hà là Đàn thề Hát Môn 3 tầng cao vợi, 99 lá cờ ngũ sắc tung bay, 8 tầng tháp trống đồng lấp lánh dưới nắng xuân. Bên tả là 500 kỵ mã chiến giáp của Đào Chiêu Hiển và 8 thớt voi chiến ngà trắng; bên hữu là 2.000 cung thủ của Bạch Uy; dưới mặt sông Nhị Hà là 160 khinh thuyền của Đô đốc Lê Đạo xếp đội hình chỉnh tề.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR08](../../../assets_generated/design_system/CHAR08_v001.png): `assets_generated/design_system/CHAR08_v001.png`
- [CHAR15](../../../assets_generated/design_system/CHAR15_v001.png): `assets_generated/design_system/CHAR15_v001.png`
- [ENV03](../../../assets_generated/design_system/ENV03_v001.png): `assets_generated/design_system/ENV03_v001.png`
- [PROP02](../../../assets_generated/design_system/PROP02_v001.png): `assets_generated/design_system/PROP02_v001.png`
- [PROP04](../../../assets_generated/design_system/PROP04_v002.png): `assets_generated/design_system/PROP04_v002.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại `10_agent_workflow/parallel/agent_a/production_state.json`. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- historical: kiểm thật và ghi pass khi có bằng chứng.
- art: kiểm thật và ghi pass khi có bằng chứng.
- language: kiểm thật và ghi pass khi có bằng chứng.
- print_geometry: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
