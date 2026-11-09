---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
compartment: "07_reference_assets"
owner_agent: "AGENT-01 (Source Archivist & Visual Analyst)"
consumers: ["ALL_AGENTS"]
---

# HƯỚNG DẪN SỬ DỤNG NGĂN 07: KHO TÀI NGUYÊN THAM CHIẾU ĐÃ CHUẨN HÓA (`07_reference_assets`)

## 1. Mục đích của Ngăn 07
Ngăn 07 lưu trữ trực tiếp các hình ảnh mẫu và bản chụp tổng hợp (Contact Sheets) đã được sắp xếp, đổi tên chuẩn xác để bất kỳ AI Agent đa phương thức (Multimodal / Vision Agent) nào trên GitHub cũng có thể mở xem trực tiếp mà không bị lỗi tên file lộn xộn hay vượt quá giới hạn dung lượng file đơn lẻ của GitHub.

## 2. Cấu trúc Thư mục trong Ngăn 07

1. **`sample_an_duong_vuong_sorted/` (22 File `.jpg` Mẫu Đã Sắp Xếp Đúng Thứ Tự Đọc):**
   - Trong file nén ban đầu, 22 bức ảnh mẫu (*Truyền thuyết An Dương Vương*) bị đánh số ngược từ trang cuối về trang bìa.
   - Tại thư mục này, toàn bộ 22 bức ảnh đã được **đổi tên và đánh số lại từ `00` (Trang Bìa) đến `21` (Trang Kết)** kèm tên mô tả bố cục:
     - `00_Cover_An_Duong_Vuong_MultiLayer.jpg` (Mẫu thiết kế Bìa sách đa tầng & Typography 4 tầng)
     - `01_Page_01_TemplateA_Splash_Mo_Dau.jpg` -> `21_Page_21_TemplateA_Splash_Ket_Truyen.jpg`
   - **Cách dùng cho AI Agent:** Dùng làm **Style Reference (`--sref` / `image_references`)** cho `AGENT-04` và làm **Mẫu Đo Tọa Độ Khung Dẫn Truyện Giấy Cổ** cho `AGENT-05`.

2. **`pdf_annotated_contact_sheets/` (10 Bảng Chụp Toàn Bộ 58 Trang `TRƯNG NỮ VƯƠNG.pdf`):**
   - Vì file `TRƯNG NỮ VƯƠNG.pdf` gốc là bản scan nặng `38 MB` (vượt giới hạn upload web 25 MB của GitHub và gây tràn bộ nhớ ngữ cảnh nếu đọc trực tiếp), toàn bộ 58 trang sách (trang 212–269) đã được trích xuất thành **10 bảng ảnh độ nét cao (`pdf_pages_01_to_06.jpg` ... `pdf_pages_55_to_58.jpg`)**.
   - Trên các trang này giữ nguyên **các dấu ngoặc vuông `[ ... ]` và đường gạch chân bằng bút** của người biên tập gốc.
   - **Cách dùng cho AI Agent:** Kết hợp xem trực tiếp 10 bảng ảnh này với bản giải mã văn bản tại `01_source_material_analysis/PDF_PAGE_BY_PAGE_ANNOTATIONS.md`.
