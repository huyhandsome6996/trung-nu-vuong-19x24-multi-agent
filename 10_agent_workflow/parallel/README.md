# Hai agent làm song song trên main

Ủy nhiệm mới của chủ dự án10/11/2026: hai ChatGPT agent bên ngoài cùng sản xuất, giữ main, không nhánh/PR. Mục này thay quy tắc một writer chung đối với đúng hai phạm vi đã giao. Không tự spawn thêm agent.

| Người | Phạm vi | State và nhật ký được ghi |
| --- | --- | --- |
| Coordinator |01–13; sửa thoại01–12;4trang phụ;4mặt bìa; công cụ chung; ghép/QA/bàn giao | State/log chung và `parallel/coordinator/` |
| AgentA |14–20, từng trang TEXT→ART→LAYOUT→QA | `parallel/agent_a/` |
| AgentB |21–28, từng trang TEXT→ART→LAYOUT→QA | `parallel/agent_b/` |

Nguồn thẩm quyền phân công: `assignments.json`. Mỗi agent clone vào thư mục riêng (`tnv-agent-a`, `tnv-agent-b`); tuyệt đối không dùng chung working tree/index với coordinator hay agent kia.

## File được phép ghi

- Chỉ `10_agent_workflow/tasks/PAGE##_TEXT|ART|LAYOUT|QA/` của trang được giao.
- Chỉ file `PAGE##_...` của trang được giao trong `assets_generated/raw_pages/`, `assets_generated/speech_clouds/`, `final_book_19x24/source|proofs|reading/`.
- Toàn bộ thư mục riêng `10_agent_workflow/parallel/agent_a/` hoặc `agent_b/`, và `assets_generated/parallel/agent_a/` hoặc `agent_b/`. Bản PDF gộp của lô, script riêng, yêu cầu sửa công cụ và ghi chú đều đặt trong thư mục lane riêng.
- Không sửa state/log chung, storyboard, Ngăn07/09, font, script dùng chung, assignments, trang agent khác, file sách gộp cuối. Cần sửa thì ghi yêu cầu trong lane, tiếp tục việc độc lập. Không xóa/đổi tên bản đã có; tạo version mới.

`guard` kiểm toàn bộ staged/unstaged/untracked; chặn file ngoài phạm vi và xóa/rename bản cũ. Đây là kiểm phạm vi file, không thay QA nội dung. Không dùng `git add .`, force-push, reset --hard hoặc checkout file của người khác.

`publish` còn kiểm từng commit local chưa có trên `origin/main`, kể cả khi working tree đã sạch. Một file chung bị commit nhầm không được lọt qua bằng cách làm sạch index. Kiểm này chạy sau fetch và sau rebase; chỉ các commit của chính lane chưa được đẩy mới được xét, không chặn commit hợp lệ của lane khác đã có trên remote.

Hai bản giao việc đầy đủ hiện hành là `agent_a/PROMPT.md` và `agent_b/PROMPT.md`, đồng thời được lưu bất biến ở `PROMPT.v002.md`; bản ngắn cũ được giữ ở `PROMPT.v001.md`. Chủ dự án xác nhận hai agent chưa khởi động tại mốc sản xuất18d65f4. Không checkout về mốc đó: clone main mới nhất để nhận công cụ và hướng dẫn cập nhật.

## Queue riêng, không tranh một production_state.json

Chạy từ gốc clone của mình; thay `agent_a` thành `agent_b` khi tương ứng:

```bash
python -m pip install -r requirements.txt
python scripts/parallel_workflow.py --lane agent_a doctor
python scripts/check_repo.py
python scripts/parallel_workflow.py --lane agent_a status
python scripts/parallel_workflow.py --lane agent_a next
python scripts/parallel_workflow.py --lane agent_a packet PAGE14_ART
python scripts/parallel_workflow.py --lane agent_a start PAGE14_ART --owner agent_a --note "Đọc brief và xem ảnh thực"
python scripts/parallel_workflow.py --lane agent_a checkpoint PAGE14_ART --note "File đã có; lỗi còn lại; bước tiếp"
python scripts/parallel_workflow.py --lane agent_a finish PAGE14_ART --evidence 10_agent_workflow/tasks/PAGE14_ART/report.v002.json --note "Đã kiểm thật"
```

