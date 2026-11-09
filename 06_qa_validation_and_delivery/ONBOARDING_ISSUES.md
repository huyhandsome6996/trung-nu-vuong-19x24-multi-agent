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

# Các vấn đề phát hiện khi nạp dự án

Bảng này ghi chênh lệch có dẫn nguồn. **Chưa sửa nguyên tác, storyboard hay Character Bible trong phiên onboarding.** Không diễn giải bản tiểu thuyết là bằng chứng chính sử. Các mã dưới đây dùng để theo dõi, không phải phê duyệt sửa đổi.

| Mã | Vấn đề và bằng chứng | Ảnh hưởng / cách xử lý tiếp theo | Trạng thái |
| --- | --- | --- | --- |
| CHAR-01 | `02/CHARACTER_BIBLE_AND_FACTIONS.md` mục 1.2 và `04/CHARACTER_DESIGN_PROMPTS.md` mục 7 gọi Đô Năng Tế và Cẩm Nương là hai nữ sư phụ. Scan PDF 32 / sách 243 mô tả Đô sư phụ vuốt chòm râu; scan PDF 30 / sách 241 cũng nói về giao tình và hôn sự với ái nữ của Lê Đạo. | **Chặn khóa sheet 07** theo prompt hiện tại. Đối chiếu crop scan và thống nhất hồ sơ từng người trước khi tạo ảnh; không đổi cả hai nhân vật chỉ từ một chi tiết. | Mở — cần quyết định hồ sơ. |
| CHAR-02 | Trưng Nhị trong Bible và prompt sheet 02 mặc lam sẫm, trong prompt bìa và trang 17 cả hai chị em cùng giáp vàng/áo choàng đỏ. | Khóa rõ màu áo trong, giáp và áo choàng ở từng giai đoạn; không làm mất nhận diện lam sẫm của Trưng Nhị khi đưa vào cảnh đông người. | Mở. |
| CHAR-03 | Gate 2 trong `AGENT_ORCHESTRATION_GUIDE.md` mô tả “10 nhân vật”; thư viện thực có 10 prompt **bảng**, nhiều bảng chứa nhóm 2–3 người. Mã Tắc và Lục Hiến chưa có thiết kế sheet riêng trong danh sách dù xuất hiện nhiều. | Tính theo **10 bảng** đúng yêu cầu chủ dự án; lập danh sách từng người trong mỗi bảng. Bổ sung mô tả/tham chiếu cho nhân vật còn thiếu trước các trang liên quan. | Mở. |
| SRC-01 | Scan PDF 06 / sách 217 viết rồng vàng biến hóa thành một đôi khổng tước. Bản phân tích sâu, hướng dẫn giọng văn, storyboard và prompt trang 01 lại đổi chiều thành đôi khổng tước hóa rồng vàng. | Sửa đồng bộ các lớp liên quan sau quyết định biên tập; không sinh trang 01 từ prompt hiện tại mà coi là đã bám nguồn. | Mở — bằng chứng scan có sẵn. |
| SRC-02 | `PDF_CONTENT_DEEP_ANALYSIS.md` mục phần II.1 đặt hành quyết Nguyễn Huyền–Trưng Định sau hơn 10 ngày trong Hồi 8. Scan PDF 26–29 / sách 237–240 đã kể pháp trường trong Hồi 7; PDF 35 / sách 246 hồi cố việc bêu đầu sau hơn 10 ngày. Storyboard trang 11 theo mạch Hồi 7. | Khi tóm tắt theo storyboard dùng mạch trang 11; cần sửa bản phân tích sâu, không lặp lại hành quyết ở Hồi 8. | Mở. |
| SRC-03 | Scan PDF 18–19 / sách 229–230 nói bắn mươi phát / mười mũi liên tiếp. Bảng chú giải PDF 18 ghi ba mươi mũi; mô tả và prompt trang 07 lại vẽ ba mũi đồng thời. | Thống nhất mười phát liên tiếp hoặc ghi rõ là dụng ý chuyển thể; chưa vẽ ba mũi đồng thời dưới nhãn chi tiết nguyên tác. | Mở. |
| SRC-04 | Scan PDF 39 / sách 250 ghi “tám thớt voi đực trắng ngà cong vút”; bảng chú giải, phân tích và storyboard trang 16 ghi “78” hoặc “bảy mươi tám”; prompt dùng 78. | Đây là chênh lệch đọc số từ scan. Cần đối chiếu crop và sửa đồng bộ trước đại cảnh Hát Môn; không biến màu ngà thành toàn thân voi trắng. | Mở. |
| SCOPE-01 | Hồi 8 trong scan kết tại mệnh lệnh Thánh Thiên ở PDF 58 / sách 269. Storyboard trang 27–28 thêm tiến đánh Luy Lâu, 65 thành, lên ngôi và tưởng niệm hiện đại. | Đánh dấu **đoạn kết mở rộng**; cần nguồn bổ sung và quyết định biên tập hoặc viết lại phạm vi kết thúc. Chưa tuyên bố toàn bộ 28 trang có căn cứ trực tiếp từ 58 trang. | Mở. |
| LAYOUT-01 | Khung dẫn X=11..179, Y=8..48 mm trong `PAGE_LAYOUT_TEMPLATES_19x24.md` nằm ngoài vùng an toàn 162×212 mm / lề trong 16, ngoài 12, trên-dưới 14 mm của master specs. | Hai điều kiện “toàn khung trong vùng an toàn” và tọa độ cố định không thể cùng đúng. Cần chọn: giữ mép giấy cổ như phần trang trí với chữ nằm sâu bên trong, hoặc dời/thu khung. Chưa tự thay tọa độ chủ dự án đã nêu. | Mở — chặn chốt khuôn chế bản. |
| LAYOUT-02 | Lời dẫn trang 06,12,16,17,19,20,24–28 vượt 65 đơn vị cách trắng. 11 trang có hơn 5 cụm in đậm, 14 trang vượt tỷ lệ đỏ 35%. Xem bảng kiểm định lượng. | Kiểm tra biên tập và bản dựng 3–5 dòng; số “52 từ”, “58 từ” trong nhãn kịch bản chưa phải số đo đáng tin. Không tự bỏ dấu **...** khi ghép chữ. | Mở. |
| LAYOUT-03 | CSS minh họa `@page` và `.story-page` chỉ có 190×240 mm, overflow hidden, không dựng trang 196×246 mm hoặc hộp Trim/Bleed. Folio CSS bottom 6/right 8 mm khác tọa độ folio trong tài liệu; hình tròn đường kính 8 mm còn có thể vượt safe zone ngay cả khi tâm gần mép. | Ngăn 05 chưa có pipeline in hoàn chỉnh; cần xây dựng và đo hộp PDF, ảnh raster, font nhúng, folio chẵn/lẻ ở bước chế bản. Không gọi đoạn CSS này là file in sẵn. | Mở. |
| PRINT-01 | Master specs có gáy 3, 3.5 và 5 mm ở các vị trí khác nhau; quy cách đóng cuốn chưa được chốt. | Gáy và trải bìa 389.5×246 mm chỉ là giả định theo gáy 3.5 mm. Chốt với thông số giấy/đóng cuốn trước xuất bìa cuối. | Mở. |
| PRINT-02 | README ngăn 03 nói 32 trang gồm 28 truyện + 4 bìa/phụ lục; `BOOK_STRUCTURE_AND_PACING.md` định nghĩa 32 ruột + bìa riêng. | Dùng cấu trúc chi tiết làm căn cứ dự kiến: 32 ruột = 2 mở đầu + 28 truyện + 2 phụ lục; cần viết đủ trang phụ và kiểm tra sơ đồ đóng cuốn. | Mở. |
| PRINT-03 | Kích thước pixel làm tròn độc lập của khổ trim và bleed có thể lệch 1 px khi crop bằng viền cố định. Ví dụ 2315−2244=71 px; Y chênh cũng 71 px. | Giữ mm là chuẩn hình học PDF. Khi crop raster phải ghi rõ chia 35/36 px hai phía và kiểm tra đầu ra, không khẳng định viền 3 mm luôn là số px nguyên bằng nhau. | Đã ghi nguyên tắc, chưa có file in để kiểm. |
| EDIT-01 | Trang 18 ghi “trích nguyên văn” nhưng câu thoại đã rút gọn/chuyển lời kết của hịch. Tuổi trong Bible và một số danh xưng là lựa chọn thiết kế, không được scan chứng minh đầy đủ. | Gắn nhãn “phỏng theo/rút gọn” khi thích hợp; tách dữ kiện tác phẩm, huyền sử và bổ sung lịch sử khi soạn phụ lục. | Mở. |

## Cách đọc đường dẫn trong bảng

`01/`, `02/`, `03/`, `04/`, `05/`, `06/` là viết tắt các ngăn cùng số thứ tự. Tên file cụ thể là định danh tra cứu; [manifest](SOURCE_INVENTORY_BASELINE.md) có đường dẫn đầy đủ. Ảnh đối chiếu nằm tại `07_reference_assets/pdf_annotated_contact_sheets/`.

## Thứ tự giải quyết

1. Trước sheet: CHAR-01, CHAR-02, CHAR-03.
2. Trước trang cụ thể: SRC-01…04 và SCOPE-01, kiểm lời dẫn/thoại.
3. Trước chế bản: LAYOUT-01…03, PRINT-01…03, EDIT-01 và các nguồn bổ sung.

Không có ảnh nào được sinh trong quá trình phát hiện các mục này.
