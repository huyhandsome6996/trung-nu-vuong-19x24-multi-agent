# Trang01 — QA bản đọc v001

**Kết luận: agent đã kiểm đạt trong phạm vi bản đọc; chưa USER_APPROVED, chưa PRINT_READY.**

| Lớp | Kiểm thực | Kết quả |
| --- | --- | --- |
| Nguồn | Đối chiếu scan06–07/sách217–218 và SOURCE_REVIEW; nhãn huyền tích, không gán chim thành chị em Trưng | Đạt |
| Mỹ thuật | So hai người với CHAR12, cảnh với ENV01; xem toàn trang và crop100% từ render300DPI; không thấy tay/chân thừa, không chữ AI/watermark; đúng2khổng tước | Đạt bản đọc |
| Ngôn ngữ |50tiếng,5cụm nhấn đủ;4dòng NotoSans12.8pt; xem dấu Việt và khoảng trắng sát từkhóa; PDF trích xuất khớp lời dẫn | Đạt |
| Hình học | Media/Bleed196×246mm; Trim[3,3,193,243]mm; chữ ở[18,14,154,29]mm từtrim; rãnh128..131.5mm; folio đúng token tranglẻ | Đạt |

Dùng Poppler hệ thống /usr/bin/pdftoppm render150DPI toàn trang và300DPI để crop kiểm. CảNotoSansRegular vàBold được nhúng/subset cóUnicode, giấy phépOFL lưu trongfonts. Khoảngcrop ngang0.05mm/mép, không kéo méo. Không có thoại nên speechplacement làđạt do khôngápdụng đã đốichiếu.

**Giới hạn in:** tranh native1120×1405px, khoảng145DPI hiệu dụng; render300DPI không tạo thêmchi tiết. Cần ảnh native cao hơn và thôngsốnhàin trướcpreflight cuối. ICC/chếđộđóng/gáy/quyền xuấtbản chưachốt,được theo dõiởPRINT_SPEC.

BảnLAYOUTv001 có khoảngtrắng lỗi tại ranhgiới cụmđỏ, đã thaybằngv002 và giữ để đốichiếu; chỉv002 đượcphép ghép bảnđọc.
