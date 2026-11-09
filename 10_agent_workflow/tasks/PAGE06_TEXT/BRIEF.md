# PAGE06_TEXT — Trang06: đối chiếu và khóa chữ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `text`. Trạng thái: `todo`. Phụ thuộc: DESIGN_BASELINE.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Đọc nguyên cảnh và nguồn scan; sửa các câu cường điệu/không có căn cứ, giữ giọng hào hùng 13–16 tuổi. Đếm thật 35–65 tiếng theo khoảng trắng, không dùng số từ ghi trong tiêu đề làm chứng cứ. Chép đủ thoại vào text.v001.json, giữ **từ khóa**; ghi nguồn, template và hash storyboard. Khóa chữ sau khi kiểm. Nếu sửa toàn file storyboard về sau, rà lại các text đã khóa theo hash mới.

## Trang 06

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 66; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 06 — THI SÁCH KHOÁC CHIẾN BÀO LẠC HẦU ĐÍNH HỔ PHÙ
- **Nguồn PDF:** Trang 14–16 (Trang sách 225–227).
- **Loại Bố Cục:** `Template A (Full-Page Heroic Splash: Thi Sách uy phong lẫm liệt giữa đại sảnh Chu Diên)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 56 từ):**
  > Chưa kịp rút quân, hơn **hai ngàn binh mã thủy bộ** của **Mã Tắc** và **Lữ Thạch** đã vây kín thủ phủ Chu Diên. Không chút nao núng, **Thi Sách** trút bỏ quan phục nhà Hán, khoác lên mình **bộ trường bào Lạc Hầu đính hổ phù** truyền từ đời **vua Hùng**, quyết làm **ngọn đuốc sống** thắp lửa căm thù cho toàn cõi Giao Chỉ!
- **Bóng Thoại (Speech Bubble):**
  - *Các vị tộc trưởng & tráng đinh Chu Diên (đồng thanh giơ cao vũ khí):* "Quyết không đội trời chung với quan quân phương Bắc!"
- **Mô tả Khung hình (Visual Composition):**
  - Đại cảnh toàn trang cực kỳ hào hùng: Ở trung tâm tiền cảnh, Thi Sách bước ra từ đại sảnh trong bộ **trường bào gấm tía đính Hổ phù vàng trước ngực**, đầu đội mũ Lạc Hầu gắn lông vũ, lưng đeo bộ cung tên gia bảo, hông đeo kiếm Dương thị, hai tay nắm chắc **ngọn trường thương bọc da hổ**. Xung quanh ngài là lão trượng họ Khúc, mạc khách họ Kiều và 7 vị tộc trưởng cùng hàng chục tráng đinh tuốt gươm giáo hô vang; phía xa ngoài cổng là khói lửa và cờ giặc Hán đen kịt.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR03](../../../assets_generated/design_system/CHAR03_v001.png): `assets_generated/design_system/CHAR03_v001.png`
- [CHAR16](../../../assets_generated/design_system/CHAR16_v001.png): `assets_generated/design_system/CHAR16_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
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
