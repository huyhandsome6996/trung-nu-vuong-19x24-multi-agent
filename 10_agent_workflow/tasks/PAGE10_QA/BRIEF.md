# PAGE10_QA — Trang10: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE10_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 10

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 65; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 10 — ĐÊM CỔ LÔI SƠN TRANG & NỖI ĐAU XÉ LÒNG CỦA TRƯNG TRẮC
- **Nguồn PDF:** Trang 24–25 (Trang sách 235–236).
- **Loại Bố Cục:** `Template B (Khung trên toàn cảnh căn cứ Cổ Lôi sơn trang trong đêm trăng - Khung dưới Trưng Trắc báo tin dữ trước Đô sư phụ)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 54 từ):**
  > Giữa đêm khuya tại căn cứ **Cổ Lôi sơn trang**, nơi mười bảy vị tộc trưởng đất **Mê Linh** cùng **ba mươi thớt voi chiến** và **mười bảy chiếc trống đồng** đang hội tụ, **Trưng Trắc** nghẹn ngào nhận tin dữ từ Chu Diên. Nỗi đau **cha bị cầm tù, chồng bị giết hại** hóa thành từng tia sấm sét trong mắt người nữ kiệt.
- **Bóng Thoại (Speech Bubble):**
  - *Trưng Trắc (nước mắt lăn dài nhưng ánh mắt rực lửa):* "Phụ thân bị bắt, phu quân vì nước hy sinh... Thù nhà nợ nước này, Trưng nhi thề quyết trả!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Toàn cảnh Cổ Lôi sơn trang ẩn giữa rừng núi ban đêm, đuốc thắp sáng rực quanh 17 chiếc trống đồng cổ và đàn voi chiến.
  - *Khung dưới:* Trong gian nhà gỗ thắp đèn nến, Trưng Trắc nắm chặt bức mật báo, đối diện là hai vị sư phụ Đô Năng Tế – Cẩm Nương và em gái Trưng Nhị đang siết chặt tay nàng.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR02](../../../assets_generated/design_system/CHAR02_v001.png): `assets_generated/design_system/CHAR02_v001.png`
- [CHAR07](../../../assets_generated/design_system/CHAR07_v001.png): `assets_generated/design_system/CHAR07_v001.png`
- [ENV03](../../../assets_generated/design_system/ENV03_v001.png): `assets_generated/design_system/ENV03_v001.png`
- [PROP02](../../../assets_generated/design_system/PROP02_v001.png): `assets_generated/design_system/PROP02_v001.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại production_state.json. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- historical: kiểm thật và ghi pass khi có bằng chứng.
- art: kiểm thật và ghi pass khi có bằng chứng.
- language: kiểm thật và ghi pass khi có bằng chứng.
- print_geometry: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
