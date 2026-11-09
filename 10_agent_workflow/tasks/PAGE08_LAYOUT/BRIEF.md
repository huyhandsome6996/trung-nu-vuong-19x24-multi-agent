# PAGE08_LAYOUT — Trang08: ghép chữ và bố cục

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `layout`. Trạng thái: `todo`. Phụ thuộc: PAGE08_ART.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Dùng nguyên text đã khóa và tranh đã kiểm. Ghép khung giấy cổ, tô đỏ #C81E1E cho **...**, đặt đủ thoại/đuôi bóng đúng người. Khổ196×246/trim190×240. Dùng layout_tokens, đo tràn chữ bằng renderer thật; xuất bản xem PNG/PDF và nguồn có thể sửa. scripts/typeset_preview.py là trợ giúp HTML; không coi HTML/PDF xem trước là file in đã duyệt.

## Trang 08

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 59; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 08 — ĐẠI CHIẾN KỴ MÃ & TUYỆT CHIÊU "MÃNH LONG GIÁNG ĐỊA"
- **Nguồn PDF:** Trang 20–21 (Trang sách 231–232).
- **Loại Bố Cục:** `Template A (Full-Page Dynamic Battle Splash: Hai chiến mã giao phong giữa sân phủ)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 50 từ):**
  > Giữa vòng vây trùng điệp, **Thi Sách** một mình một ngựa quần thảo với chủ tướng Bắc doanh **Lữ Thạch**. Khi tên tướng giặc định rút trùy thủ đánh lén, Thi Sách bất ngờ **đứng hẳn trên yên ngựa**, vung trường thương tung tuyệt chiêu **“Mãnh long giáng địa”** đâm thẳng từ trên cao xuống như rồng giáng thế!
- **Bóng Thoại (Speech Bubble):** Không có (tập trung tối đa vào động tác võ thuật đỉnh cao).
- **Mô tả Khung hình (Visual Composition):**
  - Góc máy từ dưới hất lên (Low-angle heroic shot): Chiến mã đen tuyền của Thi Sách tung vó chồm cao; Thi Sách đứng vững trên yên ngựa, áo choàng Lạc Hầu bay phần phật trong khói lửa, hai tay giương cao ngọn trường thương bọc da hổ đâm sấm sét xuống đầu Lữ Thạch đang kinh hoàng giơ thương đỡ.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR03](../../../assets_generated/design_system/CHAR03_v001.png): `assets_generated/design_system/CHAR03_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
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
