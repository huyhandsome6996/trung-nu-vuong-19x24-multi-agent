# Quy tắc cho mọi agent — main là nơi làm việc duy nhất

## Tiếp quản

1. Đọc START_HERE.md và10_agent_workflow/WORKFLOW_A_TO_Z.md. Chạy doctor, check_repo, status, next; đọc WORK_LOG và ghi chú tác vụ đang dở.
2. Chỉ dẫn trực tiếp mới nhất của chủ dự án ưu tiên hơn tài liệu cũ. Không coi yêu cầu chuẩn hóa workflow là lệnh sinh ngay28 trang.
3. Dùng main, không tự tạo nhánh/PR. Theo ủy nhiệm trực tiếp10/11/2026, cho phép hai agent bên ngoài làm song song trong hai lane tách file. Đọc10_agent_workflow/parallel/README.md. Mỗi clone/mỗi lane chỉ một writer; chỉ coordinator ghi state/log chung. Không tự spawn thêm agent ngoài phân công.
4. Pull main trước khi làm; không force-push, reset --hard, ghi đè hoặc xóa thay đổi người khác. Nếu có xung đột, xem từng phần và giữ công việc đúng.

## Nguồn và thiết kế

- Ngăn 07 là nguồn bất biến; kiểm hash tại10_agent_workflow/source_hashes.json. Repo chứa10 contact sheets, không chứa PDF gốc độc lập. Không tuyên bố đã mở PDF không có thật.
- Sự kiện/quan hệ/số lượng theo scan và09_design_system/SOURCE_DECISIONS.md; nhận diện theo registry và ảnh hiện hành; lời dẫn/thoại/template theo Ngăn 03 sau kiểm nguồn. Prompt không thắng nguồn. Ngăn 10 quản lý quy trình/tiến độ, không tự thay nội dung nguồn.
- Giữ Đô Năng Tế nam có râu; Trưng Nhị lam sẫm; Thi Sách tía/hổ phù; Thánh Thiên lục/khăn tang. Mười phát tên liên tiếp; tám voi đực da xám ở Hát Môn; không suy mọi đàn voi đều có8.
- Nguồn bổ sung trang27–28 đã được kiểm trong SOURCE_EPILOGUE; đọc evidence và SOURCE_DECISIONS trước khi khóa chữ. Không coi nguồn đã kiểm là TEXT27–28 đã hoàn thành. Các bước độc lập khác vẫn tiếp tục được.
- Mở pixel ảnh tham chiếu, không chỉ đọc prompt. Dùng phiên bản active, giữ ID NV/E/P/A; ghi actual_references + hash thật. Bảng nhóm phải chọn đúng người/vị trí.
- Ảnh nền không chữ/bóng thoại/watermark, chừa20% đỉnh; chữ Việt ghép riêng, **từ khóa** tô #C81E1E. Khổ và tọa độ theo layout_tokens. Mép giấy cổ có ngoại lệ trang trí, chữ phải trong safe text. Không kéo méo ảnh hay đổi DPI rồi gọi ảnh đủ chi tiết in.

## Thực thi và bàn giao

- production_state.json là bảng tác vụ hiện hành; trạng thái NOT_GENERATED trong page_asset_matrix là mốc baseline thiết kế, không thay queue sản xuất. Chạy packet rồi start đúng ID. Có phiên đang làm thì resume, không làm trùng.
- Sau một kết quả nhỏ, checkpoint ghi file đã có/việc còn lại; cập nhật WORK_LOG và LESSONS_LEARNED khi có kinh nghiệm mới. Commit/push main sau phần kiểm được; không đợi2giờ mới lưu.
- Không ghi đè ảnh/tệp đã khóa: tạo v002 và cập nhật nguồn tham chiếu, hash, phạm vi ảnh hưởng. Khi sửa storyboard, rà text đã khóa vì hash cả file sẽ đổi. Muốn sửa tác vụ done: đọc CHANGE_CONTROL, đánh dấu lại downstream trước khi tạo bản mới.
- finish chỉ nhận evidence đã kiểm; pass kỹ thuật không thay kiểm thị giác/sử học, DESIGN_BASELINE không phải USER_APPROVED/PRINT_READY. Không khai đã gửi tham chiếu/đã xem ảnh/đã render nếu chưa làm.
- Thiếu công cụ/nguồn bắt buộc: block đúng tác vụ, ghi nguyên nhân và cách tiếp tục; làm các việc độc lập còn lại. Không tự bịa kết quả và không tự hỏi lại các lựa chọn thường nhật đã được ủy quyền.
- Trước commit: python scripts/check_repo.py. Trước bàn giao trọn sách: workflow.py check --release và QA thực, không chỉ CI xanh.
- Không lưu token/mật khẩu vào repo, remote URL, log hoặc ảnh. Chỉ báo đã push sau khi SHA local bằng refs/heads/main trên remote.

## Phân công hiện hành10/11/2026

- Coordinator giữ01–13, sửa thoại01–12, bìa/trang phụ/ghép sách và toàn bộ file chung. AgentA chỉ14–20; AgentB chỉ21–28. Quyền file do assignments.json và parallel_workflow.py kiểm.
- A/B bắt buộc dùng queue riêng bằng parallel_workflow.py, không chạy workflow.py để start/checkpoint/finish việc được giao và không sửa state/WORK_LOG/LESSONS chung. Publish dùng guard→stage→publish, main-only, fetch/rebase/retry, không force-push. Mỗi agent clone vào thư mục riêng.
- Quy chuẩn thoại mới:09_design_system/SPEECH_STYLE_V2.md, mẫuPAGE12v003. Vẽ bóng thoại cùng chữ Việt thành một asset hợp nét/màu bối cảnh, đuôi ngắn đúng người; không dùng hộp trắng bo góc/đuôi tam giác thẳng dài.
- Trong đợt song song, nguồn/storyboard/registry/font và công cụ dùng chung được giữ cố định; nhu cầu sửa ghi trong lane/request, coordinator xử lý. Không sửa file nguồn chung để đạt tiêu chí một trang.
