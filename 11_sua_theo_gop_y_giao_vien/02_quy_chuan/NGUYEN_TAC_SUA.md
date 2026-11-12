# Quy chuẩn sửa chung - chốt cho cả 5 agent

## Thứ tự ưu tiên

1. Chỉ thị người dùng ngày 12/11/2026 và yêu cầu giáo viên trong ngăn này.
2. PDF Gemini được gửi: nguồn bố cục, phong cách, nội dung hiện có và vị trí sửa.
3. 9 ảnh khoanh đỏ: vị trí chỉ dẫn. ZIP không có lời phê dạng chữ; phần chữ do người dùng chép.
4. Cốt truyện ở ngăn 01/03 và quyết định nguồn của repo để kiểm sự kiện, tên, quan hệ; không lấy ảnh thiết kế hoặc bố cục cũ của repo để thay bản Gemini.

Giữ 21 trang, tính bìa là PDF01. Không chạy queue sản xuất 28 trang trong ngăn 10; không sửa main hoặc thiết kế cũ. Không thêm thắt sự kiện ngoài góp ý. Bổ sung thoại là lời chuyển thể biên tập, ghi rõ như vậy trong text/changes.md; không gán thành nguyên văn chính sử.

## Cờ: phương án mỹ thuật thống nhất, không tuyên bố phục dựng lịch sử

Người dùng yêu cầu thay cờ nhưng chưa đưa mẫu cờ. Để 5 agent có thể làm ngay, dùng quy ước tạm thống nhất: quân Lĩnh Nam/Văn Lang/Hai Bà dùng cờ vải hình chữ nhật đỏ đất (#A84032), trơn, không ngôi sao, chữ, quốc huy, rồng kiểu triều đại muộn; cán gỗ mộc. Xem MAU_CO.svg. Không dùng cờ đỏ sao vàng hiện đại hoặc cờ tròn mặt trời dễ nhìn thành quốc kỳ. Nếu buộc biểu diễn cờ quân Hán, dùng vải xám than trơn để phân biệt, giữ đúng phe. Đây là quy ước minh họa giảm sai niên đại, không khẳng định cờ cổ thật có hình dạng này. Nếu giáo viên cung cấp mẫu khác, coordinator đổi quy chuẩn một lần rồi rà mọi trang.

Rà cờ trên bìa, bờ sông, thuyền, sau lưng nhân vật, đám đông và phía xa; không chỉ sửa chỗ khoanh.

## Trang phục: theo tham khảo mới, giữ phong cách Gemini

Mở cả 4 ảnh người dùng gửi trong 01_nguon_bat_bien/tham_khao_trang_phuc. Chúng là tham khảo tạo hình được người dùng cung cấp, không phải chứng cứ khảo cổ đã xác thực. Giữ nét bút, tỉ lệ người và màu tranh Gemini; không chuyển nhân vật thành chibi theo ảnh tham khảo. Ưu tiên áo vạt trái hoặc áo ngắn/váy quấn, khăn vấn, đai vải, họa tiết hình học gợi Đông Sơn; màu nâu đất, chàm, đồng trầm. Giáp ngắn da/phiến đơn giản theo ảnh tham khảo cho chỉ huy; không đồng hóa mọi người thành cùng một giáp. Hạn chế mũ quan cao, áo đại triều, giáp vai/rồng hoặc tóc mũ kiểu cổ trang Trung Hoa trên phe Lĩnh Nam. Không tự xóa chi tiết gia truyền có ý nghĩa cốt truyện như hổ phù Thi Sách.

Phe Hán giữ hệ trang phục khác, không mặc đồ mới của nghĩa quân cho Tô Định/Tào Quyền/Mã Tắc/Lữ Thạch. Người hầu, dân, cung thủ và chỉ huy có mức trang bị phù hợp. Không tự thay toàn bộ thành quách mọi trang: cảnh đồng quê có trâu/lúa được chỉ định trực tiếp ở PDF03.

## Khóa nhận diện Thánh Thiên để hai lane làm song song

Áp dụng ngay cho PDF16–20, và nhân vật Thánh Thiên ở PDF21 nếu có: nữ tướng trẻ, mặt bầu hơi góc cạnh, gò má khỏe, lông mày ngang, mắt hạnh vừa, mũi ngắn, cằm tròn; tóc đen búi thấp, khăn tang trắng rõ, áo/giáp ngắn nền lục trầm (#526747), không vương miện vàng/lông lớn như Trưng Trắc. Giữ tỉ lệ người lớn theo Gemini. Trưng Trắc giữ nhận diện mặt dài, mày cong và mũ chỉ huy của bản nền; Trưng Nhị phân biệt bằng nền áo chàm. Cụm này là khóa mới, không lấy các ảnh thiết kế sẵn trong repo.

Agent4 xuất thêm source/THANH_THIEN_REFERENCE.png từ trang16 đã sửa để agent 5 đối chiếu cuối lượt. Agent5 được đọc asset lane 4, nhưng không phải đợi nó mới bắt đầu; dùng khóa chữ + ảnh PDF16/17 gốc để làm. Trước khi READY, nếu reference đã có thì đối chiếu; nếu chưa có, ghi mục liên trang PENDING để coordinator kiểm cuối. Không nhận toàn sách đã đồng bộ khi chưa xem cạnh nhau.

## Chữ và ô vàng

Thu ô theo lượng chữ, không chỉ tăng chữ cho đầy hộp. Điểm xuất phát: đệm trên/dưới khoảng 0,6–1 chiều cao dòng, đệm ngang vừa phải; điều chỉnh bằng mắt theo trang. Giữ các khung tranh, có thể nới vùng tranh vào phần ô vừa thu để không để dải trống. Không che nội dung tranh. Không ép kích thước bằng cách kéo méo nhân vật. Khóa “Phượng Hoàng” và “Trảm thủ!” thành cụm để không rớt tiếng cuối. Chú giải chân PDF02 bỏ nhãn, bỏ dấu * gọi nhãn, in nghiêng và giữ “Tiên phát chế nhân” trong ngoặc kép.

Lời thoại thêm ngắn, tự nhiên, phù hợp lớp 8–10. Bóng thoại hòa nét/màu, có đuôi đúng người, không hộp trắng lớn che tranh. Dùng chữ thật nếu công cụ hỗ trợ để giữ chính tả. Tránh vừa để chữ cũ trong ảnh vừa chồng chữ mới. Hình vùng chữ cũ cần được làm sạch trước khi dàn lại.

## Kích thước và chất lượng nguồn

PDF nguồn đo được 430,08×576 pt (~15,17×20,32 cm), không phải khổ19×24 dù tên repo có19x24. Ảnh nhúng896×1200 px, PDF không có lớp chữ trích xuất. Gói sửa giữ MediaBox nguồn và tỉ lệ trang để ghép an toàn; không kéo méo sang19×24. Chuyển khổ in là bước riêng nếu người dùng yêu cầu sau này. Không đổi nhãn DPI rồi gọi là nâng chất lượng. Giữ JPEG nguồn bất biến; xuất PNG sửa và PDF từng trang cùng khổ gốc.
