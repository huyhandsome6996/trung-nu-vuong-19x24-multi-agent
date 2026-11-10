# PAGE24_TEXT — Trang24: đối chiếu và khóa chữ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `text`. Trạng thái: `todo`. Phụ thuộc: DESIGN_BASELINE.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Đọc nguyên cảnh và nguồn scan; sửa các câu cường điệu/không có căn cứ, giữ giọng hào hùng 13–16 tuổi. Đếm thật 35–65 tiếng theo khoảng trắng, không dùng số từ ghi trong tiêu đề làm chứng cứ. Chép đủ thoại vào text.v001.json, giữ **từ khóa**; ghi nguồn, template và hash storyboard. Khóa chữ sau khi kiểm. Nếu sửa toàn file storyboard về sau, rà lại các text đã khóa theo hash mới.

## Trang 24

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 69; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 24 — THIÊN LA ĐỊA VÕNG TẠI KHE MÃNG XÀ & ĐOẠT CHIẾN THUYỀN
- **Nguồn PDF:** Trang 53–55 (Trang sách 264–266).
- **Loại Bố Cục:** `Template B (Khung trên phục kích cung nỏ tại khe Mãng Xà - Khung dưới nghĩa quân thủy chiến đánh chiếm 30 khinh thuyền ở bến Lục Đầu Giang)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 56 từ):**
  > Ham công bắt sống nữ tướng, **sáu trăm quân Hán** hò reo đuổi theo bóng áo giáp trắng lọt sâu vào **khe Mãng Xà** hiểm trở. Lập tức, tiếng trống trận nổ vang như sấm! Từ hai bên vách núi, **bốn đội phường săn đất Kẻ Từ** bắn tên nỏ xuống như mưa, trong khi dưới bến sông, **ba mươi chiến thuyền giặc** cũng bị nghĩa quân chiếm trọn!
- **Bóng Thoại (Speech Bubble):** Không có.
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Trong khe núi hẹp dựng đứng (khe Mãng Xà), hàng trăm tay cung nỏ ngắn của lão Bạch Kẻ Từ và 7 bộ tộc từ trên vách đá cao bắn xuống, lưới mây và gỗ đá chặn đứng hai đầu khe khiến quân Hán buông vũ khí xin hàng.
  - *Khung dưới:* Tại bến sông Lục Đầu Giang, hai vị đô tướng họ Khúc và họ Hoàng dẫn thủy quân Lạc Việt tràn lên chiếm gọn toàn bộ 30 chiếc khinh thuyền của Tào Quyền.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR04](../../../assets_generated/design_system/CHAR04_v001.png): `assets_generated/design_system/CHAR04_v001.png`
- [CHAR15](../../../assets_generated/design_system/CHAR15_v001.png): `assets_generated/design_system/CHAR15_v001.png`
- [ENV04](../../../assets_generated/design_system/ENV04_v001.png): `assets_generated/design_system/ENV04_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
- [PROP04](../../../assets_generated/design_system/PROP04_v002.png): `assets_generated/design_system/PROP04_v002.png`
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
