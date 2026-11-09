---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
book_size: "190mm x 240mm (Bleed: 196mm x 246mm @ 300 DPI)"
target_audience: "Học sinh Lớp 8 - Lớp 10 (13-16 tuổi)"
compartment: "06_qa_validation_and_delivery"
agent_author: "ChatGPT / Lead Agent (onboarding và rà soát QA)"
status: "IN_REVIEW"
source_grounding: "59 file tại commit 65c2e5a7cf71a1344be7f916c9b675e4325d31c8 và chỉ dẫn trực tiếp ngày 2026-11-09"
review_date: "2026-11-09"
timezone: "Asia/Ho_Chi_Minh"
---

# Báo cáo sẵn sàng dự án — 09/11/2026

## 1. Trạng thái truy cập repo

- Đã clone thành công repo `huyhandsome6996/trung-nu-vuong-19x24-multi-agent`.
- Đã kiểm kê đúng **59 file gốc**, gồm **26 Markdown + 32 JPG + 1 .gitignore**, đủ thư mục gốc và **7 ngăn 01–07**. Đây là số tại commit nền, không phải tổng file sau đợt bổ sung này.
- Đã đọc toàn bộ 26 file `.md` theo thứ tự gốc → 01/07 → 02 → 03 → 04 → 05/06; đã đọc `.gitignore` và mở xem trực tiếp **10 contact sheets** cùng **22 ảnh mẫu** từ bìa 00 đến trang 21.
- 10 contact sheets bao phủ PDF 01–58 / trang sách 212–269. **PDF gốc không nằm trong 59 file**; việc đối chiếu nguyên tác ở phiên này dựa vào ảnh scan tổng hợp, không tuyên bố đã mở PDF gốc hoặc xác minh chính sử độc lập.
- [Kiểm kê có SHA-256](SOURCE_INVENTORY_BASELINE.md) lưu dấu vết từng file; [bảng kiểm onboarding](ONBOARDING_AUDIT_2026-11-09.md) ghi kết quả định lượng.

## 2. Mục tiêu và mạch truyện 28 trang

Chuyển thể trích đoạn Hồi 7–8 của tiểu thuyết *Trưng Nữ Vương* thành sách tranh cổ tích lịch sử hào hùng cho lớp 8–10, khổ 19×24 cm. Lời kể cô đọng, nhấn khí tiết và tinh thần đoàn kết; yếu tố huyền sử phải được nhận diện là truyền thuyết hoặc cách kể của tác phẩm. Minh họa nét mực đen đan chéo, màu nước/chì màu có hạt, tương phản đỏ son–vàng đồng với lam thẫm–lục rừng; nhân vật bán hiện thực, cảnh hy sinh biểu đạt bi tráng.

| Trang | Mạch truyện theo storyboard hiện có |
| --- | --- |
| 01–02 | Văn Lang, giấc mộng dòng họ Phùng; Phùng Lực Công / Thánh Đóng và Tản Viên Sơn Thánh. |
| 03–05 | Âm mưu Tô Định tại Luy Lâu; Thi Sách, Đinh Lương–Phùng Thị Chính ở Chu Diên; mật thư của Trưng Trắc. |
| 06–09 | Thi Sách khoác trường bào Lạc Hầu, giao chiến Lữ Thạch; Thi Sách và Đinh Lương hy sinh tại Chu Diên. |
| 10–14 | Tin dữ ở Cổ Lôi; khí tiết Nguyễn Huyền–Trưng Định tại Luy Lâu; ba huyện lệnh tụ nghĩa; Trưng Trắc khoác tang bào, tuyên thệ. |
| 15–18 | Luy Lâu hoảng loạn; đại cảnh Hát Môn, suy tôn Trưng Trắc làm chủ tướng, đọc hịch bên sông Nhị Hà. |
| 19–23 | Huyền tích huyết sâm, Thánh Thiên tụ nghĩa bảy tộc; sa bàn và kế nhử giặc; thuyền Tào Quyền–Lục Hiến cập bến. |
| 24–26 | Phục kích khe Mãng Xà, đoạt thuyền, bao vây nhà gỗ và Thánh Thiên tuyên án Tào Quyền. |
| 27–28 | Đoạn kết mở rộng: tiến đánh Luy Lâu, 65 thành, Trưng Nữ Vương và tưởng niệm ngày nay. **Phần này vượt phạm vi 58 trang scan, cần nguồn bổ sung hoặc quyết định biên tập.** |

