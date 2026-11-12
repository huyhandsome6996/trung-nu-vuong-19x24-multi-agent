# Sửa truyện theo góp ý giáo viên -5 agent

Nhánh: `sua-theo-gop-y-giao-vien`. Ngày chuẩn bị:12/11/2026. Bản nền: PDF Gemini21 trang tính cả bìa. Phạm vi hiện tại là chuẩn bị đủ nguồn, phân tích và giao việc; chưa có trang tranh đã sửa.

## Bắt đầu

- Agent1: đọc04_agents/agent_1/BRIEF.md, làm PDF01–05.
- Agent2: đọc04_agents/agent_2/BRIEF.md, làm PDF06–09.
- Agent3: đọc04_agents/agent_3/BRIEF.md, làm PDF10–14.
- Agent4: đọc04_agents/agent_4/BRIEF.md, làm PDF15–17.
- Agent5: đọc04_agents/agent_5/BRIEF.md, làm PDF18–21.

Đọc AGENTS.md của ngăn này,02_quy_chuan/NGUYEN_TAC_SUA.md và 00_dieu_phoi/PHAN_TICH_VA_PHAN_CONG.md trước khi làm. 5 prompt độc lập để người dùng giao cho 5 đoạn chat nằm trong 05_prompts/. Mỗi lane chịu trọn chuỗi sửa chữ/tranh/dàn trang/QA trong trang mình, nên có thể triển khai song song.

## Các ngăn

|Ngăn|Nội dung|
|---|---|
|00_dieu_phoi|Phân tích, chia trang, manifest nguồn, nghiệm thu, ảnh tổng quan|
|01_nguon_bat_bien|PDF Gemini gốc;21 JPEG nhúng không chỉnh;9 ảnh khoanh;4 ảnh tham khảo trang phục; yêu cầu nguyên văn|
|02_quy_chuan|Cờ/trang phục/nhận diện/chữ; gợi ý thoại chuyển thể|
|03_nhiem_vu_tung_trang|21 brief MD +21 bản JSON, mỗi trang một chủ|
|04_agents|5 lane độc lập: brief, text, source, output,qa, trạng thái và nhật ký|
|05_prompts|5lệnh trực tiếp dạng.md|
|06_cong_cu|Kiểm nguồn/phân công, kiểm lane, ghép PDF21 trang|
|07_tong_hop|Coordinator ghép sau khi 5 lane xong|

## Những điểm phải nhớ

PDF mới là nguồn hình và bố cục, repo chỉ đối chiếu cốt truyện. Không dùng hình thiết kế cũ trong repo. Không chạy workflow main-only/28 trang cũ trên đợt sửa này. Chỉ push nhánh sửa, chỉ ghi lane riêng. Không sửa các file chung đồng thời. Cờ thay toàn truyện theo một quy ước; mặt Thánh Thiên khóa thống nhất. Ô vàng phải gọn ở mọi trang. Không tự nhận phục dựng lịch sử hoặc đã đạt in 300 DPI từ nguồn thấp.

Nguồn gốc: PDF21 trang,430,08×576pt, ảnh896×1200px/trang, không có lớp text.9 ảnh ZIP chỉ khoanh vị trí; chữ yêu cầu lấy từ tin nhắn người dùng. Manifest SHA256 khóa nguồn. Giữ khổ PDF gốc ở đợt sửa; tên repo19x24 không phải bằng chứng khổ thực tế.

## Kiểm gói và bàn giao

```bash
python3 11_sua_theo_gop_y_giao_vien/06_cong_cu/check_packet.py
python3 11_sua_theo_gop_y_giao_vien/06_cong_cu/validate_lane.py agent_1 --ready
```

Lệnh ready chỉ dùng khi đã có output, hiện tại dự kiến báo thiếu vì trạng thái NOT_STARTED. Đây là đúng, không phải lỗi gói. CầnPython 3,PyMuPDF,Pillow cho kiểm ảnh/PDF và ghép; công cụ tạo/chỉnh tranh phải do môi trường agent cung cấp, repo không tự sinh tranh.
