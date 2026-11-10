# PAGE13_QA — Trang13: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE13_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 13

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 59; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 13 — TRƯNG PHU NHÂN KHOÁC TANG BÀO TRẮNG ĐỨNG LÊN PHẤT CỜ
- **Nguồn PDF:** Trang 32–33 (Trang sách 243–244).
- **Loại Bố Cục:** `Template A (Full-Page Splash: Hình ảnh kinh điển Trưng Trắc khoác trang phục trắng, vấn khăn tang trắng đứng giữa đại sảnh)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 56 từ):**
  > Giữa đại sảnh trang nghiêm, **Trưng Trắc** bước ra trong **bộ trang phục trắng muốt**, đầu vấn **chiếc khăn tang trắng** khiến ai nhìn thấy cũng nghẹn ngào. Nhưng nàng **không rơi thêm một giọt nước mắt**, mà cất giọng đanh thép tuyên bố cùng **mười bảy vị tộc trưởng Mê Linh** quyết đứng lên giành lại giang sơn!
- **Bóng Thoại (Speech Bubble):**
  - *Trưng Trắc:* "Cây muốn lặng mà gió chẳng dừng! Đất Mê Linh, Chu Diên này là cơ nghiệp ngàn năm của dòng giống Hồng Bàng, Hùng Vương!"
- **Mô tả Khung hình (Visual Composition):**
  - Toàn trang tập trung vào thần thái xuất thần của **Trưng Trắc**: Nàng đứng trên bục gỗ cao giữa nhà lớn Cổ Lôi sơn trang, mặc bộ chiến bào trắng tinh khôi, đầu vấn khăn tang trắng bay nhẹ, gương mặt đẹp uy nghiêm không một giọt lệ, bàn tay phải giơ cao nắm chặt thanh kiếm gia truyền. Phía dưới, hai vị sư phụ Đô Năng Tế – Cẩm Nương, Trưng Nhị và 17 vị tộc trưởng Mê Linh râu tóc dựng ngược vì xúc động.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR02](../../../assets_generated/design_system/CHAR02_v001.png): `assets_generated/design_system/CHAR02_v001.png`
- [CHAR07](../../../assets_generated/design_system/CHAR07_v001.png): `assets_generated/design_system/CHAR07_v001.png`
- [ENV03](../../../assets_generated/design_system/ENV03_v001.png): `assets_generated/design_system/ENV03_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại `10_agent_workflow/production_state.json`. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- historical: kiểm thật và ghi pass khi có bằng chứng.
- art: kiểm thật và ghi pass khi có bằng chứng.
- language: kiểm thật và ghi pass khi có bằng chứng.
- print_geometry: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