Theo file cấu trúc sách: **32 trang ruột = 28 trang truyện + 4 trang dẫn nhập/phụ lục**, bìa tính riêng. Một số README mô tả khác; chưa coi nội dung phụ trợ là đã viết xong.

## 3. Form tiêu chuẩn đầu ra

| Thành phần | Yêu cầu áp dụng |
| --- | --- |
| Thành phẩm | 190×240 mm; raster đích 2244×2835 px @300 DPI. |
| Tràn lề | 3 mm mỗi cạnh → 196×246 mm; raster đích 2315×2906 px @300 DPI. |
| An toàn | Mục tiêu 162×212 mm, lề trong/ngoài và trên/dưới theo đặc tả; xung đột với tọa độ khung giấy cổ đã ghi trong sổ vấn đề. |
| Tranh nền | 4:5 ưu tiên; 3:4 phải có phương án bù/cắt biên; dành khoảng 20% đỉnh trang thoáng, không chữ, không bóng thoại, không watermark. |
| Chế bản chữ | Lớp riêng: giấy cổ viền mực, nền #FFFBEB → #F59E0B; chữ Việt căn giữa, đen #1A1A1A; mọi cụm **...** trong lời dẫn render đỏ #C81E1E, in đậm. |
| Khung dẫn | Tọa độ yêu cầu X=11..179 mm, Y=8..48 mm; 3–5 dòng, mục tiêu 35–65 đơn vị cách trắng; cần kiểm tra tràn chữ và vùng an toàn ở bản dựng. |
| Template | A: toàn trang; B: hai khung ngang/chéo; C: đa khung hoặc zoom tròn. Phân trang: **A=14, B=10, C=4**. |
| Bìa | Trước: 4 tầng chữ; sau: lư hương, cờ ngũ sắc, tóm tắt và ô ISBN. Gáy chờ thông số đóng cuốn; không tự tạo ISBN. |
| Nhân vật | Tạo và được chủ dự án chốt **10 bảng tham chiếu** trước khi dùng cho trang 01–28; ghi tên file/phiên bản và người duyệt. |

Chi tiết tại [STANDARD_OUTPUT_CONTRACT.md](../05_book_design_and_layout_19x24/STANDARD_OUTPUT_CONTRACT.md). Hiện ngăn 05 chỉ có đặc tả và đoạn mã trong Markdown, **chưa có chương trình dàn trang hoàn chỉnh để chạy ngay**.

## 4. Đề xuất bước bắt đầu

**Đề xuất: khóa 10 Character Sheets trước**, bắt đầu bằng giải quyết hồ sơ Đô Năng Tế và khóa màu nhận diện Trưng Nhị. Chưa có ảnh nhân vật được tạo hoặc phê duyệt.

Chờ chủ dự án chọn: **(A) Khóa 10 bảng nhân vật** hoặc **(B) Ưu tiên bìa và trang 01**. Nếu chọn B, vẫn cần khóa các nhân vật xuất hiện trước khi làm tranh thành phẩm; không bỏ quy chuẩn đồng nhất nhân vật.

**Kết luận trạng thái:** Onboarding hoàn tất; sẵn sàng bước khóa hồ sơ. **Chưa đủ điều kiện tự xác nhận toàn bộ dự án READY_FOR_PRODUCTION hoặc APPROVED**, do các mục ở [ONBOARDING_ISSUES.md](ONBOARDING_ISSUES.md). Không sinh ảnh trong phiên onboarding này.
