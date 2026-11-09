---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
compartment: "01_source_material_analysis"
owner_agent: "AGENT-01 (Source Archivist & Visual Analyst)"
consumers: ["AGENT-02", "AGENT-03", "AGENT-04", "AGENT-05", "AGENT-06"]
---

# HƯỚNG DẪN SỬ DỤNG NGĂN 01: PHÂN TÍCH TÀI LIỆU NGUỒN & GIẢI PHẪU MẪU (`01_source_material_analysis`)

## 1. Mục đích của Ngăn 01
Ngăn này lưu trữ toàn bộ kết quả đọc hiểu, bóc tách và phân tích chuyên sâu từ **2 nguồn nguyên liệu gốc** mà Chủ dự án đã cung cấp:
1. **File `TRƯNG NỮ VƯƠNG.pdf` (58 trang scan, tương ứng trang sách 212–269 của tiểu thuyết lịch sử *Trưng Nữ Vương* - tác giả Phùng Văn Khai):** Nguồn cốt truyện, nhân vật, bối cảnh lịch sử, lời thoại và các chi tiết huyền sử.
2. **22 File ảnh `.jpg` mẫu (*Truyền thuyết An Dương Vương - Chiếc nỏ thần, thành Cổ Loa và mối tình bi kịch của Mỵ Châu - Trọng Thủy*):** Nguồn mẫu chuẩn về bố cục thiết kế trang, thiết kế bìa, cách đặt khung dẫn truyện, quy tắc tô màu chữ nhấn và phong cách minh họa.

Mục tiêu của Ngăn 01 là giúp **bất kỳ AI Agent nào** (dù không có khả năng đọc file PDF scan nặng 38MB hay xử lý hàng loạt ảnh cùng lúc) chỉ cần đọc các file `.md` trong ngăn này là **nắm được 100% nội dung văn bản gốc, các đoạn đã được đánh dấu bút `[ ... ]` trên trang sách, và công thức thiết kế của bộ ảnh mẫu**.

## 2. Danh mục Tài liệu trong Ngăn 01 & Hướng dẫn Đọc cho Từng Agent

| Tên File Markdown | Nội dung Chuyên sâu | Agent Nào Bắt buộc Đọc? | Cách Sử dụng Dữ liệu trong File |
| :--- | :--- | :--- | :--- |
| `PDF_CONTENT_DEEP_ANALYSIS.md` | Phân tích tổng thể 58 trang PDF: Bối cảnh lịch sử năm 40 SCN, cấu trúc Hồi 7 & Hồi 8, hệ thống 25+ nhân vật & bộ tộc, giải mã truyền thuyết dòng họ Phùng - Hùng Duệ Vương - Thánh Đóng - Tản Viên Sơn Thánh. | **Tất cả các Agent** (`AGENT-02`, `AGENT-03`, `AGENT-04`, `AGENT-06`) | Dùng để hiểu mạch truyện lớn, mối quan hệ nhân vật, địa danh lịch sử (Luy Lâu, Chu Diên, Mê Linh, Cổ Lôi sơn trang, cửa Hát Môn, sông Nhị Hà, núi Phượng Hoàng, bến Lục Đầu Giang) và thông điệp tự hào dân tộc. |
| `PDF_PAGE_BY_PAGE_ANNOTATIONS.md` | **Bảng giải mã chi tiết từng trang từ Trang PDF 01 đến Trang PDF 58** (trang sách 212–269), trích lục nguyên văn các đoạn được **đánh dấu ngoặc vuông `[ ... ]` và gạch chân** trên bản scan. | `AGENT-02` (Chuyển thể), `AGENT-03` (Biên kịch), `AGENT-06` (Kiểm định) | Dùng làm căn cứ trực tiếp để viết kịch bản phân cảnh và lời dẫn. **Ưu tiên số 1** là chuyển thể đầy đủ tất cả các trường đoạn nằm trong dấu ngoặc vuông `[ ... ]` và các câu văn được gạch chân. |
| `JPG_SAMPLE_LAYOUT_DECONSTRUCTION.md` | Giải phẫu toàn bộ 22 bức ảnh `.jpg` mẫu: Bảng ánh xạ tên file gốc sang thứ tự trang `00` (Bìa) -> `21` (Trang kết), nguyên văn lời dẫn trên 22 ảnh, phân tích 3 mẫu chia khung (Template A, B, C) và quy tắc tô đỏ từ khóa. | `AGENT-03` (Biên kịch), `AGENT-04` (Prompt/Mỹ thuật), `AGENT-05` (Dàn trang) | Dùng để học chính xác độ dài câu văn trong khung dẫn truyện (30–65 từ), cách chọn từ khóa tô đỏ, cách thiết kế Bìa sách và cách chia khung hình trên mỗi trang sách 19×24cm. |

## 3. Quy tắc Bảo toàn Dữ liệu Nguồn (Source Grounding Rules)
1. **Không bịa đặt sai lệch lịch sử - nguyên tác:** Mọi tên nhân vật (Trưng Trắc, Trưng Nhị, Thi Sách, Đinh Lương, Phùng Thị Chính, Đô Năng Tế, Cẩm Nương, Thánh Thiên, Nguyễn Huyền, Trưng Định, Đào Chiêu Hiển, Phạm Danh Hương, Lê Đạo, Bạch Uy, Tô Định, Tào Quyền, Mã Tắc, Lữ Thạch, Lục Hiến...) và địa danh phải viết đúng chính tả như trong `PDF_CONTENT_DEEP_ANALYSIS.md`.
2. **Tôn trọng dấu biên tập gốc (`[ ... ]` và gạch chân):** Trong file `TRƯNG NỮ VƯƠNG.pdf`, người biên tập ban đầu đã đọc và dùng bút đánh dấu ngoặc vuông `[ ... ]` quanh những đoạn văn giàu hình ảnh điện ảnh nhất, đồng thời gạch chân các hành động võ thuật, trang phục và lời thề đanh thép. Các Agent bước sau tuyệt đối không được bỏ sót các chi tiết đã được đánh dấu này.
