# PAGE26_ART — Trang26: tạo và kiểm tranh nền

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `art`. Trạng thái: `todo`. Phụ thuộc: PAGE26_TEXT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Lấy text đã khóa từ evidence bước TEXT. Xem các sheet liên quan; soạn prompt cuối theo cảnh, ghi actual_references và hash. Tạo ảnh bằng công cụ sinh ảnh, nền không chữ, không bóng thoại, chừa20% đỉnh; dùng đúng A/B/C. Kiểm mặt, phục trang, tay/chân/vũ khí và hành động. Lưu PNG native có phiên bản và metadata theo templates/RAW_IMAGE_METADATA.json. Không resize rồi khai native300DPI.

## Trang 26

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 69; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 26 — THÁNH THIÊN ĐỘNG CHỦ TUYÊN ÁN TRẢM THỦ TÀO QUYỀN
- **Nguồn PDF:** Trang 57–58 (Trang sách 268–269).
- **Loại Bố Cục:** `Template A (Full-Page Climax Splash: Thánh Thiên rút trường kiếm tuyên án trước Tào Quyền và Lục Hiến bị trói dưới sân)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 52 từ):**
  > Giữa khoảng sân rộng dưới chân núi Phượng Hoàng, **Tào Quyền**, **Lục Hiến** và ba tướng giặc bị trói mỗi người một cọc vào **năm chiếc cọc gỗ** trước sự chứng kiến của hàng ngàn nghĩa sĩ. **Nữ động chủ Thánh Thiên** rút thanh trường kiếm sáng quắc chỉ thẳng vào tên đại gian ác, **hiên ngang tuyên tội** để tế hương hồn cha và các bậc liệt sĩ!
- **Bóng Thoại (Speech Bubble):**
  - *Thánh Thiên (uy phong lẫm liệt):* "Tào tặc! Ngươi vô cớ sát hại cha ta, tàn hại dòng giống Lạc Việt ta. Hôm nay ta thay mặt trời đất Giao Chỉ tuyên án: TRẢM THỦ!"
- **Mô tả Khung hình (Visual Composition):**
  - Đại cảnh oai hùng: Chính giữa sân, **Thánh Thiên** đứng hiên ngang với thanh trường kiếm chỉ thẳng về phía Tào Quyền và Lục Hiến đang bị trói vào cọc gỗ; xung quanh là 7 vị tộc trưởng núi Phượng Hoàng và 6 vị đô tướng giương cao cờ nghĩa.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR04](../../../assets_generated/design_system/CHAR04_v001.png): `assets_generated/design_system/CHAR04_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [CHAR11](../../../assets_generated/design_system/CHAR11_v001.png): `assets_generated/design_system/CHAR11_v001.png`
- [ENV04](../../../assets_generated/design_system/ENV04_v001.png): `assets_generated/design_system/ENV04_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
- [PROP03](../../../assets_generated/design_system/PROP03_v002.png): `assets_generated/design_system/PROP03_v002.png`
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
