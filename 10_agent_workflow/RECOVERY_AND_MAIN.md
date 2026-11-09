# Làm trên main và phục hồi khi bị ngắt

## Trước phiên

Chạy `git status --short`. Nếu sạch: `git switch main` rồi `git pull --ff-only origin main`. Nếu có sửa dở, đọc trạng thái/WORK_LOG và giữ lại công việc; không reset xóa. Chạy check/status/next. Task in_progress chứa owner, last_note và updated_at; mở brief cùng các file đã có để tiếp tục.

## Lưu theo phần nhỏ

Sau một đoạn chữ đã đối chiếu hoặc một ảnh đã lưu, checkpoint nêu file thật, trạng thái, lỗi còn lại và bước tiếp. Chạy check rồi commit/push main. Không đợi toàn bộ 28 trang. Sau một lần gọi công cụ dài, lưu artifact trước khi gọi lượt tiếp.

Git không tự đồng bộ file chưa push. Phiên bị ngắt vẫn có thể mất file tạm chưa lưu; workflow giảm rủi ro bằng checkpoint và commit nhỏ, không hứa chống mọi lỗi môi trường.

## Trước push

1. Xem `git diff --stat`, diff cụ thể và ảnh/PDF đã đổi; stage đúng file đã kiểm.
2. Chạy `python scripts/check_repo.py`, rồi commit theo phạm vi.
3. `git pull --rebase origin main`. Nếu xung đột, xem từng file và giữ công việc đúng; không dùng ours/theirs đại trà.
4. `git push origin main`. Đối chiếu `git rev-parse HEAD` với `git ls-remote origin refs/heads/main`.
5. Nếu bị từ chối, ghi đúng lý do thiếu quyền hoặc protection. Không force-push hay tự tắt protection; dùng quyền xác thực do môi trường cấp, không nhúng PAT vào URL/file.

## Một người ghi tại một thời điểm

Queue chặn nhiều task active trong cùng bản clone. Hai agent trên hai máy vẫn có thể nhận trùng trước khi sync; đây không phải khóa phân tán. Mặc định chỉ một agent ghi, agent khác đọc. Nếu chủ dự án giao cộng tác, phân phạm vi rõ và lần lượt commit/pull.

## Nhánh cũ và thay đổi đã khóa

Thiết kế và QA cũ đã được hợp nhất vào main, giữ nguyên lịch sử commit. Chỉ xóa nhánh cũ sau khi xác nhận main remote chứa toàn bộ commit đó. Agent mới không clone nhánh thiết kế theo các log lịch sử.

Khi đổi artifact đã khóa, đọc [CHANGE_CONTROL](CHANGE_CONTROL.md). Reopen bước đầu chịu ảnh hưởng và chuỗi sau nó, giữ phiên bản cũ. Hash fail là dấu hiệu cần rà lại, không chỉ thay hash để báo xanh.
