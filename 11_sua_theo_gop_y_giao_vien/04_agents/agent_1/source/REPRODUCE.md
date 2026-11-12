# Tái tạo đầu ra Agent 1

Chạy từ bất kỳ thư mục nào:

```bash
python3 11_sua_theo_gop_y_giao_vien/04_agents/agent_1/source/build_pages.py --combine
```

Đầu vào dàn trang là JPEG bất biến trong ngăn 01, `PDF_XX/art_edit_raw.png`, mask/toạ độ trong script, chữ cuối trong `../text/PDF_XX.json` và font Noto đính kèm. `edit_prompt.md` cùng `provenance.json` ghi công cụ và ảnh tham chiếu đã gửi. Chỉnh tranh đã thực hiện bằng image_gen.imagegen; chạy lại mô hình sinh không bảo đảm cùng pixel. Script chỉ chọn vùng ảnh đã sửa, giữ pixel gốc ngoài mask và dàn chữ thật; không tự vẽ cờ/nhân vật bằng hình học.

`layout.json` lưu cỡ chữ, hộp chữ và từng dòng cuối. PDF01 giữ chữ raster bìa gốc; PDF02–05 có lớp chữ thật. Mỗi PDF có MediaBox 430,08 × 576 pt; PNG 896 × 1200 px, giữ tỉ lệ gốc. Không nâng DPI hoặc tuyên bố đạt in 300 DPI.

Sau khi tái tạo cần render độc lập bằng `pdftoppm -f 1 -singlefile -r 150 -png ...` và mở ảnh để kiểm lại; script không tự ký PASS thị giác.
