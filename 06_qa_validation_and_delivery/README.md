---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
compartment: "06_qa_validation_and_delivery"
owner_agent: "AGENT-06 (Quality Assurance & Print Auditor)"
consumers: ["ALL_AGENTS"]
---

# HƯỚNG DẪN SỬ DỤNG NGĂN 06: KIỂM ĐỊNH CHẤT LƯỢNG & GIAO THỨC CỘNG TÁC GITHUB (`06_qa_validation_and_delivery`)

## 1. Mục đích của Ngăn 06
Ngăn 06 là **Trạm Kiểm soát Chất lượng Cuối cùng (Final Quality Gate)** trước khi bất kỳ trang truyện hoặc ấn phẩm nào được phê duyệt phát hành. Đồng thời, ngăn này quy định **Giao thức Làm việc Nhóm trên GitHub (GitHub Multi-Agent Collaboration Protocol)** để nhiều AI Agent cùng đọc, chia nhánh (Branch), gửi Pull Request và bàn giao kết quả mà không bao giờ xung đột dữ liệu.

## 2. Danh mục Tài liệu trong Ngăn 06

| Tên File Markdown | Nội dung Trọng tâm | Agent Nào Bắt buộc Đọc? | Khi Nào Sử dụng? |
| :--- | :--- | :--- | :--- |
| `QA_CHECKLIST_HISTORICAL_ART_PRINT.md` | Hệ thống Bảng kiểm 3 Lớp (**Lớp 1: Sử học & Sư phạm Lớp 8–10**, **Lớp 2: Mỹ thuật & Bố cục theo mẫu JPG**, **Lớp 3: Kỹ thuật Chế bản In ấn 19×24 cm 300 DPI**). | Tất cả các Agent (đặc biệt là `AGENT-06`) | Kiểm tra từng trang ngay sau khi tạo ảnh và sau khi ghép chữ xuất file PDF. |
| `GITHUB_COLLABORATION_PROTOCOL.md` | Quy chuẩn cấu trúc nhánh Git (`feat/agent-03-...`), quy ước đặt tên file đầu ra, mẫu Pull Request (PR Template) và bảng trạng thái tiến độ từng trang. | Tất cả các Agent làm việc trên GitHub | Đọc trước khi thực hiện `git commit`, `git push` hoặc mở Pull Request. |
