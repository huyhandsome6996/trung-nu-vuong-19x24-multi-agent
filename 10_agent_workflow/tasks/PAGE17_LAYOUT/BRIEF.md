# PAGE17_LAYOUT — Trang17: ghép chữ và bố cục

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `layout`. Trạng thái: `todo`. Phụ thuộc: PAGE17_ART.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Dùng nguyên text đã khóa và tranh đã kiểm. Ghép khung giấy cổ, tô đỏ #C81E1E cho **...**, đặt đủ thoại/đuôi bóng đúng người. Khổ196×246/trim190×240. Dùng layout_tokens, đo tràn chữ bằng renderer thật; xuất bản xem PNG/PDF và nguồn có thể sửa. scripts/typeset_preview.py là trợ giúp HTML; không coi HTML/PDF xem trước là file in đã duyệt.

## Trang 17

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 67; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 17 — SUY TÔN CHỦ TƯỚNG BA QUÂN TRƯỚC LINH VỊ VUA HÙNG
- **Nguồn PDF:** Trang 40–41 (Trang sách 251–252).
- **Loại Bố Cục:** `Template B (Khung trên cận cảnh bài vị Hùng Vương Quốc Chủ & lư hương đồng cổ - Khung dưới Hai Bà Trưng bước lên kỳ đài)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 53 từ):**
  > Trên đỉnh đài cao, khói hương trầm từ **chiếc lư đồng cổ** cuộn bay nghi ngút trước bài vị **“Hùng Vương Quốc Chủ”** và linh vị hai vị liệt sĩ **Trưng Định – Thi Sách**. Trước muôn vạn nghĩa quân, các vị trưởng lão và huyện lệnh đồng lòng suy tôn **Trưng Trắc làm Chủ soái ba quân**, cùng em gái **Trưng Nhị** bước lên kỳ đài.
- **Bóng Thoại (Speech Bubble):** Không có.
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Cận cảnh trang nghiêm chiếc lư hương đồng chạm khắc tinh xảo tỏa khói hương quyện thành hình chim Lạc và bóng dáng tiên tổ Hùng Vương trên nền trời, phía sau là bài vị vàng *"Hùng Vương Quốc Chủ"* và hai bài vị mới ghi tên *Trưng Định – Thi Sách*.
  - *Khung dưới:* Trong tiếng 9 hồi chiêng trống đồng vang rền, **Trưng Trắc** mặc giáp đồng và chiến bào đỏ son; **Trưng Nhị** mặc áo giáp nền lam sẫm viền đồng, điểm lụa đỏ; cả hai đều vấn khăn tang trắng kết hợp mũ kim khôi uy dũng bước lên bậc thềm kỳ đài.

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

Các tệp của bước trước nằm trong evidence của dependencies tại `10_agent_workflow/parallel/agent_a/production_state.json`. Không tạo lại chữ/ảnh đã khóa.

## Tiêu chí bàn giao

- vietnamese_fonts: kiểm thật và ghi pass khi có bằng chứng.
- red_keywords: kiểm thật và ghi pass khi có bằng chứng.
- safe_text: kiểm thật và ghi pass khi có bằng chứng.
- bleed_geometry: kiểm thật và ghi pass khi có bằng chứng.
- no_overflow: kiểm thật và ghi pass khi có bằng chứng.
- speech_placement: kiểm thật và ghi pass khi có bằng chứng.

Copy report.template.json thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts (đường dẫn từ gốc repo), checks và open_issues. Không sửa template thành báo cáo pass.

Chạy start trước khi làm; checkpoint sau phần nhỏ; finish sau check. Mỗi checkpoint có kết quả thì commit/push main.
