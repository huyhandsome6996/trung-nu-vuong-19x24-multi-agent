# PAGE25_ART — Trang25: tạo và kiểm tranh nền

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `art`. Trạng thái: `todo`. Phụ thuộc: PAGE25_TEXT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Lấy text đã khóa từ evidence bước TEXT. Xem các sheet liên quan; soạn prompt cuối theo cảnh, ghi actual_references và hash. Tạo ảnh bằng công cụ sinh ảnh, nền không chữ, không bóng thoại, chừa20% đỉnh; dùng đúng A/B/C. Kiểm mặt, phục trang, tay/chân/vũ khí và hành động. Lưu PNG native có phiên bản và metadata theo templates/RAW_IMAGE_METADATA.json. Không resize rồi khai native300DPI.

## Trang 25

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 66; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 25 — BAO VÂY TÀO QUYỀN & TRỪNG TRỊ VIỆT GIAN LỤC HIẾN
- **Nguồn PDF:** Trang 54–56 (Trang sách 265–267).
- **Loại Bố Cục:** `Template B (Khung trên hơn 300 nghĩa quân đeo nỏ ngắn vây chặt nhà gỗ - Khung dưới tướng trẻ nghĩa quân mắng thẳng mặt tên phản bội Lục Hiến)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 54 từ):**
  > Đứng chờ dưới chân núi mà không thấy một tên lính nào quay về, **Tào Quyền** và **Lục Hiến** kinh hoàng nhận ra mình đã **trúng kế điệu hổ ly sơn**. Chưa kịp tháo chạy, hơn **ba trăm tráng đinh** mang **nỏ ngắn và quắc mã tấu** đã vây chặt bốn phía, còn **Nữ tướng Thánh Thiên** cưỡi ngựa dẫn đại quân chiến thắng kéo xuống!
- **Bóng Thoại (Speech Bubble):**
  - *Đô tướng nghĩa quân (chỉ mặt Lục Hiến):* "Lục Hiến! Ngươi ăn lộc đất Nam mà dẫn giặc về hại Thần y và đồng bào, còn mặt mũi nào nhìn hương thân phụ lão đất Phượng Hoàng!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Hơn 300 nghĩa quân sơn cước tay cầm đao kiếm, quắc mã tấu, lưng đeo nỏ ngắn vây kín sân nhà gỗ; Tào Quyền và Lục Hiến mặt cắt không còn giọt máu.
  - *Khung dưới:* Tiếng trống khải hoàn vang dội, **Thánh Thiên** ngồi vững trên lưng chiến mã dẫn hàng ngàn nghĩa quân từ đường núi Phượng Hoàng tiến xuống trong nắng vàng rực rỡ.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR04](../../../assets_generated/design_system/CHAR04_v001.png): `assets_generated/design_system/CHAR04_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [CHAR11](../../../assets_generated/design_system/CHAR11_v001.png): `assets_generated/design_system/CHAR11_v001.png`
- [CHAR15](../../../assets_generated/design_system/CHAR15_v001.png): `assets_generated/design_system/CHAR15_v001.png`
- [ENV04](../../../assets_generated/design_system/ENV04_v001.png): `assets_generated/design_system/ENV04_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
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
