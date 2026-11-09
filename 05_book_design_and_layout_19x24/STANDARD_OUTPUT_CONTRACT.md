---

> Trạng thái hiện hành theo [workflow A–Z](../10_agent_workflow/WORKFLOW_A_TO_Z.md): QA pass là kiểm của agent; USER_APPROVED cần xác nhận thực của chủ dự án; PRINT_READY cần thông số và kiểm file in.
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
book_size: "190mm x 240mm (Bleed: 196mm x 246mm @ 300 DPI)"
target_audience: "Học sinh Lớp 8 - Lớp 10 (13-16 tuổi)"
compartment: "05_book_design_and_layout_19x24"
agent_author: "ChatGPT / Lead Agent (onboarding và rà soát QA)"
status: "IN_REVIEW"
source_grounding: "59 file tại commit 65c2e5a7cf71a1344be7f916c9b675e4325d31c8 và chỉ dẫn trực tiếp ngày 2026-11-09"
review_date: "2026-11-09"
timezone: "Asia/Ho_Chi_Minh"
---

# Form đầu ra áp dụng sau onboarding

Tổng hợp chỉ dẫn trực tiếp của chủ dự án ngày 09/11/2026. Chỉ khóa các yêu cầu không mâu thuẫn; các điểm cần quyết định nằm ở [sổ vấn đề](../06_qa_validation_and_delivery/ONBOARDING_ISSUES.md). Đây không phải xác nhận đã có sản phẩm đạt chuẩn in.

## 1. Hình học trang

| Hạng mục | Chuẩn |
| --- | --- |
| Trim | 190×240 mm; raster mục tiêu 2244×2835 px @300 DPI. |
| Bleed | 3 mm bốn cạnh; tổng 196×246 mm; raster 2315×2906 px @300 DPI. |
| Hệ tọa độ | Gốc trim ở góc trên trái (0,0). Bleed từ X=−3..193, Y=−3..243 mm. Trên canvas bleed, tọa độ trim phải dịch +3 mm cả hai trục. |
| Safe zone | Vùng 162×212 mm theo master: trong 16 mm, ngoài 12 mm, trên/dưới 14 mm; đảo lề trong/ngoài theo trang trái/phải. Tọa độ khung giấy cổ hiện chưa tương thích hoàn toàn. |
| Tỷ lệ sinh | Ưu tiên 4:5; ảnh 3:4 chỉ dùng khi chừa đủ biên để điều chỉnh. Không kéo méo nhân vật. |

Chuyển mm→px dùng công thức `mm / 25.4 × 300`. Lấy mm làm chuẩn vật lý PDF; pixel đích làm tròn theo quy chuẩn trên. DPI metadata không tự tạo thêm chi tiết; phải kiểm chất lượng ảnh gốc và ảnh sau xử lý.

## 2. Hai lớp sản xuất

1. **Raw illustration:** tranh sạch chữ, `text-free, no labels, no speech bubbles, no watermarks`; khoảng 20% vùng thoáng đỉnh trang ruột. Trang có mũ, kiếm giơ cao phải kiểm cả đạo cụ có bị khung chữ che hay không. Bìa trước theo vùng trống tiêu đề riêng; bìa sau theo vùng tóm tắt/ISBN riêng.
2. **Typesetting:** thêm toàn bộ chữ bằng font hỗ trợ tiếng Việt. Bài vị, mật thư, tên trên cờ nếu cần đọc cũng thuộc lớp chữ; không giao AI tự viết. Lưu tranh gốc riêng, không ghi đè bởi bản ghép.

## 3. Khung dẫn truyện

- Tọa độ được yêu cầu: **X=11..179 mm, Y=8..48 mm** trên trim; không tự sửa trong phiên onboarding. Cần giải quyết LAYOUT-01 trước khi coi là khuôn in đã khóa.
- Khung giấy cổ viền mực đen, mép rách tự nhiên, nền #FFFBEB → #F59E0B; không đặt lên mặt nhân vật.
- Chữ căn giữa, mục tiêu 3–5 dòng / 35–65 đơn vị cách trắng. Phải đo lại sau chọn font và ghép chữ thực.
- Chữ thường #1A1A1A; **tất cả cụm trong dấu sao đôi ở trường lời dẫn** render đỏ #C81E1E và in đậm. Không tô đỏ cả tiêu đề, nhãn trường hoặc mọi chữ đậm trong tài liệu nguồn.
- Giữ đúng nội dung chữ được chốt; không tự bớt từ khóa để đạt tỷ lệ 20–35%. Nếu quá nhiều cụm, đưa về bước biên tập.

## 4. Template và bìa

| Template | Trang theo storyboard hiện tại |
| --- | --- |
| A — toàn trang | 04, 06, 08, 11, 13, 14, 16, 18, 20, 22, 23, 26, 27, 28 |
| B — hai khung ngang/chéo | 01, 02, 07, 09, 10, 15, 17, 19, 24, 25 |
| C — đa khung / zoom tròn | 03, 05, 12, 21 |

Bìa trước: tít dẫn trên dải lụa vàng → đại tự TRƯNG NỮ VƯƠNG đỏ, viền theo mẫu được duyệt → phụ đề khung mây → tên nhân vật chính. Chi tiết viền trong master và prompt người dùng chưa hoàn toàn cùng cách mô tả, cần xem bản mẫu khi duyệt bìa.

Bìa sau: lư hương đồng, 99 cờ ngũ sắc bên Nhị Hà, khung tóm tắt và ô ISBN. Ô ISBN chỉ là vùng dành chỗ cho đến khi có thông tin thật. Bìa rời 196×246 mm khác panel 193×246 mm trong bìa trải; không dùng lẫn. Chưa chốt gáy từ con số ước tính.

## 5. Đồng nhất nhân vật và bàn giao

- **10 bảng nhân vật phải được tạo và chủ dự án chốt trước trang 01–28.** Các bảng nhóm vẫn tính là một bảng nhưng phải có tên/mã từng người.
- Dùng đúng file ảnh đã duyệt làm tham chiếu cho trang sau; ghi phiên bản và nguồn trong metadata, không chỉ dùng lại prompt chữ.
- Đặt tên theo `06_qa_validation_and_delivery/GITHUB_COLLABORATION_PROTOCOL.md`.
- Mỗi sản phẩm đi kèm trạng thái DRAFT/IN_REVIEW/READY_FOR_PRODUCTION/APPROVED, nguồn, prompt, tham chiếu, thông số và kiểm tra đã thực hiện. Chỉ đạt APPROVED sau kiểm cả nội dung, mỹ thuật và chế bản.
- Tiến độ sau nhiệm vụ thiết kế: **30 bảng hình hiện hành,17 bảng casting cho41 hồ sơ nhân vật; chưa dựng28 trang ruột hoặc PDF in**. Quy chuẩn nhân vật và layout hiện hành tại [Ngăn09](../09_design_system/00_READ_FIRST.md).

- Ngoại lệ chế bản đã ghi cho chuẩn v1: mép giấy cổ giữ tọa độ gốc là trang trí; chữ trong X18..172/Y14..43mm. Dùng `09_design_system/layout_components/layout_tokens.json` và SOURCE_DECISIONS khi dựng.

- Ngoại lệ chế bản đã ghi cho chuẩn v1: mép giấy cổ giữ tọa độ gốc là trang trí; chữ trong X18..172/Y14..43mm. Dùng `09_design_system/layout_components/layout_tokens.json` và SOURCE_DECISIONS khi dựng.
