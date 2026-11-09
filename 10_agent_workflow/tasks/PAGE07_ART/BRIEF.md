# PAGE07_ART — Trang07: tạo và kiểm tranh nền

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `art`. Trạng thái: `todo`. Phụ thuộc: PAGE07_TEXT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Lấy text đã khóa từ evidence bước TEXT. Xem các sheet liên quan; soạn prompt cuối theo cảnh, ghi actual_references và hash. Tạo ảnh bằng công cụ sinh ảnh, nền không chữ, không bóng thoại, chừa20% đỉnh; dùng đúng A/B/C. Kiểm mặt, phục trang, tay/chân/vũ khí và hành động. Lưu PNG native có phiên bản và metadata theo templates/RAW_IMAGE_METADATA.json. Không resize rồi khai native300DPI.

## Trang 07

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 60; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 07 — TUYỆT KỸ TIỄN PHÁP THẦN THÔNG CỦA DƯƠNG HUYỆN LỆNH
- **Nguồn PDF:** Trang 17–19 (Trang sách 228–230).
- **Loại Bố Cục:** `Template B (Khung trên Thi Sách giương cung bắn liên tiếp mười phát tên - Khung dưới 10 tên giặc ngã rạp & chiến mã phi ra)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 52 từ):**
  > Trước cổng phủ, tên tướng giặc **Lữ Thạch** ngạo mạn buông lời dụ hàng rồi bất ngờ **bắn tên lén** về phía Thi Sách. Chàng lập tức gạt tên giặc, rút cây **cung gia bảo** bắn liên tiếp **mười phát tên thần thông**, xuyên thủng hàng ngũ khiên giáo của kẻ thù rồi tung mình lên **chiến mã đen tuyền**.
- **Bóng Thoại (Speech Bubble):**
  - *Thi Sách:* "Lữ Thạch! Bọn ngươi miệng nói nhân nghĩa mà đằng sau gươm giáo hại người. Hôm nay đừng hòng toàn mạng trở về!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung trên:* Cận cảnh Thi Sách đứng hiên ngang trước thềm phủ Chu Diên, kéo căng dây cung gia bảo bắn mười mũi tên liên tiếp xé gió lao đi.
  - *Khung dưới:* Hàng loạt lính khiên giáp hộ vệ trước mặt Lữ Thạch ngã rạp, ngựa của Lữ Thạch hoảng sợ chồm lên; trong khi đó con chiến mã đen tuyền (Hắc mã) của Thi Sách tung vó phi ra đón chủ nhân.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR03](../../../assets_generated/design_system/CHAR03_v001.png): `assets_generated/design_system/CHAR03_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [CHAR11](../../../assets_generated/design_system/CHAR11_v001.png): `assets_generated/design_system/CHAR11_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
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
