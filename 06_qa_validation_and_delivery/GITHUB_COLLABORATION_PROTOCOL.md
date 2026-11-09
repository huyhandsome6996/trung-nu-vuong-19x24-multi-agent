# GIAO THỨC CỘNG TÁC MULTI-AGENT TRÊN GITHUB (GITHUB WORKFLOW & HANDOFF PROTOCOL)

Để nhiều AI Agent có thể làm việc song song hoặc nối tiếp nhau trên kho lưu trữ GitHub này mà không giẫm chân lên nhau, mọi Agent tuân thủ quy chuẩn dưới đây.

## 1. Quy ước Phân Nhánh Git (Branch Naming Convention)
- `main`: Nhánh chính chứa toàn bộ cấu trúc 7 ngăn, tài liệu đặc tả `.md` và các trang đã đạt chuẩn `APPROVED`.
- `agent-01/source-analysis`: Nhánh cập nhật phân tích tài liệu nguồn.
- `agent-02/adaptation-bible`: Nhánh cập nhật hồ sơ nhân vật và quy chuẩn văn phong.
- `agent-03/storyboards`: Nhánh cập nhật kịch bản phân cảnh và lời dẫn.
- `agent-04/art-assets-part-1` & `agent-04/art-assets-part-2`: Nhánh sinh ảnh Character Sheets và ảnh nền 28 trang.
- `agent-05/layout-19x24`: Nhánh chế bản dàn trang, ghép khung chữ và xuất PDF 19×24 cm.
- `agent-06/qa-review`: Nhánh kiểm định chất lượng và phê duyệt phát hành.

## 2. Cấu trúc Đặt Tên File Thành Phẩm khi Đẩy lên Repo
Khi `AGENT-04` và `AGENT-05` sinh ra các file hình ảnh và PDF, hãy lưu theo đúng quy ước tên file chuẩn sau:
- **Character Reference Sheets:**
  - `assets_generated/characters/CHAR_01_Trung_Trac.png`
  - `assets_generated/characters/CHAR_02_Trung_Nhi.png`
  - `assets_generated/characters/CHAR_03_Thi_Sach_Lac_Hau.png`
  - `assets_generated/characters/CHAR_04_Thanh_Thien.png`
  - ...
- **Ảnh Minh Họa Nền Chưa Chữ (Raw Text-Free Illustrations - 2315×2906 px):**
  - `assets_generated/raw_pages/PAGE_00_Front_Cover_Raw.png`
  - `assets_generated/raw_pages/PAGE_01_Van_Lang_Khong_Tuoc_Raw.png`
  - ...
  - `assets_generated/raw_pages/PAGE_28_Trung_Nu_Vuong_Finale_Raw.png`
  - `assets_generated/raw_pages/PAGE_29_Back_Cover_Raw.png`
- **Trang Đã Ghép Khung Giấy Cổ & Chữ Tô Đỏ Hoàn Chỉnh (Final Typeset Pages - 300 DPI):**
  - `final_book_19x24/pages_jpg/00_Front_Cover_19x24.jpg`
  - `final_book_19x24/pages_jpg/01_Page_01_19x24.jpg`
  - ...
  - `final_book_19x24/pages_jpg/28_Page_28_19x24.jpg`
  - `final_book_19x24/pages_jpg/29_Back_Cover_19x24.jpg`
  - `final_book_19x24/TRUNG_NU_VUONG_19x24CM_PRINT_READY.pdf`

## 3. Mẫu Báo Cáo Bàn Giao Giữa Các Agent (Pull Request / Handoff Template)
Mỗi khi một Agent hoàn thành nhiệm vụ của mình, hãy ghi log bàn giao theo mẫu:

```markdown
### [AGENT HANDOFF REPORT]
- **Agent Thực hiện:** AGENT-04 (Art Director & Prompt Engineer)
- **Ngăn Đã Cập nhật:** `04_art_direction_and_image_prompts` / `assets_generated`
- **Phạm vi Hoàn thành:** Đã sinh đủ 10 Character Reference Sheets và 14 trang nền Hồi 7 (Trang 01 - Trang 14).
- **Kiểm tra Tự động:**
  - [x] Tỷ lệ khung hình khớp khổ 19x24cm (chừa 20% vùng thoáng đỉnh trang).
  - [x] Không chứa chữ rác (Text-free background).
  - [x] Đồng nhất gương mặt và trang phục nhân vật với Character Bible.
- **Agent Tiếp nhận Tiếp theo:** AGENT-05 (Book Designer & Layout Engineer).
```
