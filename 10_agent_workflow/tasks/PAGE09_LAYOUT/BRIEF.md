# PAGE09_LAYOUT — Trang09: ghép chữ và bố cục

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `layout`. Trạng thái: `todo`. Phụ thuộc: PAGE09_ART.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Dùng nguyên text đã khóa và tranh đã kiểm. Ghép khung giấy cổ, tô đỏ #C81E1E cho **...**, đặt đủ thoại/đuôi bóng đúng người. Khổ196×246/trim190×240. Dùng layout_tokens, đo tràn chữ bằng renderer thật; xuất bản xem PNG/PDF và nguồn có thể sửa. scripts/typeset_preview.py là trợ giúp HTML; không coi HTML/PDF xem trước là file in đã duyệt.

## Trang 09

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 65; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 09 — CHÉM ĐẦU LỮ THẠCH & KHÚC CA BI TRÁNG TẠI CHU DIÊN
- **Nguồn PDF:** Trang 22–23 (Trang sách 233–234).
- **Loại Bố Cục:** `Template B (Khung trên Thi Sách đâm gãy thương hạ sát Lữ Thạch - Khung dưới Đinh Lương cùng 200 tráng đinh và Thi Sách tử chiến giữa mưa tên)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 58 từ):**
  > Với sức mạnh áp đảo, **Thi Sách** đâm gãy trường thương của **Lữ Thạch**, phi thân kết liễu tên chủ tướng hung hãn ngay tại trận! Từ vườn nhãn, **Đinh Lương** vung đại đao dẫn **hai trăm tráng đinh** xông vào mở đường máu, nhưng trước biển quân thù hơn hai ngàn tên, **Thi Sách cùng toàn bộ nghĩa sĩ đã anh dũng hy sinh**.
- **Bóng Thoại (Speech Bubble):**
  - *Đinh Lương (vung đại đao giữa vòng vây):* "Giặc Mã! Cái chết của bọn ta hôm nay chính là ngày báo tang cho quân phương Bắc các ngươi!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Ngọn thương của Lữ Thạch gãy đôi văng lên không trung; Thi Sách rút thanh kiếm gia truyền Dương thị hạ gục Lữ Thạch trước sự kinh hoàng của Mã Tắc.
  - *Khung dưới (Xử lý nghệ thuật bi tráng cho lứa tuổi lớp 8–10):* Giữa biển lửa đỏ rực tại sân phủ Chu Diên, Thi Sách và Đinh Lương đứng tựa lưng vào nhau trên bậc thềm đá, xung quanh là hàng trăm mũi tên cắm trên khiên và đất; cả hai vẫn đứng thẳng hiên ngang như hai bức tượng đồng bất tử dưới ánh lửa.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR03](../../../assets_generated/design_system/CHAR03_v001.png): `assets_generated/design_system/CHAR03_v001.png`
- [CHAR05](../../../assets_generated/design_system/CHAR05_v001.png): `assets_generated/design_system/CHAR05_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [CHAR11](../../../assets_generated/design_system/CHAR11_v001.png): `assets_generated/design_system/CHAR11_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
- [PROP03](../../../assets_generated/design_system/PROP03_v002.png): `assets_generated/design_system/PROP03_v002.png`
- [ANIMAL01](../../../assets_generated/design_system/ANIMAL01_v001.png): `assets_generated/design_system/ANIMAL01_v001.png`
- [ARMY01](../../../assets_generated/design_system/ARMY01_v001.png): `assets_generated/design_system/ARMY01_v001.png`
- [CHIEFS01](../../../assets_generated/design_system/CHIEFS01_v001.png): `assets_generated/design_system/CHIEFS01_v001.png`

reference_candidates.json là danh sách ứng viên, không phải tuyên bố mọi ảnh đã truyền cho công cụ. Ghi lại ảnh thực dùng trong metadata. Mở từng ảnh để kiểm mặt/vị trí trước khi tạo.

Các tệp của bước trước nằm trong evidence của dependencies tại production_state.json. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- vietnamese_fonts: kiểm thật và ghi pass khi có bằng chứng.
- red_keywords: kiểm thật và ghi pass khi có bằng chứng.
- safe_text: kiểm thật và ghi pass khi có bằng chứng.
- bleed_geometry: kiểm thật và ghi pass khi có bằng chứng.
- no_overflow: kiểm thật và ghi pass khi có bằng chứng.
- speech_placement: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
