# THÔNG SỐ KỸ THUẬT XUẤT BẢN CHUẨN: KHỔ SÁCH 19x24 CM (PRINT & LAYOUT MASTER SPECS)

> Hiệu lực hiện hành: tọa độ cụ thể theo [layout_tokens](09_design_system/layout_components/layout_tokens.json) và [ngoại lệ đã khóa](09_design_system/SOURCE_DECISIONS.md). Mép giấy cổ X11..179/Y8..48 là trang trí; chữ X18..172/Y14..43 trong safe text. Gáy/giấy/đóng chỉ là phương án tạm, phải chốt PRINT_SPEC với nhà in.

Tài liệu này là **Quy chuẩn Kỹ thuật Bắt buộc (Hard Constraints)** cho mọi AI Agent tham gia thiết kế minh họa, dàn trang, làm bìa và xuất file PDF/JPG cho dự án **TRƯNG NỮ VƯƠNG**.

## 1. Thông số Kích thước Vật lý & Độ phân giải (Physical Dimensions & Pixel Grid)

Khổ sách **19cm × 24cm** là khổ sách vàng của dòng sách tranh truyện lịch sử, sách thiếu niên - học đường cao cấp tại Việt Nam (lớn hơn khổ truyện tranh thông thường 13×18cm, mang lại không gian đại cảnh chiến trận và thành quách cực kỳ hoành tráng).

| Hạng mục Thông số | Kích thước Hệ Mét (mm / cm) | Kích thước Pixel ở 300 DPI (Chuẩn In Offset) | Kích thước Pixel ở 150 DPI (Bản Xem trước / Web) | Ghi chú Kỹ thuật cho AI Agent |
| :--- | :--- | :--- | :--- | :--- |
| **Khổ thành phẩm (Trim Size)** | **190 mm × 240 mm** *(19 cm × 24 cm)* | **2244 px × 2835 px** | **1122 px × 1417 px** | Kích thước trang sách sau khi xén giấy thành phẩm. Tỷ lệ khung hình: `19 : 24` (`≈ 0.7917`). |
| **Khổ tràn lề (Bleed Size - cộng 3mm mỗi cạnh)** | **196 mm × 246 mm** *(19.6 cm × 24.6 cm)* | **2315 px × 2906 px** | **1157 px × 1453 px** | Mọi tranh minh họa nền (Full-bleed background) phải xuất ở kích thước này để khi xén không bị hở viền trắng. |
| **Vùng an toàn (Safe Zone - cách mép xén 12mm–15mm)** | **162 mm × 212 mm** *(Lề trong 16mm, Lề ngoài 12mm, Trên/Dưới 14mm)* | **1913 px × 2504 px** | **956 px × 1252 px** | Toàn bộ **chữ trong Khung dẫn truyện** (mép giấy cổ là ngoại lệ trang trí), **Bóng thoại (Speech Bubbles)**, **Số trang** và **Gương mặt nhân vật chính** BẮT BUỘC nằm trọn trong vùng này. |
| **Trải đôi 2 trang (Double-Page Spread Trim)** | **380 mm × 240 mm** *(38 cm × 24 cm)* | **4488 px × 2835 px** | **2244 px × 1417 px** | Dùng khi thiết kế đại cảnh trải đôi (ví dụ: Đại lễ tế cờ tại đàn thề Hát Môn). |
| **Trải đôi 2 trang có tràn lề (Spread with Bleed)** | **386 mm × 246 mm** *(38.6 cm × 24.6 cm)* | **4559 px × 2906 px** | **2280 px × 1453 px** | Tránh đặt mặt nhân vật hoặc chữ ngay đường gáy giữa (Gutter `x = 193mm ± 8mm`). |

## 2. Thông số Thiết kế Bìa Sách Khổ 19x24 cm (Cover Spread Specifications)

Bộ truyện có cấu trúc chuẩn **32 trang ruột** (in trên giấy Couche Matt 150gsm, độ dày gáy sách ước tính `3.0 mm` đối với bìa mềm có tay gấp, hoặc `5.0 mm` đối với bìa cứng).

