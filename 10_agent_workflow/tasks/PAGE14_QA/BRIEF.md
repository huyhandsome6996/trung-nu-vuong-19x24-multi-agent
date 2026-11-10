# PAGE14_QA — Trang14: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE14_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 14

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 60; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 14 — TIẾNG HÔ SẤM DẬY NÚI RỪNG MÊ LINH (KẾT HỒI THỨ BẢY)
- **Nguồn PDF:** Trang 33–34 (Trang sách 244–245).
- **Loại Bố Cục:** `Template A (Full-Page Epic Splash: Quần hùng đồng thanh giơ cao gươm giáo và trống đồng rền vang)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 51 từ):**
  > Lời tuyên thệ của **Trưng Trắc** vang rền như **sấm động bên tai**, đốt cháy ngọn lửa căm hận đã dồn nén bấy lâu trong tim muôn dân Lạc Việt. Tất thảy các vị **bô lão, tộc trưởng, huyện lệnh và tướng sĩ** đồng loạt tuốt gươm hô vang, mở đầu **cuộc tổng khởi nghĩa vĩ đại nhất lịch sử**!
- **Bóng Thoại (Speech Bubble lớn vang dội):**
  - *Toàn thể tướng sĩ & tộc trưởng:* "QUYẾT ĐÁNH GIẶC TÔ ĐỊNH! QUYẾT ĐÁNH ĐUỔI LOÀI ÁC TẶC PHƯƠNG BẮC!"
- **Mô tả Khung hình (Visual Composition):**
  - Đại cảnh toàn trang nhìn từ trên cao xuống đại sảnh mở thông ra sân lớn Cổ Lôi sơn trang: Hàng trăm thanh trường thương, đại đao, cung nỏ đồng loạt giơ cao lên trời dưới ánh đuốc rực lửa; 17 chiếc trống đồng lớn được gióng lên rền vang, đàn voi chiến phía xa vươn vòi gầm vang vọng khắp núi rừng Mê Linh.


> Đính chính thiết kế 09/11/2026: áp dụng đối chiếu scan và chuẩn nhận diện tại `09_design_system/SOURCE_DECISIONS.md`; xem hồ sơ v1 trước khi dùng prompt cũ.

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [ENV03](../../../assets_generated/design_system/ENV03_v001.png): `assets_generated/design_system/ENV03_v001.png`
- [PROP02](../../../assets_generated/design_system/PROP02_v001.png): `assets_generated/design_system/PROP02_v001.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại `10_agent_workflow/parallel/agent_a/production_state.json`. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- historical: kiểm thật và ghi pass khi có bằng chứng.
- art: kiểm thật và ghi pass khi có bằng chứng.
- language: kiểm thật và ghi pass khi có bằng chứng.
- print_geometry: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
