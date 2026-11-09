# THÔNG SỐ TỌA ĐỘ DÀN TRANG RUỘT KHỔ 19x24 CM (INTERIOR PAGE LAYOUT TEMPLATES)

## 1. Hệ Trục Tọa Độ Trang Sách 19x24 cm (Coordinate Grid System)
- **Hệ tọa độ gốc `(0, 0)`:** Góc trên bên trái của trang thành phẩm (`190mm × 240mm` | `2244px × 2835px` @ 300 DPI).
- **Tràn lề (Bleed):** Mở rộng ra ngoài từ `-3mm` đến `193mm` theo trục X, và từ `-3mm` đến `243mm` theo trục Y (`2315px × 2906px` @ 300 DPI).

## 2. Thông số Kỹ thuật của Khung Dẫn Truyện Giấy Cổ (Top Parchment Narration Box)

Đây là thành phần nhận diện quan trọng nhất được học từ 22 ảnh `.jpg` mẫu:

| Thuộc tính | Giá trị Hệ Mét (mm) | Giá trị Pixel (@ 300 DPI) | Quy chuẩn Thiết kế Đồ họa |
| :--- | :--- | :--- | :--- |
| **Vị trí Trục X (`left` -> `right`)** | `X = 11 mm` đến `X = 179 mm` *(Rộng `168 mm` = 88.4% khổ ngang)* | `130 px` -> `2114 px` *(Rộng `1984 px`)* | Căn giữa trang tuyệt đối (`margin: 0 auto`). Đảm bảo cách mép xén hai bên `11mm` (nằm gọn trong vùng an toàn). |
| **Vị trí Trục Y (`top` -> `bottom`)** | `Y = 8 mm` đến `Y = 48 mm` *(Cao `38 mm – 44 mm` tùy 3 hay 5 dòng chữ)* | `94 px` -> `567 px` *(Cao `450 px – 520 px`)* | Nằm ở 18%–20% phía trên trang sách, đè lên vùng bầu trời/không gian thoáng của tranh nền. |
| **Nền Giấy Cổ (Background Fill)** | Chuyển sắc tâm (Radial Gradient) | — | Tâm khung màu Vàng Kem Sáng (`#FFFBEB`), chuyển dần ra rìa khung màu Vàng Đất Cổ (`#FDE68A` -> `#F59E0B`), độ đục `opacity: 0.96`. |
| **Viền Khung (Parchment Border)** | Dày `1.2 mm` (`~3.5 pt`) | `14 px` | Viền mực đen nâu (`#1C1917`) có độ sần/răng cưa nhẹ giả mép giấy dó cổ hoặc cuộn da cổ, bo góc `6mm` (`70px`), kèm bóng đổ mềm (`drop-shadow: 0 4px 10px rgba(0,0,0,0.45)`). |
| **Font Chữ & Cỡ Chữ (Typography)** | Cỡ chữ: **`12.5 pt – 13.5 pt`**<br>Khoảng cách dòng (`line-height`): **`1.42`** | `52 px – 56 px` | Sử dụng Font hỗ trợ đầy đủ tiếng Việt có dấu đậm nét truyền thống pha hiện đại: **Noto SansSemiBold / Baloo 2 Bold / Merriweather Bold / Patrick Hand VN**. |
| **Quy tắc Màu Chữ (Dual-Color Text)** | Chữ thường: **`#1A1A1A`**<br>Chữ nhấn (`**...**`): **`#C81E1E`** | — | Mọi cụm từ được đánh dấu `**...**` trong kịch bản Ngăn 03 được render bằng màu **Đỏ Son (`#C81E1E`)** in đậm (`font-weight: 800`). |

## 3. Thông số Tọa độ 3 Mẫu Chia Khung Tranh (The 3 Layout Templates on 190×240mm Canvas)

### 3.1. Template A — Đại Cảnh Toàn Trang (Full-Bleed Cinematic Splash)
- **Áp dụng cho các trang:** `04, 06, 08, 11, 13, 14, 16, 18, 20, 22, 23, 26, 27, 28` (14 trang).
- **Cấu trúc lớp (Z-Index Layers):**
  - `Layer 0 (Z=0)`: Tranh minh họa toàn trang phủ kín vùng tràn lề `196mm × 246mm` (`2315 × 2906 px`).
  - `Layer 1 (Z=10)`: Khung dẫn truyện giấy cổ tại `X: 11mm..179mm`, `Y: 8mm..48mm`.
  - `Layer 2 (Z=20)`: Bóng thoại nhân vật (nếu có) đặt tại vùng trung cảnh (`Y: 60mm..120mm`), cách xa gương mặt nhân vật chính và có đuôi nhọn chỉ đúng miệng người nói.

### 3.2. Template B — Chia 2 Khung Ngang hoặc Chéo (Two-Panel Dynamic Split)
- **Áp dụng cho các trang:** `01, 02, 07, 09, 10, 15, 17, 19, 24, 25` (10 trang).
- **Tọa độ Khung:**
  - **Khung Trên (Upper Panel):** Phủ từ đỉnh trang `Y = -3mm` xuống `Y = 128mm` (hoặc cắt chéo từ `Y = 122mm` bên trái xuống `Y = 134mm` bên phải). Khung dẫn truyện giấy cổ nằm đè lên phần đỉnh của Khung Trên (`Y = 8mm..46mm`).
  - **Đường Rãnh Phân Cách (Panel Gutter):** Đường viền trắng kẹp giữa 2 nét mực đen, độ dày tổng cộng `3.5 mm` (`41 px`), nghiêng góc `0°` (ngang) hoặc `5°` (chéo động).
  - **Khung Dưới (Lower Panel):** Phủ từ `Y = 131.5mm` xuống đáy tràn lề `Y = 243mm`.

### 3.3. Template C — Đa Khung & Khung Phóng Cận Cảnh Hình Tròn (Multi-Panel & Circular Inset Zoom)
- **Áp dụng cho các trang:** `03, 05, 12, 21` (4 trang).
- **Tọa độ Khung:**
  - Chia thành 1 khung lớn trên (`Y = -3mm..135mm`) và 2 khung nhỏ dưới chia đôi theo chiều dọc tại `X = 95mm`, **HOẶC** đặt một **Khung Tròn Phóng Cận Cảnh (Circular Inset Zoom)** đường kính `68 mm` (`803 px`), tâm tại `(X = 48mm, Y = 115mm)`, có viền kép Trắng (`2.5mm`) + Đen (`1mm`) giống hệt Trang 11 của bộ mẫu *An Dương Vương*.

## 4. Thông số Bóng Thoại (Speech Bubbles) & Số Trang (Page Number Badge)
- **Bóng Thoại (Speech Bubble):**
  - Hình elip bo tròn hoặc đám mây nối đôi, nền Trắng ngà (`#FFFFFF`), viền mực đen dày `0.8mm` (`9px`).
  - Cỡ chữ thoại: `10.5 pt – 11.5 pt`, màu Đen (`#111827`), các tiếng hô lớn (như *"TRẢM THỦ!"*, *"QUYẾT ĐÁNH GIẶC TÔ ĐỊNH!"*) dùng cỡ `13pt` in hoa màu Đỏ Son (`#C81E1E`).
- **Số Trang (Folio):**
  - Đặt ở góc dưới ngoài (`X = 12mm` cho trang chẵn / `X = 178mm` cho trang lẻ, `Y = 228mm`), nằm trong một vòng tròn nhỏ họa tiết mặt trời trống đồng đường kính `8mm`, chữ số màu vàng kim trên nền đỏ sẫm.
