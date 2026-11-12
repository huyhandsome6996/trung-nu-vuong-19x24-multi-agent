# Tái tạo lô trang

`python3 11_sua_theo_gop_y_giao_vien/04_agents/agent_2/source/build_pages.py`

Phụ thuộc: Pillow, reportlab, PyMuPDF. Font Noto Sans Bold được lưu cùng nguồn.
Mỗi thư mục PDF_XX chứa ảnh chỉnh thật `edited_art.png`, tham số `layout.json`,
prompt và provenance. Script chỉ đặt chữ/ô dẫn; không vẽ phục trang, cờ hoặc
nhân vật bằng hình học. JSON chữ giữ toàn bộ lời dẫn và người nói.

PNG dùng chữ raster; PDF có lớp chữ Việt thật có thể chọn/copy. MediaBox giữ
430,08×576 pt. Nguồn gốc 896×1200 px; không tuyên bố 300 DPI hoặc giáo viên duyệt.
Ảnh chỉnh được giữ để tái tạo chính xác đầu ra; tái chạy mô hình tạo ảnh có thể
khác nét. Dùng ảnh nguồn bất biến ở ngăn 01 để đối chiếu, không ghi đè nguồn.
