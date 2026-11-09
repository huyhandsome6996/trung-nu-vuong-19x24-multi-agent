# PAGE18_ART — Trang18: tạo và kiểm tranh nền

Tệp được tạo lại bởi workflow.py; không sửa trực tiếp brief này.

Loại: `art`. Trạng thái: `todo`. Phụ thuộc: PAGE18_TEXT.

Đọc START_HERE.md, 10_agent_workflow/WORKFLOW_A_TO_Z.md, 09_design_system/SOURCE_DECISIONS.md.

## Việc cần làm

Lấy text đã khóa từ evidence bước TEXT. Xem các sheet liên quan; soạn prompt cuối theo cảnh, ghi actual_references và hash. Tạo ảnh bằng công cụ sinh ảnh, nền không chữ, không bóng thoại, chừa20% đỉnh; dùng đúng A/B/C. Kiểm mặt, phục trang, tay/chân/vũ khí và hành động. Lưu PNG native có phiên bản và metadata theo templates/RAW_IMAGE_METADATA.json. Không resize rồi khai native300DPI.

## Trang 18

Nguồn chữ hiện hành: `03_storyboards_and_scripts/STORYBOARD_PART_2_HOI_8_HAT_MON_PHUONG_HOANG.md`. Đếm tiếng bằng khoảng trắng: 64; mục tiêu35–65.

Bản text.draft.json giữ nguyên lời dẫn, CHƯA chép thoại và CHƯA được duyệt. Khi dùng cho chế bản phải chép đủ thoại, đặt trạng thái locked và kiểm thật.

### Cảnh và chữ từ storyboard

### TRANG 18 — LỜI THỀ HÁT MÔN DẬY SÓNG SÔNG NHỊ HÀ
- **Nguồn PDF:** Trang 41–42 (Trang sách 252–253).
- **Loại Bố Cục:** `Template A (Full-Page Iconic Splash: Trưng Trắc giương cao kiếm và đọc Hịch tế cáo trời đất trên đỉnh kỳ đài Hát Môn)`.
- **Text Khung Dẫn Truyện (Top Narration Box - 57 từ):**
  > Giữa tiếng sóng sông Nhị Hà vỗ bờ và tiếng trống đồng rung chuyển đất trời, **Chủ tướng Trưng Trắc** dõng dạc đọc **bài Hịch tế cáo trời đất**. Lời thề **đền nợ nước, trả thù nhà, khôi phục cơ nghiệp Lĩnh Nam** của dòng giống Hùng Vương vang vọng khắp núi sông, truyền đi khắp bốn phương như **ngọn gió lốc đại ngàn**!
- **Bóng Thoại (Speech Bubble - Trích nguyên văn lời Hịch cổ trang 253):**
  - *Trưng Trắc (trên đỉnh kỳ đài):* "Ta vốn dòng dõi hoàng tộc, con cháu Hùng tướng, vì nghĩa trừ hại! Hãy kề vai sát cánh mà giương cây cung mạnh, quét sạch bọn ngoại bang, lấy hết nước sông Thiên Hà mà rửa binh khí! Khôi phục cơ nghiệp Lĩnh Nam, cho muôn dân hưởng thái bình!"
- **Mô tả Khung hình (Visual Composition):**
  - Trang biểu tượng trung tâm của cả cuốn sách: **Trưng Trắc** đứng ở vị trí cao nhất trên kỳ đài Hát Môn, một tay cầm cuộn Hịch văn thẻ tre mở rộng, một tay rút thanh trường kiếm chỉ thẳng lên bầu trời xanh rực nắng; sát bên phải là **Trưng Nhị**, phía sau là hai vị sư phụ Đô Năng Tế – Cẩm Nương, 3 vị huyện lệnh và 17 vị tộc trưởng; phía dưới là hàng vạn nghĩa quân đồng loạt giơ cao gươm giáo hô vang dậy sóng sông Nhị Hà.

---

### Ảnh tham chiếu ứng viên

- [CHAR01](../../../assets_generated/characters/CHAR_01_Trung_Trac_v001.png): `assets_generated/characters/CHAR_01_Trung_Trac_v001.png`
- [CHAR02](../../../assets_generated/design_system/CHAR02_v001.png): `assets_generated/design_system/CHAR02_v001.png`
- [CHAR07](../../../assets_generated/design_system/CHAR07_v001.png): `assets_generated/design_system/CHAR07_v001.png`
- [ENV03](../../../assets_generated/design_system/ENV03_v001.png): `assets_generated/design_system/ENV03_v001.png`
- [PROP01](../../../assets_generated/design_system/PROP01_v001.png): `assets_generated/design_system/PROP01_v001.png`
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
