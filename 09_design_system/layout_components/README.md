# Thành phần dàn trang

Các file SVG là mẫu vector có tọa độ xác định, không sinh bằng AI. `*_guide.svg` có đường kỹ thuật, không đưa vào trang cuối. File blank chỉ chứa thành phần trang trí, chữ ghép sau.

- template_A_guide.svg: toàn trang.
- template_B_guide.svg: hai khung chéo.
- template_C_guide.svg: khung trên/dưới và ví dụ zoom tròn; chọn một cách chia phù hợp cảnh, không bắt buộc mọi trang C có cả hai kiểu.
- parchment_blank.svg: giấy cổ trên canvas196×246mm, gốc trim(0,0), chữ riêng.
- speech_bubble_blank.svg: bóng thoại mẫu80×48mm; kéo đuôi theo người nói, không kéo méo chữ.
- folio_blank.svg: nền số trang8mm, tâm trong vùng an toàn.
- cover_spread_guide.svg: bìa trải giả định gáy3.5mm, chưa chốt in.
- layout_tokens.json: nguồn thông số máy đọc.

## Vùng an toàn và khung giấy cổ

Trang lẻ: X16..178/Y14..226. Trang chẵn: X12..174/Y14..226. Cùng kích thước162×212mm. Vùng dùng chung hai phía là X16..174 (rộng158mm). Mép giấy cổ X11..179/Y8..48 được coi là trang trí; chữ đặt trong X18..172/Y14..43. Đây là ngoại lệ có ghi trong SOURCE_DECISIONS.md, không tuyên bố toàn khung nằm trong vùng chữ an toàn.

Số trang đường kính8mm: tâm trang lẻ(173,221), chẵn(17,221), để toàn hình tròn không chạm mép safe. 5 dòng cỡ12.8pt ×1.42 cần khoảng32mm, lớn hơn vùng chữ cao29mm; vì thế phải dựng thử thật và có thể dùng4 dòng hoặc biên tập lời dẫn, không cam kết mọi đoạn65 đơn vị vừa5 dòng. Không tự hạ chữ quá nhỏ.

## Bìa

Trước có4 tầng chữ theo COVER_DESIGN_SPEC, vùng tranh có chủ thể rõ dưới tiêu đề. Sau có lư đồng/cờ/tóm tắt/ô ISBN trống. Viền đại tự chọn bản đỏ son–trắng kem–đồng vàng với bóng đen mảnh, giữ 4 tầng thống nhất. Không dựng mã ISBN giả. Khổ trải và gáy chỉ là guide; hỏi nhà in khi xuất bản in cuối.

## Font và xuất

Noto Sans là lựa chọn ưu tiên; cần kiểm font thực có đủ dấu Việt/được phép nhúng trước dùng. Không tải ngẫu nhiên font hoặc giả định font đã kèm repo. Màu in cần ICC nhà in. Khi xuất PDF: trang canvas196×246mm, TrimBox cách3mm, BleedBox phủ canvas. SVG guide không thay thế pipeline PDF hoàn chỉnh.
