# PAGE23_TEXT — Trang23: đối chiếu và khóa chữ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `text`. Trạng thái: `todo`. Phụ thuộc: DESIGN_BASELINE.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Đọc nguyên cảnh và nguồn scan; sửa các câu cường điệu/không có căn cứ, giữ giọng hào hùng 13–16 tuổi. Đếm thật 35–65 tiếng theo khoảng trắng, không dùng số từ ghi trong tiêu đề làm chứng cứ. Chép đủ thoại vào text.v001.json, giữ **từ khóa**; ghi nguồn, template và hash storyboard. Khóa chữ sau khi kiểm. Nếu sửa toàn file storyboard về sau, rà lại các text đã khóa theo hash mới.

## Trang 23

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 65; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 23 — NỮ TƯỚNG THÁNH THIÊN XUẤT TRẬN NHỬ ĐỊCH
- **Nguồn PDF:** Trang 51–52 (Trang sách 262–263).
- **Loại Bố Cục:** `Template A (Full-Page Dynamic Action Splash: Thánh Thiên mở toang cánh cửa nhà gỗ, chỉ kiếm mắng thẳng mặt Tào Quyền)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 55 từ):**
  > Khi quân giặc tràn vào khoảng sân rộng trước khu nhà gỗ của vị thần y quá cố, cánh cửa chính bỗng mở toang! **Nữ động chủ Thánh Thiên** khoác **bộ giáp ngắn**, đầu **chít khăn tang trắng**, chân đi **giày da báo** oai phong lẫm liệt bước ra, rút kiếm **vạch mặt tội ác của Tào Quyền** rồi tung mình rút lên đường núi.
- **Bóng Thoại (Speech Bubble):**
  - *Thánh Thiên:* "Tào tặc! Ngươi vô cớ sát hại cha ta, hôm nay tự dẫn xác đến đây chính là ý trời! Có giỏi thì đuổi theo ta!"
- **Mô tả Khung hình (Visual Composition):**
  - Cận cảnh – Trung cảnh cực kỳ ấn tượng: Từ cánh cửa gỗ mở toang, thiếu nữ 17 tuổi **Thánh Thiên** trong bộ đoản giáp đồng – da thuộc, dải khăn tang trắng bay dài sau gáy, chân đi giày da báo, tay cầm trường kiếm sáng loáng chỉ thẳng vào mặt Tào Quyền đang cưỡi ngựa dưới sân.

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

- source_alignment: kiểm thật và ghi pass khi có bằng chứng.
- narration_35_65: kiểm thật và ghi pass khi có bằng chứng.
- keywords_preserved: kiểm thật và ghi pass khi có bằng chứng.
- dialogue_locked: kiểm thật và ghi pass khi có bằng chứng.
- template_locked: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
