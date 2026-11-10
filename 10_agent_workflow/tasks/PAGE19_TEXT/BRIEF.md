# PAGE19_TEXT — Trang19: đối chiếu và khóa chữ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `text`. Trạng thái: `todo`. Phụ thuộc: DESIGN_BASELINE.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Đọc nguyên cảnh và nguồn scan; sửa các câu cường điệu/không có căn cứ, giữ giọng hào hùng 13–16 tuổi. Đếm thật 35–65 tiếng theo khoảng trắng, không dùng số từ ghi trong tiêu đề làm chứng cứ. Chép đủ thoại vào text.v001.json, giữ **từ khóa**; ghi nguồn, template và hash storyboard. Khóa chữ sau khi kiểm. Nếu sửa toàn file storyboard về sau, rà lại các text đã khóa theo hash mới.

## Trang 19

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 69; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 19 — HUYỀN TÍCH 27 CỦ HUYẾT SÂM & NỮ TƯỚNG THÁNH THIÊN
- **Nguồn PDF:** Trang 42–43 (Trang sách 253–254).
- **Loại Bố Cục:** `Template B (Khung trên huyền tích vượt bão biển Đằng Giang tìm huyết sâm trên vách đá - Khung dưới thiếu nữ Thánh Thiên 17 tuổi văn võ toàn tài)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 56 từ):**
  > Hưởng ứng lời hịch ở Hát Môn, tại vùng **núi Phượng Hoàng** phía Đông có một nữ kiệt mười bảy tuổi tên là **Thánh Thiên**, con gái của **Thần y Nguyễn Huyền**. Tương truyền nàng chào đời trong cơn bão lớn ngoài **cửa biển Đằng Giang**, được nuôi dưỡng bằng **hai mươi bảy củ huyết sâm quý trên vách đá cheo leo**, nên sớm có **trí dũng hơn người**.
- **Bóng Thoại (Speech Bubble):** Không có.
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên (Màu sắc cổ tích huyền ảo):* Giữa sóng gió cửa biển Đằng Giang, người cha thần y Nguyễn Huyền leo trên vách đá dựng đứng hái những củ **huyết sâm tỏa ánh sáng đỏ hồng kỳ diệu**.
  - *Khung dưới:* Thiếu nữ **Thánh Thiên** 17 tuổi khỏe khoắn, cưỡi ngựa bắn cung điều khiển cả muông thú giữa núi rừng Phượng Hoàng và giúp cha bốc thuốc cứu dân lành.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR04](../../../assets_generated/design_system/CHAR04_v001.png): `assets_generated/design_system/CHAR04_v001.png`
- [CHAR06](../../../assets_generated/design_system/CHAR06_v001.png): `assets_generated/design_system/CHAR06_v001.png`
- [ENV03](../../../assets_generated/design_system/ENV03_v001.png): `assets_generated/design_system/ENV03_v001.png`
- [PROP03](../../../assets_generated/design_system/PROP03_v002.png): `assets_generated/design_system/PROP03_v002.png`
- [PROP04](../../../assets_generated/design_system/PROP04_v002.png): `assets_generated/design_system/PROP04_v002.png`
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
