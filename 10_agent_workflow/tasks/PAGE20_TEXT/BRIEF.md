# PAGE20_TEXT — Trang20: đối chiếu và khóa chữ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `text`. Trạng thái: `todo`. Phụ thuộc: DESIGN_BASELINE.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Đọc nguyên cảnh và nguồn scan; sửa các câu cường điệu/không có căn cứ, giữ giọng hào hùng 13–16 tuổi. Đếm thật 35–65 tiếng theo khoảng trắng, không dùng số từ ghi trong tiêu đề làm chứng cứ. Chép đủ thoại vào text.v001.json, giữ **từ khóa**; ghi nguồn, template và hash storyboard. Khóa chữ sau khi kiểm. Nếu sửa toàn file storyboard về sau, rà lại các text đã khóa theo hash mới.

## Trang 20

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 66; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 20 — BẢY BỘ TỘC NÚI PHƯỢNG HOÀNG TỤ NGHĨA BÁO THÙ
- **Nguồn PDF:** Trang 44–45 (Trang sách 255–256).
- **Loại Bố Cục:** `Template A (Full-Page Splash: Thánh Thiên đứng giữa 7 vị tộc trưởng núi Phượng Hoàng và hơn 4.000 nghĩa quân)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 54 từ):**
  > Khi tin **Thần y Nguyễn Huyền** bị giặc Hán sát hại ở Luy Lâu truyền về, **bảy bộ tộc lớn vùng núi Phượng Hoàng** đều vô cùng căm phẫn. Bởi sinh thời, vị thần y đã cứu sống biết bao người dân nơi đây. Hơn **bốn ngàn tráng đinh** lập tức tập hợp, đồng lòng suy tôn **Thánh Thiên làm Nữ động chủ** để báo thù!
- **Bóng Thoại (Speech Bubble):**
  - *Vị tộc trưởng họ Thân:* "Thần y Nguyễn Huyền có ơn tái tạo với bảy bộ tộc ta! Bảy tộc Nguyễn, Đinh, Thân, Thiệu, Thái, Bùi, Hoàng quyết theo Nữ động chủ đánh giặc đến cùng!"
- **Mô tả Khung hình (Visual Composition):**
  - Tại khoảng sân rộng trước căn nhà gỗ lớn dưới chân núi Phượng Hoàng, thiếu nữ Thánh Thiên đầu chít khăn tang trắng đứng trên thềm cao, trước mặt nàng là 7 vị tộc trưởng uy dũng của 7 họ lớn cùng hàng ngàn tráng đinh miền sơn cước giơ cao cung nỏ, giáo mác.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR04](../../../assets_generated/design_system/CHAR04_v001.png): `assets_generated/design_system/CHAR04_v001.png`
- [ENV04](../../../assets_generated/design_system/ENV04_v001.png): `assets_generated/design_system/ENV04_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại `10_agent_workflow/parallel/agent_a/production_state.json`. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- source_alignment: kiểm thật và ghi pass khi có bằng chứng.
- narration_35_65: kiểm thật và ghi pass khi có bằng chứng.
- keywords_preserved: kiểm thật và ghi pass khi có bằng chứng.
- dialogue_locked: kiểm thật và ghi pass khi có bằng chứng.
- template_locked: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
