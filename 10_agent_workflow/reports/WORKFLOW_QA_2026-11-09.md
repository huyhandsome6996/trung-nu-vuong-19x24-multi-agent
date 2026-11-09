# Kiểm tra workflow ngày 09/11/2026

## Đã chạy và đạt ở môi trường làm việc

- 8 unit tests: chọn task/tiếp tục sau reload, chặn phụ thuộc chưa xong, từ chối report chưa kiểm, phát hiện artifact đổi hash, reopen downstream, từ chối storyboard cũ, chu trình/path thoát repo, ảnh native/ảnh tham chiếu và keyword/draft proof.
- `workflow.py check`: 125 task, phụ thuộc không chu trình, 28 phần storyboard, evidence và hash 32 JPG nguồn.
- `check_repo.py`: link Markdown, mẫu credential, registry và ảnh thiết kế; đủ 41 hồ sơ/14 cảnh/36 đạo cụ/4 động vật, 29 công việc ảnh bổ sung đã có file. `git diff --check` đạt.
- Doctor/status/next/packet thực chạy: main; 2 baseline done, 122 todo, 1 blocked; PAGE01_TEXT là việc tiếp. Packet dẫn đúng PROP03/PROP04 v002 hiện hành, draft chưa chép thoại có cảnh báo rõ.
- `workflow.py check --release` trả mã lỗi 1 do còn tác vụ sản xuất: đây là kết quả mong đợi, ngăn báo đã hoàn tất sách khi mới dựng workflow.

## Giới hạn kiểm tra

- Không sinh ảnh/trang truyện mới trong nhiệm vụ hợp nhất và chuẩn hóa repo.
- Helper HTML proof đã kiểm một phần logic keyword/draft bằng tests; chưa kiểm bản render trong browser hoặc nhúng font Việt/PDF in thực. Agent chế bản phải chạy với text locked, ảnh và font thật rồi mở renderer kiểm.
- JSON report và các check pass là lời xác nhận của reviewer; CLI kiểm được cấu trúc/file/hash, không tự xác nhận nội dung scan, gương mặt hoặc không có chữ trong tranh.
- GitHub từ chối tạo workflow bằng PAT hiện tại vì thiếu workflow scope. YAML được lưu làm mẫu tại templates/github-actions-validate.yml; CI chưa hoạt động. Tests/check đã chạy local. Khi có quyền workflow, đưa mẫu vào .github/workflows/validate-main.yml rồi kiểm trạng thái chạy thực trên GitHub.
- Hợp nhất/push và dọn nhánh chỉ được báo thành công sau đối chiếu Git remote. Kết quả thao tác được ghi vào nhật ký sau khi thực hiện.
