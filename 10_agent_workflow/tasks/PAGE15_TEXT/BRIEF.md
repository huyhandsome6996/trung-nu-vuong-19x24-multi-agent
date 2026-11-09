# PAGE15_TEXT — Trang15: đối chiếu và khóa chữ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `text`. Trạng thái: `todo`. Phụ thuộc: DESIGN_BASELINE.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Đọc nguyên cảnh và nguồn scan; sửa các câu cường điệu/không có căn cứ, giữ giọng hào hùng 13–16 tuổi. Đếm thật 35–65 tiếng theo khoảng trắng, không dùng số từ ghi trong tiêu đề làm chứng cứ. Chép đủ thoại vào text.v001.json, giữ **từ khóa**; ghi nguồn, template và hash storyboard. Khóa chữ sau khi kiểm. Nếu sửa toàn file storyboard về sau, rà lại các text đã khóa theo hash mới.

## Trang 15

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 63; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 15 — CƠN HOẢNG LOẠN CỦA TÔ ĐỊNH TẠI THÀNH LUY LÂU
- **Nguồn PDF:** Trang 35–38 (Trang sách 246–249).
- **Loại Bố Cục:** `Template B (Khung trên thành Luy Lâu đóng chặt cổng giữa bốn bề khói lửa - Khung dưới Tô Định và Tào Quyền bàn kế chia quân)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 55 từ):**
  > Chỉ trong mười ngày, ngọn lửa khởi nghĩa đã **bùng cháy khắp cõi Giao Chỉ**. Tiếng **trống đồng, tiếng chiêng và tiếng voi gầm** vang vọng ngày đêm khiến **Thái thú Tô Định** ăn ngủ không yên. Hoảng sợ trước tin **Trưng Trắc** lập đại bản doanh và **Thánh Thiên** tụ nghĩa ở núi Phượng Hoàng, giặc vội vã chia quân đàn áp.
- **Bóng Thoại (Speech Bubble):**
  - *Đại tổng quản Tào Quyền:* "Xin đại nhân cho hạ quan dẫn sáu trăm quân tinh nhuệ cùng Lục Hiến đi san phẳng núi Phượng Hoàng của con bé Thánh Thiên trước!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Bốn cổng thành Luy Lâu đóng chặt, phía xa chân trời bốn phía đều bốc lên những cột khói báo hiệu nghĩa quân Lạc Việt nổi dậy.
  - *Khung dưới:* Trong sảnh đường Luy Lâu, Tô Định mặt mày tái mét nghe Đại tổng quản Tào Quyền, Mã Tắc, Sầm Lân, Sầm Bá chỉ tay lên bản đồ chia đường thủy bộ tiến đánh.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [CHAR11](../../../assets_generated/design_system/CHAR11_v001.png): `assets_generated/design_system/CHAR11_v001.png`
- [CHAR14](../../../assets_generated/design_system/CHAR14_v001.png): `assets_generated/design_system/CHAR14_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP02](../../../assets_generated/design_system/PROP02_v001.png): `assets_generated/design_system/PROP02_v001.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại production_state.json. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- source_alignment: kiểm thật và ghi pass khi có bằng chứng.
- narration_35_65: kiểm thật và ghi pass khi có bằng chứng.
- keywords_preserved: kiểm thật và ghi pass khi có bằng chứng.
- dialogue_locked: kiểm thật và ghi pass khi có bằng chứng.
- template_locked: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
