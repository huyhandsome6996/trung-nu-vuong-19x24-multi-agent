# PAGE02_QA — Trang02: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE02_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 02

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 62; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 02 — THÁNH ĐÓNG KẾT NGHĨA TẢN VIÊN ĐẠI PHÁ QUÂN THỤC
- **Nguồn PDF:** Trang 07–10 (Trang sách 218–221).
- **Loại Bố Cục:** `Template B (Chia 2 khung chéo: Khung trên nâng đỉnh đồng - Khung dưới đại chiến thủy bộ cùng Tản Viên Sơn Thánh)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 56 từ):**
  > Cậu bé sinh ra được đặt tên là **Phùng Lực Công**, năm mười sáu tuổi đã có sức mạnh **nhấc bổng đỉnh đồng, bạt nghiêng sườn núi**, được dân gian tôn gọi là **Thánh Đóng**. Chàng kết nghĩa cùng **Tản Viên Sơn Thánh**, thống lĩnh quân Văn Lang **đánh tan quân xâm lược**, để lại dòng máu anh hùng cho hậu thế.
- **Bóng Thoại (Speech Bubble):** Không có.
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Trước lầu kén rể của vua Hùng Duệ Vương, chàng thiếu niên Phùng Lực Công (Thánh Đóng) 16 tuổi vạm vỡ hai tay nâng bổng chiếc đỉnh đồng khổng lồ trước sự kinh ngạc của Tản Viên Sơn Thánh và quần thần.
  - *Khung dưới:* Đại cảnh Tản Viên Sơn Thánh và Đại Lực tướng quân Phùng Lực Công cưỡi ngựa và chiến thuyền dẫn quân Văn Lang đánh tan đạo quân Thục bên bờ sông, tiếng trống đồng vang động.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR09](../../../assets_generated/design_system/CHAR09_v001.png): `assets_generated/design_system/CHAR09_v001.png`
- [CHAR12](../../../assets_generated/design_system/CHAR12_v001.png): `assets_generated/design_system/CHAR12_v001.png`
- [ENV01](../../../assets_generated/design_system/ENV01_v001.png): `assets_generated/design_system/ENV01_v001.png`
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
