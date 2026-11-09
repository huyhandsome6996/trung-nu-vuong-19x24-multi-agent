# PAGE03_ART — Trang03: tạo và kiểm tranh nền

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `art`. Trạng thái: `todo`. Phụ thuộc: PAGE03_TEXT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Lấy text đã khóa từ evidence bước TEXT. Xem các sheet liên quan; soạn prompt cuối theo cảnh, ghi actual_references và hash. Tạo ảnh bằng công cụ sinh ảnh, nền không chữ, không bóng thoại, chừa20% đỉnh; dùng đúng A/B/C. Kiểm mặt, phục trang, tay/chân/vũ khí và hành động. Lưu PNG native có phiên bản và metadata theo templates/RAW_IMAGE_METADATA.json. Không resize rồi khai native300DPI.

## Trang 03

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_1_HOI_7_CHU_DIEN.md`. Đếm tiếng bằng khoảng trắng: 61; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 03 — ÁCH ĐÔ HỘ BẠO TÀN & ĐÊM MẬT LỆNH THÀNH LUY LÂU
- **Nguồn PDF:** Trang 01–03 (Trang sách 212–214).
- **Loại Bố Cục:** `Template C (1 khung lớn cảnh đêm phủ Luy Lâu + 1 khung Zoom tròn chiếc Hổ phù điều binh + 1 khung dưới ngục tối)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 54 từ):**
  > Hàng trăm năm sau, đất **Giao Chỉ** rơi vào ách cai trị tàn bạo của **Thái thú Tô Định** nhà Đông Hán. Sợ hãi trước uy tín của hai dòng họ lớn **Trưng – Dương**, Tô Định dùng kế độc **“Tiên phát chế nhân”**, lừa bắt giam **Thần y Nguyễn Huyền** và **Huyện lệnh Mê Linh Trưng Định** vào ngục tối.
- **Bóng Thoại (Speech Bubble):**
  - *Tô Định (nét mặt nham hiểm):* "Hãy cầm lấy hổ phù, ngay trong đêm nay dẫn binh đánh úp phủ Chu Diên, giết sạch nhà Thi Sách!"
- **Mô tả Khung hình (Visual Composition):**
  - *Khung chính:* Trong căn phòng u tối thắp đèn nến tại thành Luy Lâu lúc nửa đêm, Thái thú Tô Định khoác đại bào lông thú đang trao thẻ đồng cho Tư mã Mã Tắc và tướng giặc Lữ Thạch.
  - *Khung Zoom tròn (Inset):* Cận cảnh bàn tay Tô Định trao chiếc **Hổ phù bằng đồng đen** lạnh lẽo.
  - *Khung góc dưới:* Hình ảnh hai bậc trưởng giả Nguyễn Huyền và Trưng Định bị giam trong ngục tối Luy Lâu nhưng ánh mắt vẫn sáng quắc bất khuất.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR06](../../../assets_generated/design_system/CHAR06_v001.png): `assets_generated/design_system/CHAR06_v001.png`
- [CHAR10](../../../assets_generated/design_system/CHAR10_v001.png): `assets_generated/design_system/CHAR10_v001.png`
- [CHAR11](../../../assets_generated/design_system/CHAR11_v001.png): `assets_generated/design_system/CHAR11_v001.png`
- [ENV02](../../../assets_generated/design_system/ENV02_v001.png): `assets_generated/design_system/ENV02_v001.png`
- [PROP02](../../../assets_generated/design_system/PROP02_v001.png): `assets_generated/design_system/PROP02_v001.png`
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
