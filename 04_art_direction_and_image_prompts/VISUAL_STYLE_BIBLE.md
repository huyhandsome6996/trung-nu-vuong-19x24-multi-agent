# CẨM NANG CHỈ ĐẠO MỸ THUẬT (VISUAL STYLE BIBLE: ANCIENT VIETNAMESE HEROIC FAIRY TALE)

## 1. Phân tích ADN Phong cách từ 22 Ảnh Mẫu `.jpg` & Định hướng Lớp 8–10
Qua phân tích 22 file `.jpg` mẫu (*Truyền thuyết An Dương Vương*), phong cách mỹ thuật của dự án được định danh chính xác là:
> **"Traditional Vietnamese Historical Comic & Fairy-Tale Illustration (Detailed Black Ink Cross-Hatching + Textured Watercolor & Colored-Pencil Wash, Semi-Realistic Heroic Proportions for Ages 13–16)"**

### 1.1. Đặc trưng Nét vẽ (Linework & Shading)
- **Đường viền chính (Contour Lines):** Nét bút sắt mực đen (`#111111`) rõ ràng, sắc nét, phân tách rành mạch từng nhân vật, từng viên gạch thành trì, từng con sóng và từng chiếc lông vũ trên mũ Lạc Hầu.
- **Đan nét tạo khối (Cross-Hatching Texture):** Vùng bóng đổ trên vách đá, thân cây cổ thụ, nếp áo choàng và giáp trụ không tô bệt mà dùng các nét gạch chéo tỉ mỉ như tranh khắc gỗ truyền thống kết hợp truyện tranh lịch sử Á Đông cao cấp.
- **Tỷ lệ giải phẫu nhân vật (Character Proportions):** Tỷ lệ `7.5 – 8 đầu` chuẩn mực cho học sinh lớp 8–10 (13–16 tuổi):
  - Tuyệt đối **KHÔNG** vẽ kiểu chibi trẻ mẫu giáo, cũng **KHÔNG** vẽ kiểu 3D bóng mượt hiện đại hay anime mắt quá to sai lệch lịch sử.
  - Gương mặt nam anh hùng (Thi Sách, Đinh Lương, Trưng Định, Nguyễn Huyền, Phùng Lực Công) góc cạnh, sống mũi cao, mày rậm, ánh mắt cương nghị.
  - Gương mặt nữ anh hùng (Trưng Trắc, Trưng Nhị, Thánh Thiên, Phùng Thị Chính) thanh tú, đoan trang nhưng toát lên **uy khí lẫm liệt của bậc nữ tướng cầm quân**.

### 1.2. Hệ Bảng màu Hào Hùng – Tự Hào Dân Tộc (Heroic Color Palette)

| Tên Màu Chủ Đạo | Mã Màu HEX | Giá trị CMYK (Chuẩn In 19×24cm) | Ý nghĩa Thị giác & Ứng dụng trong Tranh |
| :--- | :--- | :--- | :--- |
| **Đỏ Son Lạc Việt (Lac Viet Crimson)** | `#B91C1C` / `#C81E1E` | `C:15 M:95 Y:90 K:5` | Màu áo choàng chiến trận của Hai Bà Trưng, cờ đại nghĩa, trường bào Lạc Hầu của Thi Sách, và màu chữ nhấn trong Khung dẫn truyện. |
| **Vàng Đồng Ngọc Lũ (Dong Son Bronze Gold)** | `#D97706` / `#F59E0B` | `C:10 M:45 Y:95 K:0` | Màu trống đồng, hổ phù trước ngực Thi Sách, giáp đồng mạ vàng, mũ lông vũ vua Hùng, ánh hào quang rồng vàng khổng tước. |
| **Trắng Tang Bào Uy Nghiêm (Sacred Mourning White)** | `#F8FAFC` / `#E2E8F0` | `C:3 M:2 Y:2 K:0` | Bộ trang phục trắng và dải khăn tang trắng của Trưng Trắc tại Cổ Lôi sơn trang và của nữ tướng Thánh Thiên tại núi Phượng Hoàng. |
| **Lam Thẫm Sông Nhị Hà (Nhi Ha River Deep Blue)** | `#1E3A8A` / `#1D4ED8` | `C:95 M:75 Y:5 K:10` | Màu nước sông Nhị Hà, cửa Hát Môn, bến Lục Đầu Giang, cửa biển Đằng Giang và bầu trời đêm Cổ Lôi. |
| **Lục Rừng Đại Ngàn (Phong Chau Emerald)** | `#15803D` / `#166534` | `C:85 M:25 Y:95 K:10` | Màu rừng núi Mê Linh, dãy núi Phượng Hoàng, khe Mãng Xà, vườn nhãn Chu Diên. |
| **Đen Khói Lửa & Sắt Thép (Han Iron & Smoke)** | `#1F2937` / `#111827` | `C:75 M:65 Y:60 K:80` | Màu giáp sắt và quan phục u ám của quân đô hộ Đông Hán (Tô Định, Tào Quyền, Mã Tắc, Lữ Thạch). |

## 2. Chuỗi Master Style Prompt (Dùng chung cho Mọi Lần Gọi Công Cụ Sinh Ảnh)

Khi gọi bất kỳ công cụ sinh ảnh nào, `AGENT-04` luôn gắn **Master Style Prefix** và **Master Style Suffix** sau đây vào câu lệnh:

- **Master Style Prefix:**
  ```text
  Epic Vietnamese historical fairy-tale comic illustration in traditional hand-drawn ink linework with detailed cross-hatching and rich watercolor colored-pencil grain texture, semi-realistic heroic character proportions for young adult readers (grades 8-10), vibrant warm bronze-gold and crimson-red palette contrasting with deep indigo blues and lush forest greens.
  ```
- **Master Style Suffix (Đảm bảo bố cục 19×24cm và chừa chỗ đặt Khung dẫn truyện):**
  ```text
  Vertical book page composition (aspect ratio 4:5 matching 19x24cm print format), leave generous open sky or atmospheric negative space in the top 20% of the frame for a narration scroll box, dramatic cinematic lighting, authentic 1st-century AD Lac Viet Dong Son bronze drums, feathered headdresses, and scale armor details, clean composition, text-free, no labels, no speech bubbles, no watermarks.
  ```
