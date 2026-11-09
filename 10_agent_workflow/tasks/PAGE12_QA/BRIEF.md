# PAGE12_QA — Trang12: kiểm nguồn/mỹ thuật/chữ/khổ

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `qa`. Trạng thái: `todo`. Phụ thuộc: PAGE12_LAYOUT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Mở ảnh render ở kích thước đọc thật và zoom100%; so với scan, sheet, text đã khóa. Kiểm bốn lớp historical/art/language/print_geometry. Ghi lỗi cụ thể và sửa về đúng bước. Báo cáo pass chỉ khi có artifact thực và không còn lỗi trong phạm vi; đây là QA của agent, không phải chủ dự án duyệt.

## Trang 12

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 69; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 12 — BA VỊ HUYỆN LỆNH NGHĨA KHÍ TỤ HỘI VỀ CỔ LÔI SƠN TRANG
- **Nguồn PDF:** Trang 29–31 (Trang sách 240–242).
- **Loại Bố Cục:** `Template C (3 khung giới thiệu 3 vị huyện lệnh tài ba: Lê Đạo - Đào Chiêu Hiển - Phạm Danh Hương)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 54 từ):**
  > Cái chết bi tráng của các bậc anh hùng ở Chu Diên và Luy Lâu đã làm **rung chuyển toàn cõi Giao Chỉ**. Ngay trong buổi sớm ấy, ba vị huyện lệnh người Việt là **Lê Đạo**, **Đào Chiêu Hiển** và **Phạm Danh Hương** đã dứt khoát **trút bỏ ấn quan nhà Hán**, đem toàn bộ gia sản và nghĩa binh tìm về **Cổ Lôi sơn trang** tụ nghĩa.
- **Bóng Thoại (Speech Bubble):**
  - *Phạm Danh Hương (tay cầm phất trần trắng):* "Lão hủ xem tinh tượng biết khí vận nước Nam đã tới, xin dâng toàn bộ binh lương theo chủ công khởi nghĩa!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung 1:* Huyện lệnh Khúc Dương **Lê Đạo** cao lớn, râu ba chòm điểm bạc, trên vai đậu một con **chim ưng đen tuyền**, tay cầm ống trúc mật báo bước vào sơn trang.
  - *Khung 2:* Huyện lệnh Câu Lậu **Đào Chiêu Hiển** tráng kiện, mắt sáng miệng rộng, dẫn theo đội kỵ binh tinh nhuệ.
  - *Khung 3:* Lão huyện lệnh An Định **Phạm Danh Hương** râu tóc bạc phơ như tiên ông, tay cầm cây phất trần trắng muốt cúi chào nhị vị sư phụ và hai chị em họ Trưng.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR02](../../../assets_generated/design_system/CHAR02_v001.png): `assets_generated/design_system/CHAR02_v001.png`
- [CHAR07](../../../assets_generated/design_system/CHAR07_v001.png): `assets_generated/design_system/CHAR07_v001.png`
- [CHAR08](../../../assets_generated/design_system/CHAR08_v001.png): `assets_generated/design_system/CHAR08_v001.png`
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
