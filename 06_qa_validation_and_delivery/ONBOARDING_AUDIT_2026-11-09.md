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

# Kết quả kiểm tra onboarding — 09/11/2026

## Phạm vi và kết quả

| Kiểm tra | Kết quả |
| --- | --- |
| Clone repo, 7 ngăn, 59 file gốc | PASS |
| Đọc 26 Markdown và .gitignore | Hoàn tất |
| Mở xem 10 contact sheets + 22 ảnh mẫu | Hoàn tất; JPG giải mã được 32/32 |
| Dải scan | PDF 01–58 / sách 212–269, không đứt dải tên file |
| Dải storyboard / prompt trang | 01–28; có prompt bìa trước/sau và 10 bảng nhân vật |
| Phân loại template | A=14, B=10, C=4; khớp danh sách trong ngăn 05 |
| Chương trình chế bản chạy được | Chưa có; hiện là đặc tả và ví dụ mã Markdown |
| Sinh ảnh trong onboarding | Không thực hiện |
| Quy chuẩn sản xuất hoàn toàn nhất quán | CHƯA ĐẠT; xem ONBOARDING_ISSUES.md |

## Kiểm đếm lời dẫn từng trang

**Phương pháp:** trích duy nhất dòng blockquote đầu trong mục Text Khung Dẫn Truyện; bỏ dấu `**`, tách theo khoảng trắng. “Số đơn vị” là token cách trắng, không phải phép phân từ tiếng Việt theo ngôn ngữ học. Tỷ lệ đỏ = tổng đơn vị trong các cặp `**...**` chia tổng đơn vị. Kết quả hỗ trợ biên tập, không đo thay số dòng thực tế khi typeset. Nhãn “52 từ”, “58 từ” có sẵn trong storyboard không được dùng làm số đo.

| Trang | Template | Đơn vị cách trắng | Cụm đỏ | Tỷ lệ đỏ | Cờ kiểm tra |
| --- | --- | ---: | ---: | ---: | --- |
| 01 | B | 58 | 5 | 39.7% | tỷ lệ đỏ |
| 02 | B | 62 | 5 | 35.5% | tỷ lệ đỏ |
| 03 | C | 61 | 6 | 37.7% | số cụm, tỷ lệ đỏ |
| 04 | A | 61 | 6 | 39.3% | số cụm, tỷ lệ đỏ |
| 05 | C | 57 | 5 | 26.3% | Trong ngưỡng đo |
| 06 | A | 66 | 7 | 37.9% | độ dài, số cụm, tỷ lệ đỏ |
| 07 | B | 60 | 5 | 28.3% | Trong ngưỡng đo |
| 08 | A | 59 | 4 | 22.0% | Trong ngưỡng đo |
| 09 | B | 65 | 5 | 33.8% | Trong ngưỡng đo |
| 10 | B | 65 | 6 | 40.0% | số cụm, tỷ lệ đỏ |
| 11 | A | 63 | 5 | 34.9% | Trong ngưỡng đo |
| 12 | C | 69 | 6 | 34.8% | độ dài, số cụm |
| 13 | A | 59 | 5 | 42.4% | tỷ lệ đỏ |
| 14 | A | 60 | 4 | 40.0% | tỷ lệ đỏ |
| 15 | B | 63 | 5 | 34.9% | Trong ngưỡng đo |
| 16 | A | 70 | 6 | 47.1% | độ dài, số cụm, tỷ lệ đỏ |
| 17 | B | 67 | 5 | 32.8% | độ dài |
| 18 | A | 64 | 4 | 42.2% | tỷ lệ đỏ |
| 19 | B | 69 | 6 | 42.0% | độ dài, số cụm, tỷ lệ đỏ |
| 20 | A | 66 | 4 | 33.3% | độ dài |
| 21 | C | 65 | 8 | 50.8% | số cụm, tỷ lệ đỏ |
| 22 | A | 62 | 5 | 29.0% | Trong ngưỡng đo |
| 23 | A | 65 | 5 | 33.8% | Trong ngưỡng đo |
| 24 | B | 69 | 4 | 27.5% | độ dài |
| 25 | B | 66 | 6 | 36.4% | độ dài, số cụm, tỷ lệ đỏ |
| 26 | A | 66 | 5 | 25.8% | độ dài |
| 27 | A | 70 | 7 | 32.9% | độ dài, số cụm |
| 28 | A | 74 | 10 | 50.0% | độ dài, số cụm, tỷ lệ đỏ |

- **11/28** lời dẫn vượt 65 đơn vị cách trắng.
- **11/28** có hơn 5 cụm tô đỏ.
- **14/28** có tỷ lệ đỏ vượt 35% theo phương pháp nêu trên.
- Không tự sửa lời dẫn hoặc dấu tô đỏ trong phiên này. Không coi số liệu này là xác nhận đã kiểm font, ngắt dòng, bleed hay màu in.

## Đối chiếu ảnh nguồn nổi bật

- Scan PDF 06 / sách 217: rồng vàng hóa đôi khổng tước.
- Scan PDF 18–19 / sách 229–230: mươi phát tên, mười mũi liên tiếp.
- Scan PDF 32 / sách 243: Đô sư phụ vuốt chòm râu.
- Scan PDF 39 / sách 250: tám voi đực, ngà trắng; số 78 trong bản diễn giải cần sửa/duyệt lại.
- Scan PDF 58 / sách 269 kết Hồi 8 ở lệnh của Thánh Thiên, chưa có cảnh 65 thành/lên ngôi trong đoạn trích.

## Giới hạn của lần rà soát

Không có PDF gốc độ phân giải cao, đối chiếu chính sử ngoài repo hoặc bằng chứng duyệt thiết kế. Không xác nhận mọi dấu bút đã được chép lại nguyên văn 100%; contact sheets cho phép đối chiếu trực quan nhưng các đoạn nhỏ cần crop/phóng lớn khi biên tập chi tiết. Mọi trạng thái APPROVED còn phải qua kiểm sản phẩm thực.