Các trạng thái `done` được kế thừa có evidence đã khóa: dùng lại, không ghi đè. Bản draft và request cũ không chứng minh tác vụ đã xong. Chữ cũ27–28 có thể còn file nhưng task chưa finish: đọc nguồn bổ sung và tạo bản mới, không tự gắn done. Baseline và SOURCE_EPILOGUE là prerequisite read-only trong lane; agent chỉ có thể mutate task thuộc trang mình.

## Lưu sau từng kết quả, xử lý cuộc đua push

Ghi `WORK_LOG.md` và `LESSONS_LEARNED.md` trong lane, rồi:

```bash
python scripts/parallel_workflow.py --lane agent_a check
python scripts/parallel_workflow.py --lane agent_a guard
python scripts/parallel_workflow.py --lane agent_a stage
python scripts/parallel_workflow.py --lane agent_a publish --message "agent_a: page14 art checkpoint"
```

`publish` kiểm phạm vi, queue/evidence và check_repo, commit staged files, fetch/rebase main, push. Nếu người khác vừa push thì tự fetch/rebase rồi thử lại; không force. Nếu có conflict thật, abort rebase giữ commit của mình và báo đường dẫn, không chọn ours/theirs bừa. Sau push, script fast-forward theo cập nhật mới nếu cần để đối chiếu SHA local và remote bằng nhau.

Dùng quyền môi trường; khi cần PAT, truyền bằng biến môi trường của tiến trình `TNV_GIT_TOKEN` hoặc `GH_TOKEN`/`GITHUB_TOKEN`, không lưu token vào file, URL hay nhật ký. Wrapper dùng credential helper tạm trong bộ nhớ, không ghi cấu hình credential bền vững. Không chép PAT vào prompt/file bàn giao.

Nếu công cụ ảnh timeout: kiểm file trả thật; lưu image/request/metadata và push ngay khi có output, trước khi làm việc dài khác. Không nhận đang có job nền sau khi phiên đã bị ngắt. Thiếu công cụ thì block đúng task trong lane, tiếp tục việc độc lập.

## Yêu cầu sản xuất

Đọc `AGENTS.md`, `START_HERE.md`, workflow A–Z, SOURCE_DECISIONS, IMAGE_CATALOG, hồ sơ/scan đúng trang và `09_design_system/SPEECH_STYLE_V2.md`. Xem pixel ảnh trước khi truyền. Giữ chuẩn mặt/trang phục theo giai đoạn, đúng số lượng/quan hệ theo scan; lời dẫn35–65tiếng, đủ thoại, keyword đỏ#C81E1E. Bóng thoại mới phải được **vẽ cùng chữ bên trong**, hợp nét/màu cảnh như PAGE12v003, không hộp trắng UI.

Giữ trim190×240/bleed196×246 và safe tokens; native<300DPI phải ghi thật. Lưu nguồn sửa được, bản render, prompt/hash/meta và báo cáo thị giác; QA agent không phải USER_APPROVED/PRINT_READY. Nguồn27–28 đã có trong SOURCE_EPILOGUE; không biến montage hay E14 tượng trưng thành sự kiện/di tích đã xác minh.

## Kết thúc lô và ghép sách

Agent hoàn thiện hết task của mình, viết `HANDOFF.md` trong lane: file/version/SHA, trang đã QA, blocker và việc cần coordinator. Không nhập state chung hoặc ghép sách toàn bộ.

Coordinator chạy `python scripts/integrate_parallel.py --lane agent_a` (và agent_b) sau khi toàn lane done. Lệnh kiểm evidence/hash trước khi nhập đúng task vào state chung, không sửa lane. Chỉ coordinator gộp nhật ký,4trang phụ/4mặt bìa/32ruột và báo cáo cuối; PRINT_SPEC vẫn cần dữ liệu nhà in thực.
