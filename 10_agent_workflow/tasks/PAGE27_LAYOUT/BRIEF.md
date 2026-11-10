# PAGE27_LAYOUT — Trang27: ghép chữ và bố cục

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `layout`. Trạng thái: `todo`. Phụ thuộc: PAGE27_ART.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Dùng nguyên text đã khóa và tranh đã kiểm. Ghép khung giấy cổ, tô đỏ #C81E1E cho **...**, đặt đủ thoại/đuôi bóng đúng người. Khổ196×246/trim190×240. Dùng layout_tokens, đo tràn chữ bằng renderer thật; xuất bản xem PNG/PDF và nguồn có thể sửa. scripts/typeset_preview.py là trợ giúp HTML; không coi HTML/PDF xem trước là file in đã duyệt.

## Trang 27

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 56; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 27 — SÓNG DẬY LĨNH NAM: THU PHỤC SÁU MƯƠI LĂM THÀNH TRÌ
- **Nguồn bổ sung:** HIST01, Bảo tàng Lịch sử Quốc gia (17/01/2013), đối chiếu09/11/2026 tại10_agent_workflow/tasks/SOURCE_EPILOGUE; chuyển từ mạch tiểu thuyết sang tổng kết lịch sử, không có trong scan58trang.
- **Loại Bố Cục:** `Template A (Full-Page Epic Montage Splash: Đại quân Hai Bà Trưng cưỡi voi chiến và chiến thuyền của Thánh Thiên – Lê Đạo hợp quân tiến đánh thành Luy Lâu)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 56 tiếng theo khoảng trắng):**
  > Khép lại những trận đánh ở **núi Phượng Hoàng** và **Lục Đầu Giang**, câu chuyện hướng về khởi nghĩa **Hát Môn**. Năm40, dưới cờ **Hai Bà Trưng**, nghĩa quân **đánh chiếm thành Luy Lâu**, buộc **Tô Định** tháo chạy. Những nhân vật như **Thánh Thiên, Phùng Thị Chính** góp vào bức tranh hào hùng của truyện.
- **Bóng Thoại (Speech Bubble):** Không có.
- **Mô tả Khung hình (Visual Composition):**
  - Đại cảnh toàn trang rực rỡ sắc đỏ – vàng kim: **Hai Bà Trưng (Trưng Trắc – Trưng Nhị)** cưỡi trên lưng hai thớt voi chiến da xám, ngà trắng khổng lồ, sát cánh bên cạnh là nữ tướng **Thánh Thiên** cưỡi chiến mã và **Phùng Thị Chính**, phía sau là hàng vạn nghĩa quân giương cờ ngũ sắc tràn qua cổng thành Luy Lâu đang mở toang.

---
- **Giới hạn hình ảnh:** Đội hình hợp quân là montage nhân vật truyện, không phải bằng chứng khảo chứng Thánh Thiên–Phùng Thị Chính cùng có mặt tại cổng Luy Lâu. Không khẳng định tuyến hành quân từ Phượng Hoàng.

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR02](../../../assets_generated/design_system/CHAR02_v001.png): `assets_generated/design_system/CHAR02_v001.png`
- [CHAR04](../../../assets_generated/design_system/CHAR04_v001.png): `assets_generated/design_system/CHAR04_v001.png`
- [CHAR05](../../../assets_generated/design_system/CHAR05_v001.png): `assets_generated/design_system/CHAR05_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP02](../../../assets_generated/design_system/PROP02_v001.png): `assets_generated/design_system/PROP02_v001.png`
- [PROP04](../../../assets_generated/design_system/PROP04_v002.png): `assets_generated/design_system/PROP04_v002.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại `10_agent_workflow/parallel/agent_b/production_state.json`. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- vietnamese_fonts: kiểm thật và ghi pass khi có bằng chứng.
- red_keywords: kiểm thật và ghi pass khi có bằng chứng.
- safe_text: kiểm thật và ghi pass khi có bằng chứng.
- bleed_geometry: kiểm thật và ghi pass khi có bằng chứng.
- no_overflow: kiểm thật và ghi pass khi có bằng chứng.
- speech_placement: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
