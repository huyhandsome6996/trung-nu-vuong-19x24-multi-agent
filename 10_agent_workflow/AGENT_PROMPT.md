# Copy đề bài dưới để giao agent khác

```text
Hãy tiếp quản và sản xuất dự án TRƯNG NỮ VƯƠNG 19×24 cm tại:
https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent

Clone main, đọc AGENTS.md và START_HERE.md, làm theo 10_agent_workflow/WORKFLOW_A_TO_Z.md. Mọi việc cập nhật trực tiếp main; không tự chia nhánh hoặc tạo PR. Giữ các file, thiết kế và bằng chứng đã có.

Chạy python scripts/check_repo.py, rồi python scripts/workflow.py status/next/packet. Ưu tiên việc đang dở; nếu không có thì chọn task đủ phụ thuộc. Đọc storyboard, scan, hồ sơ và mở ảnh tham chiếu thật; giữ đồng nhất mặt, trang phục và đạo cụ. Một agent lần lượt đảm nhiệm sáu vai trò, không bắt buộc gọi nhiều agent.

Tôi giao bạn thực hiện A–Z trong phạm vi có dữ liệu và công cụ: kiểm nguồn, khóa chữ, sinh tranh nền không chữ, ghép chữ Việt/khung giấy cổ/từ khóa đỏ #C81E1E, kiểm từng trang, bìa, trang phụ, đóng sách và bàn giao. Sách có 28 trang truyện, 4 trang phụ và 4 mặt bìa. Bộ thiết kế baseline đã có; không vẽ lại toàn bộ nhân vật từ đầu.

Dùng start/checkpoint/finish với báo cáo và artifact thật. Sau từng phần đã kiểm, ghi WORK_LOG/LESSONS_LEARNED, commit/push main và xác nhận SHA remote. Không đợi xong cả sách mới lưu. Khi bị ngắt, ghi rõ file đã có, lỗi còn lại và bước tiếp để agent sau tiếp tục được.

Trang 27–28 cần nguồn bổ sung: chủ động nghiên cứu nguồn công khai chính thống và ghi đối chiếu trước khi khóa chữ. Thiếu công cụ ảnh/renderer hoặc dữ liệu nhà in/ISBN/quyền cần thiết thì block đúng task, ghi thiếu gì và tiếp tục việc độc lập. Không bịa kết quả. DESIGN_BASELINE và CI xanh không có nghĩa tôi đã duyệt hoặc sách sẵn in. Chỉ hỏi dữ liệu bắt buộc không thể suy ra, sau khi đã làm các phần có thể làm.

Không lưu PAT/mật khẩu vào repo, log hoặc URL. Clone repo public không cần PAT; push dùng quyền do môi trường cấp. Không tự xuất bản thương mại hoặc gửi file cho bên thứ ba ngoài phạm vi tôi giao.
```

Đây là đề bài để chủ dự án giao cho agent khác. Tạo workflow không tự khởi chạy toàn bộ 125 task hoặc tác vụ chạy nền.
