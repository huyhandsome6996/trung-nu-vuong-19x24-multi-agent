# PAGE21_QA — Trang21: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE21_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 21

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 65; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 21 — SA BÀN ĐẤT DẺO & MƯU KẾ "DỤ HỔ VÀO KHE MÃNG XÀ"
- **Nguồn PDF:** Trang 47–49 (Trang sách 258–260).
- **Loại Bố Cục:** `Template C (1 khung lớn Thánh Thiên chỉ huy trước sa bàn đất dẻo + 2 khung nhỏ lão Bạch Kẻ Từ và hai tướng thủy quân họ Khúc, họ Hoàng)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 55 từ):**
  > Biết tin **Đại tổng quản Tào Quyền** cùng tên Việt gian **Lục Hiến** đang dẫn **ba mươi chiến thuyền** và **sáu trăm quân tinh nhuệ** tiến vào bến **Lục Đầu Giang**, **Thánh Thiên** lập tức cho đắp **sa bàn đất dẻo** mô tả địa thế núi rừng. Nàng bày kế **giả thua nhử địch vào khe Mãng Xà** để bắt gọn toàn bộ quân thù!
- **Bóng Thoại (Speech Bubble):**
  - *Thánh Thiên (chỉ kiếm vào sa bàn):* "Ta sẽ đích thân dẫn dụ Tào Quyền vào khe Mãng Xà giữa lưng chừng núi, đồng thời đánh chiếm toàn bộ ba mươi chiến thuyền của chúng dưới bến sông!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung chính:* Trong nhà gỗ lớn, **Thánh Thiên** mặc giáp ngắn gọn gàng, tay cầm que chỉ vào chiếc **sa bàn đắp đất dẻo** thể hiện rõ dãy núi Phượng Hoàng, khe Mãng Xà và ngã ba sông Lục Đầu Giang.
  - *2 Khung dưới:* Lão chủ phường săn họ Bạch đất Kẻ Từ và hai vị đô tướng trẻ họ Khúc, họ Hoàng chắp tay nhận lệnh mai phục.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR04](../../../assets_generated/design_system/CHAR04_v001.png): `assets_generated/design_system/CHAR04_v001.png`
- [CHAR15](../../../assets_generated/design_system/CHAR15_v001.png): `assets_generated/design_system/CHAR15_v001.png`
- [ENV04](../../../assets_generated/design_system/ENV04_v001.png): `assets_generated/design_system/ENV04_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
- [PROP03](../../../assets_generated/design_system/PROP03_v002.png): `assets_generated/design_system/PROP03_v002.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại `10_agent_workflow/parallel/agent_b/production_state.json`. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- historical: kiểm thật và ghi pass khi có bằng chứng.
- art: kiểm thật và ghi pass khi có bằng chứng.
- language: kiểm thật và ghi pass khi có bằng chứng.
- print_geometry: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
