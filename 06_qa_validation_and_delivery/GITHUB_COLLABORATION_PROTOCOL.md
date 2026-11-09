# Giao thức hiện hành: mọi việc ở main

Quyết định ngày 09/11/2026 thay quy ước phân nhánh trước đây. Main chứa cả bản nháp và bản đã kiểm; metadata/báo cáo xác định mức hoàn thành. Vào main không đồng nghĩa chủ dự án đã duyệt.

1. Clone/pull main; đọc START_HERE, AGENTS và production_state; ưu tiên resume.
2. Một agent ghi tại một thời điểm. Không tự tạo branch/PR; sáu vai trò là chuyên môn, không phải sáu nhánh.
3. Làm theo task ID và packet/start/checkpoint/finish với evidence thật.
4. Giữ nguyên nguồn Ngăn 07 và asset cũ. File mới có phiên bản/hash, theo [quy ước đầu ra](../10_agent_workflow/CAPABILITIES_AND_OUTPUTS.md).
5. Ghi WORK_LOG/LESSONS, chạy `python scripts/check_repo.py`, stage đúng phạm vi, commit, pull --rebase và push main.
6. Đối chiếu SHA local/remote trước khi báo đã đồng bộ. Không force-push hoặc lưu credential trong repo.
7. File in phải qua QA thực theo [workflow](../10_agent_workflow/WORKFLOW_A_TO_Z.md), không dùng checkbox mẫu để khẳng định đã kiểm.

[Phục hồi](../10_agent_workflow/RECOVERY_AND_MAIN.md) · [Mẫu bàn giao](../10_agent_workflow/templates/HANDOFF.md) · [Lệnh](../10_agent_workflow/COMMANDS.md)
