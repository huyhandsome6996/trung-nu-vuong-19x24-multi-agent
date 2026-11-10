# PAGE22_QA — Trang22: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE22_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 22

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 62; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 22 — ĐOÀN THUYỀN GIẶC HÁN ĐI VÀO SƯƠNG MÙ LỤC ĐẦU GIANG
- **Nguồn PDF:** Trang 46–47 & 50 (Trang sách 257–258 & 261).
- **Loại Bố Cục:** `Template A (Full-Page Atmospheric Splash: 30 khinh thuyền của Tào Quyền rẽ sương mù tiến vào bến Lục Đầu Giang)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 52 từ):**
  > Mờ sáng hôm ấy, sương mù giăng kín mặt sông **Lục Đầu Giang**. **Đại tổng quản Tào Quyền** cùng tên huyện lệnh phản bội **Lục Hiến** dẫn **ba mươi khinh thuyền** cập bến chân núi Phượng Hoàng. Ngạo mạn khinh thường nghĩa quân chỉ là đám dân sơn cước, Tào Quyền thúc **sáu trăm binh tướng** hùng hổ tiến sâu vào núi.
- **Bóng Thoại (Speech Bubble):**
  - *Tào Quyền (cười ngạo mạn trên mũi thuyền):* "Bọn dân sơn cước cùng con bé miệng còn hôi sữa kia làm sao cản nổi đại quân của bản tổng quản!"
- **Mô tả Khung hình (Visual Composition):**
  - Cảnh sông nước Lục Đầu Giang buổi bình minh sương mù bảng lảng: 30 chiếc chiến thuyền của quân Đông Hán cập bờ lau lách hoang vu; Tào Quyền mặc giáp đen – tím đứng ở mũi thuyền chỉ đao về phía dãy núi Phượng Hoàng sừng sững, trong khi trên các vách đá và lùm cây phía xa thấp thoáng bóng mắt quan sát của trinh sát nghĩa quân.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [CHAR11](../../../assets_generated/design_system/CHAR11_v001.png): `assets_generated/design_system/CHAR11_v001.png`
- [ENV04](../../../assets_generated/design_system/ENV04_v001.png): `assets_generated/design_system/ENV04_v001.png`
- [PROP04](../../../assets_generated/design_system/PROP04_v002.png): `assets_generated/design_system/PROP04_v002.png`
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
