# PAGE01_TEXT — Trang01: đối chiếu và khóa chữ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `text`. Trạng thái: `todo`. Phụ thuộc: DESIGN_BASELINE.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Đọc nguyên cảnh và nguồn scan; sửa các câu cường điệu/không có căn cứ, giữ giọng hào hùng 13–16 tuổi. Đếm thật 35–65 tiếng theo khoảng trắng, không dùng số từ ghi trong tiêu đề làm chứng cứ. Chép đủ thoại vào text.v001.json, giữ **từ khóa**; ghi nguồn, template và hash storyboard. Khóa chữ sau khi kiểm. Nếu sửa toàn file storyboard về sau, rà lại các text đã khóa theo hash mới.

## Trang 01

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 58; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 01 — HUYỀN TÍCH VĂN LANG & GIẤC MỘNG ĐÔI KHỔNG TƯỚC VÀNG
- **Nguồn PDF:** Trang 06–07 (Trang sách 217–218).
- **Loại Bố Cục:** `Template B (Chia 2 khung ngang: Khung trên đại cảnh kinh đô Phong Châu - Khung dưới giấc mộng rồng vàng khổng tước)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 52 từ):**
  > Ngày xửa ngày xưa, từ thuở **vua Hùng dựng nước Văn Lang**, giang sơn gấm vóc trải hơn **hai ngàn tám trăm năm** bền vững. Vào đời **Hùng Duệ Vương**, tại đất Đông An có vợ chồng ông **Phùng Đặng** hiền đức, đêm xuân nằm mộng thấy **rồng vàng hóa đôi chim khổng tước** giáng thế đầu thai.
- **Bóng Thoại (Speech Bubble):** Không có.
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên (40%):* Đại cảnh núi sông Văn Lang hùng vĩ nơi ngã ba sông Bạch Hạc, kinh đô Phong Châu rực rỡ cờ hoa dưới bầu trời xanh.
  - *Khung dưới (40%):* Đêm trăng mùa xuân, vợ chồng ông Phùng Đặng – bà Lưu Thị Tuấn ngước nhìn bầu trời rực sáng hào quang đỏ vàng, nơi rồng vàng đang hóa thành đôi chim khổng tước lộng lẫy bay xuống mái nhà gỗ.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR12](../../../assets_generated/design_system/CHAR12_v001.png): `assets_generated/design_system/CHAR12_v001.png`
- [ENV01](../../../assets_generated/design_system/ENV01_v001.png): `assets_generated/design_system/ENV01_v001.png`
- [PROP03](../../../assets_generated/design_system/PROP03_v002.png): `assets_generated/design_system/PROP03_v002.png`
- [PROP04](../../../assets_generated/design_system/PROP04_v002.png): `assets_generated/design_system/PROP04_v002.png`
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
