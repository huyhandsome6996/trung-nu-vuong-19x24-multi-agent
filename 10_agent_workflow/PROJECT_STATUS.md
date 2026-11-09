# Hiện trạng để bắt tay làm ngay

Mốc 09/11/2026 sau hợp nhất main. Tiến độ về sau lấy từ `production_state.json` và WORK_LOG; không sửa ngược các báo cáo lịch sử.

| Hạng mục | Đã có | Việc còn lại |
| --- | --- | --- |
| Tư liệu | 26 Markdown và 32 JPG gốc, kiểm kê 59 file nền | Không có PDF độc lập trong repo; đọc 10 contact sheets |
| Thiết kế | 30 bảng hình, 41 hồ sơ, 14 cảnh, 36 nhóm đạo cụ, 4 động vật, 24 mặt tộc trưởng | Baseline dùng cho bản nháp; chưa tự coi mọi ảnh đã được chủ dự án duyệt |
| Kịch bản | 28 trang, chỉ định A/B/C, lời dẫn/thoại và **từ khóa** | Đối chiếu và khóa chữ; một số lời dẫn vượt 65 tiếng |
| Tranh trang | Bộ tham chiếu và thư viện prompt | Chưa sinh 28 trang minh họa thành phẩm |
| Dàn trang | SVG/tokens và helper HTML proof | Chưa có 28 trang ghép chữ hoặc file in |
| Vận hành | 125 tác vụ, CLI/brief/phục hồi và mẫu cấu hình CI (chưa kích hoạt) | Mốc này: 2 done, 122 todo, 1 blocked |
| Phần kết | Trang 27–28 có nhãn mở rộng | Cần nguồn ngoài đoạn trích, task SOURCE_EPILOGUE |
| Chế bản cuối | Trim 190×240, bleed 196×246 mm | Cần font Việt, giấy/đóng/gáy/ICC; thông tin xuất bản và quyền sử dụng khi liên quan |

Bước tiếp theo: `python scripts/workflow.py packet PAGE01_TEXT`. Mở brief và đối chiếu scan PDF 06–07. Sau khi khóa chữ một trang có thể đi tiếp ART → LAYOUT → QA hoặc chuyển sang việc độc lập nếu thiếu công cụ.

Lời dẫn trang 06/12/16/17/19/20/24/25/26/27/28 vượt 65 tiếng ở mốc này. Số đếm dựa trên khoảng trắng, không phải tách từ theo ngôn ngữ học. Tiêu đề ghi “52 từ” trong tài liệu cũ không thay số đếm thực. Các câu tuyệt đối như “vĩ đại nhất” cũng cần đối chiếu và tiết chế trong bước TEXT.
