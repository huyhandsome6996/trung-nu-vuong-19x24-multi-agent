# PAGE04_ART — Trang04: tạo và kiểm tranh nền

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `art`. Trạng thái: `todo`. Phụ thuộc: PAGE04_TEXT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Lấy text đã khóa từ evidence bước TEXT. Xem các sheet liên quan; soạn prompt cuối theo cảnh, ghi actual_references và hash. Tạo ảnh bằng công cụ sinh ảnh, nền không chữ, không bóng thoại, chừa20% đỉnh; dùng đúng A/B/C. Kiểm mặt, phục trang, tay/chân/vũ khí và hành động. Lưu PNG native có phiên bản và metadata theo templates/RAW_IMAGE_METADATA.json. Không resize rồi khai native300DPI.

## Trang 04

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 61; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 04 — LỜI THỀ TRUNG NGHĨA CỦA HẬU DUỆ HỌ PHÙNG TẠI PHỦ CHU DIÊN
- **Nguồn PDF:** Trang 04–05 & 10–11 (Trang sách 215–216 & 221–222).
- **Loại Bố Cục:** `Template A (Full-Page Splash cảnh sảnh đường phủ Chu Diên lúc bình minh)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 55 từ):**
  > Tại huyện **Chu Diên**, **Huyện lệnh Thi Sách** vừa tiễn phu nhân **Trưng Trắc** về Mê Linh bàn kế lớn thì triệu ngay đôi vợ chồng trẻ **Đinh Lương – Phùng Thị Chính**. Mang trong mình dòng máu của **Thánh Đóng Phùng Lực Công** năm xưa, đôi vợ chồng trẻ nguyện **vào núi đao biển lửa** cùng chủ công cứu nước.
- **Bóng Thoại (Speech Bubble):**
  - *Phùng Thị Chính (chắp tay kiên định):* "Vợ chồng tiểu nữ dẫu phải vào núi đao biển lửa cũng quyết theo chủ công đánh đuổi giặc phương Bắc!"
- **Mô tả Khung hình (Visual Composition):**
  - Tiền cảnh là Huyện lệnh Thi Sách uy nghiêm, lịch lãm đang đứng trước án thư trong phủ Chu Diên; đối diện là tráng sĩ Đinh Lương và nữ tướng trẻ Phùng Thị Chính đang chắp tay tuyên thệ dưới ánh nắng sớm chiếu qua khung cửa gỗ.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR03](../../../assets_generated/design_system/CHAR03_v001.png): `assets_generated/design_system/CHAR03_v001.png`
- [CHAR05](../../../assets_generated/design_system/CHAR05_v001.png): `assets_generated/design_system/CHAR05_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP03](../../../assets_generated/design_system/PROP03_v002.png): `assets_generated/design_system/PROP03_v002.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại production_state.json. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- actual_refs: kiểm thật và ghi pass khi có bằng chứng.
- character_consistency: kiểm thật và ghi pass khi có bằng chứng.
- no_text: kiểm thật và ghi pass khi có bằng chứng.
- top_clearance: kiểm thật và ghi pass khi có bằng chứng.
- anatomy: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
