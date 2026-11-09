---
project: "TRƯNG NỮ VƯƠNG"
book_size: "190x240mm; bleed196x246mm @300DPI for final pages"
target_audience: "Lớp8–10 (13–16 tuổi)"
agent_author: "ChatGPT / design production and QA"
status: "DESIGN_BASELINE"
user_approved: false
date: "2026-11-09"
---

# Báo cáo kiểm bộ thiết kế v1

## Phạm vi hoàn thành

- **30 bảng hình hiện hành:** 17 casting +1 góc quay/biểu cảm +5 bối cảnh +4 đạo cụ +1 quân đội +1 động vật +1 mặt tộc trưởng.
- **41 hồ sơ nhân vật**, bao gồm người thực sự xuất hiện và người chỉ được nhắc trong nguồn; **24 mã mặt tập thể** không bịa tên riêng.
- **14 bối cảnh**,36 mã đạo cụ/phương tiện và4 động vật; ma trận phụ thuộc cho đủ28 trang.
- 7 SVG thành phần/khuôn và1 JSON thông số layout; prompt, registry, metadata và hướng dẫn cho agent.
- Phiên này có29 thiết kế ảnh bổ sung và2 lần sửa mục tiêu; cùng1 ảnh Trưng Trắc đã có, repo giữ32 PNG (30 hiện hành +2 bản cũ) và30 preview WebP. Không tính preview là tranh mới.

## Kết quả quan sát hình

| Nhóm | Kiểm đã thực hiện | Giới hạn |
| --- | --- | --- |
| CHAR01–04 | Trưng Trắc hai phục trang; Trưng Nhị nền lam; Thi Sách tía, huy hiệu hổ, ngựa đen; Thánh Thiên lục/khăn tang/giày đốm. | Mặt cùng người được đánh giá bằng quan sát, không có thước đo nhận diện tự động. Các nữ tướng có nét họa phong gần nhau, khi làm cận cảnh phải giữ hồ sơ riêng. |
| CHAR05–09 | Đúng cặp/ba người, râu/tóc/màu/đạo cụ phân biệt; Đô Năng Tế nam có râu; Cẩm Nương nữ; Lê Đạo có chim ưng; Thánh Đóng và Tản Viên riêng. | Một số bảng có thêm mặt/góc nhỏ ngoài yêu cầu, không hiểu là có thêm nhân vật. |
| CHAR10–17 | Bộ ba phản diện, Mã Tắc–Lục Hiến, gia đình trong huyền tích và các vai phụ có mã/vị trí; khác chủng loại giáp và dáng. | Người chỉ được nhắc là thiết kế dự phòng, không tự cho xuất hiện trong28 trang. |
| TURN01 | Trước/nghiêng/sau và4 biểu cảm Trưng Trắc giữ cấu trúc nhận diện tổng thể. | Chi tiết lông/mũ/hoa văn có thể lệch nhỏ giữa góc; lấy ảnh chính làm chuẩn cận cảnh, không tuyên bố đồng nhất pixel100%. |
| ENV01–05 | Chất liệu gỗ/đá, rừng/sông, cổng/sân đọc được; ENV03 có8 voi xám ngà trắng; ENV05 có nhãn nội dung kết biểu tượng trong hồ sơ. | Bảng không có đủ17 trống/99 cờ/160 thuyền; cần triển khai số lượng khi vẽ trang. Cổng/kiến trúc là lựa chọn mỹ thuật, không phục dựng khảo cổ hoặc địa điểm thật. |
| PROP01–02 | Kiếm/cung/nỏ/thương phân biệt; hổ phù ngực khác tín vật cầm tay; lư có nắp khác đỉnh mở; bài vị/thẻ tre không có chữ AI. | Tỷ lệ vật thể giữa ô không dùng làm thước đo; kích thước lấy hồ sơ. |
| PROP03 v002 | Đồng nhất huyết sâm đỏ với ENV03; đủ đồ thuốc/sa bàn/đạo cụ sân. | Gốm/hoa văn là concept, chưa kiểm định niên đại khảo cổ từng vật. |
| PROP04 v002 | Đã loại đèn kính, thay đèn dầu đất nung và vòng dây da; giữ thuyền/bành voi và rồng hóa đôi khổng tước. | Dây buộc/cơ chế phương tiện cần kiểm lại theo góc vẽ trang; không gọi đây là bản vẽ chế tạo. |
| ARMY01 / ANIMAL01 | 8 mẫu trang phục/quần chúng; ngựa đen/chim câu trắng/chim ưng đen-nâu/voi xám; PH03 định danh. | Trang phục quần chúng là mẫu, không sao chép cùng mặt cho toàn quân. |
| CHIEFS01 | Đếm được24 ô theo4×6; PH03 hàng4/cột2; màu khăn trong registry đã sửa theo ảnh thực tế. | Một số gương mặt có nét giống nhau trong họa phong; dùng mã ô và đặc điểm râu/khăn để giữ liên tục. |