| Thành phần Bìa | Kích thước Thành phẩm (mm) | Kích thước Có Tràn lề 3mm (mm) | Kích thước Pixel (300 DPI) | Nội dung Bắt buộc trên Thiết kế |
| :--- | :--- | :--- | :--- | :--- |
| **Bìa Trước (Front Cover - Bìa 1)** | `190 mm × 240 mm` | `193 mm × 246 mm` *(3mm trên/dưới/phải)* | `2280 px × 2906 px` | Tít phụ trên dải lụa vàng + Đại tự **TRƯNG NỮ VƯƠNG** + Phụ đề trong khung mây + Tên tập/chương + Đại cảnh Hai Bà Trưng, Thi Sách, Thánh Thiên & thành Luy Lâu / đàn thề Hát Môn. |
| **Gáy Sách (Spine)** | `3.5 mm × 240 mm` *(Bìa mềm 32–36 trang)* | `3.5 mm × 246 mm` | `41 px × 2906 px` | Tên sách **TRƯNG NỮ VƯƠNG** chạy dọc từ trên xuống, số tập, logo ở chân gáy. |
| **Bìa Sau (Back Cover - Bìa 4)** | `190 mm × 240 mm` | `193 mm × 246 mm` *(3mm trên/dưới/trái)* | `2280 px × 2906 px` | Tranh minh họa bi tráng (Lư hương đồng Bách Việt & cờ nghĩa ngũ sắc tung bay bên sông Nhị Hà) + Khung tóm tắt cốt truyện hào hùng + Thông tin xuất bản & Khung mã vạch ISBN góc dưới bên phải. |
| **Bìa Trải Toàn bộ (Full Cover Spread)** | `383.5 mm × 240 mm` | **389.5 mm × 246 mm** | **4600 px × 2906 px** | File tổng hợp ghép Bìa Sau (Trái) + Gáy (Giữa) + Bìa Trước (Phải). |

## 3. Bảng Đối chiếu Tỷ lệ giữa Ảnh Mẫu `.jpg` và Khổ Sách Đích 19x24 cm

Qua phân tích kỹ thuật 22 file `.jpg` mẫu trong `truyen.zip`:
- Kích thước gốc của 22 ảnh `.jpg` mẫu: **`1086 px × 1448 px`** (Tỷ lệ `3 : 4` = `0.750`).
- Kích thước khổ sách đích `19cm × 24cm`: **`2244 px × 2835 px`** ở 300 DPI (Tỷ lệ `19 : 24` = `0.7917`).
- **Quy tắc chuyển đổi cho AI Agent:**
  1. Khổ `19×24cm` rộng hơn theo chiều ngang khoảng **5.5%** so với tỷ lệ `3:4` của ảnh mẫu. Đây là một lợi thế lớn cho sách in vì giúp **Khung dẫn truyện (Narration Box)** ở đầu trang chứa được câu chữ thoáng mắt hơn và đại cảnh chiến trận (thuyền chiến trên sông Nhị Hà, thành Chu Diên, núi Phượng Hoàng) trải rộng hào hùng hơn.
  2. Khi gọi các mô hình sinh ảnh chỉ hỗ trợ tỷ lệ cố định (`3:4` hoặc `4:5`):
     - Nếu sinh ở tỷ lệ `3:4` (`0.75`): Mở rộng nhẹ hai bên biên hoặc crop nhẹ 2.5% cạnh trên/dưới để khớp hoàn hảo vào khung `196mm × 246mm` (`0.796`).
     - Nếu sinh ở tỷ lệ `4:5` (`0.80`): Khớp gần như tuyệt đối (`0.80` so với `0.7917`, chênh lệch dưới 1%) — chỉ cần trim nhẹ 1mm hai bên mép tràn lề! **Do đó, khuyến nghị ưu tiên sử dụng tỷ lệ `4:5` hoặc `3:4` có chừa biên an toàn khi gọi công cụ sinh ảnh AI.**