## Kiểm kỹ thuật

- Tất cả PNG hiện hành mở/giải mã được, ghi kích thước thật và SHA-256 trong JSON; không đổi DPI để giả tăng chi tiết.
- Validator kiểm41 profile,24 face IDs,29 jobs mới đều GENERATED,14 cảnh,36 props,4 động vật và28 trang có mã hợp lệ.
- SVG đã được parse XML; khuôn A/B/C và bìa được render bằng Inkscape và xem lại bằng ảnh. Mép giấy cổ là trang trí, vùng chữ riêng đã ghi rõ.
- Album có30 ảnh preview nội bộ và link tới bản gốc; HTML không dùng tài nguyên mạng ngoài. Đã kiểm đường dẫn và cú pháp JS. Chưa chạy kiểm thị giác HTML bằng Chromium vì môi trường thiếu browser binary; không ghi giả là đã kiểm browser.
- Không chạy OCR hoặc kiểm định màu CMYK/ICC/font in; không phát hành PDF in trong nhiệm vụ này.

## Bản đang dùng và bản cũ

**PROP03_v002.png** và **PROP04_v002.png** là chuẩn hiện hành. Hai file v001 tương ứng giữ nguyên, metadata SUPERSEDED và có đường dẫn bản thay. Các bảng khác dùngv001. Không tự coi DESIGN_BASELINE là người dùng đã duyệt từng hình; chuẩn này được chọn theo ủy nhiệm thiết kế toàn bộ để agent tiếp tục bản nháp.

## Việc thuộc giai đoạn dựng truyện

Viết/soát lại lời dẫn vừa khuôn, xác minh nguồn đoạn kết27–28 nếu giữ các khẳng định lịch sử, chọn ảnh địa điểm thật nếu cần gọi tên một ngôi đền, sinh riêng từng tranh có đủ chi tiết, kiểm đồng nhất theo góc, ghép chữ Việt, font, bleed, ICC và gáy nhà in. **Không tuyên bố30 bảng thiết kế là30 trang truyện đã in xong.**

## Danh mục kích thước thật

| Bảng | File hiện hành | Pixel | Trạng thái |
| --- | --- | --- | --- |
| CHAR02 | `assets_generated/design_system/CHAR02_v001.png` | 1122×1402 | DESIGN_BASELINE |
| CHAR03 | `assets_generated/design_system/CHAR03_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR04 | `assets_generated/design_system/CHAR04_v001.png` | 1122×1402 | DESIGN_BASELINE |
| CHAR05 | `assets_generated/design_system/CHAR05_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR06 | `assets_generated/design_system/CHAR06_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR07 | `assets_generated/design_system/CHAR07_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR08 | `assets_generated/design_system/CHAR08_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR09 | `assets_generated/design_system/CHAR09_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR10 | `assets_generated/design_system/CHAR10_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR11 | `assets_generated/design_system/CHAR11_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR12 | `assets_generated/design_system/CHAR12_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR13 | `assets_generated/design_system/CHAR13_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR14 | `assets_generated/design_system/CHAR14_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR15 | `assets_generated/design_system/CHAR15_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR16 | `assets_generated/design_system/CHAR16_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHAR17 | `assets_generated/design_system/CHAR17_v001.png` | 1536×1024 | DESIGN_BASELINE |
| TURN01 | `assets_generated/design_system/TURN01_v001.png` | 1536×1024 | DESIGN_BASELINE |
| ENV01 | `assets_generated/design_system/ENV01_v001.png` | 1536×1024 | DESIGN_BASELINE |
| ENV02 | `assets_generated/design_system/ENV02_v001.png` | 1536×1024 | DESIGN_BASELINE |
| ENV03 | `assets_generated/design_system/ENV03_v001.png` | 1536×1024 | DESIGN_BASELINE |
| ENV04 | `assets_generated/design_system/ENV04_v001.png` | 1536×1024 | DESIGN_BASELINE |
| PROP01 | `assets_generated/design_system/PROP01_v001.png` | 1536×1024 | DESIGN_BASELINE |
| PROP02 | `assets_generated/design_system/PROP02_v001.png` | 1536×1024 | DESIGN_BASELINE |
| PROP03 | `assets_generated/design_system/PROP03_v002.png` | 1536×1024 | DESIGN_BASELINE |
| PROP04 | `assets_generated/design_system/PROP04_v002.png` | 1536×1024 | DESIGN_BASELINE |
| ARMY01 | `assets_generated/design_system/ARMY01_v001.png` | 1536×1024 | DESIGN_BASELINE |
| ANIMAL01 | `assets_generated/design_system/ANIMAL01_v001.png` | 1536×1024 | DESIGN_BASELINE |
| CHIEFS01 | `assets_generated/design_system/CHIEFS01_v001.png` | 1536×1024 | DESIGN_BASELINE |
| ENV05 | `assets_generated/design_system/ENV05_v001.png` | 1536×1024 | DESIGN_BASELINE |
