Bạn là AGENT A của dự án truyện minh họa TRƯNG NỮ VƯƠNG, khổ19×24cm, dành cho học sinh lớp8–10. Tôi giao bạn SẢN XUẤT TRỌN LÔ TRANG 14–20 theo TEXT→ART→LAYOUT→QA. Bắt đầu thực hiện ngay trong phiên này, không dừng ở kế hoạch; không chờ tôi duyệt từng trang.

Repository: https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent
Nhánh duy nhất: main. Tôi cung cấp PAT riêng. Không chép PAT vào repo, file.env, remoteURL, script, nhật ký hoặc báo cáo; không in token ra màn hình. Dùng credential môi trường, hoặc truyền TNV_GIT_TOKEN vào môi trường tiến trình publish. Không tự spawn thêm agent.

1. Phân công và mốc tiếp quản

- Bạn CHỈ có trang 14, 15, 16, 17, 18, 19, 20, lane agent_a.
- Agent còn lại có 21–28, lane agent_b; không nhận việc hoặc sửa file của họ.
- Coordinator giữ01–13, sửa thoại cũ,4trang phụ,4mặt bìa, công cụ/nguồn chung, tích hợp state và ghép sách cuối. Không tự làm thay các phần này dù queue chung có việc todo/blocked.
- Mốc đã kiểm trước khi viết prompt: main18d65f4. Chủ dự án xác nhận chưa gửi việc cho A/B. PAGE04v003/PAGE12v003/PAGE13v002 là mẫu bóng thoại mới; sách chưa hoàn chỉnh, chưa sẵn in. Clone main MỚI NHẤT để lấy cả hướng dẫn/công cụ sau mốc này, không checkout ngược về18d65f4.
- Trạng thái lô bạn: TEXT14–18 đã done và có evidence; giữ nguyên nếu kiểm còn hợp lệ. ART/LAYOUT/QA14–18 chưa hoàn tất. Trang19–20 chưa hoàn tất TEXT/ART/LAYOUT/QA. Có23bước còn làm. Tác vụ đầu dự kiến PAGE14_ART; đọc next thực tế trước khi start.
- State chung đánh blocked các trang đã giao cho lane là để coordinator không nhận nhầm; đó không phải blocker của lane. Chỉ dùng state riêng để nhận việc. Khi khởi động muộn hoặc tiếp tục phiên, next/evidence trên main mới nhất có quyền hơn số liệu mốc trong prompt; không làm lại phần done hợp lệ.

2. Clone độc lập, đọc hồ sơ, kiểm môi trường

Tạo clone riêng; không dùng chung thư mục, working tree, Git index hoặc worktree với agent khác. Nếu tên thư mục đã tồn tại, kiểm tra nó thuộc đúng lane trước khi dùng; không xóa/reset để tạo chỗ. Chạy:

```bash
git clone --branch main --single-branch https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent.git tnv-agent-a
cd tnv-agent-a
git branch --show-current
git status --short
git pull --ff-only origin main
python -m pip install -r requirements.txt
```

Đọc theo thứ tự: AGENTS.md → START_HERE.md →10_agent_workflow/parallel/README.md → assignments.json → PROMPT.md trong thư mục lane →10_agent_workflow/WORKFLOW_A_TO_Z.md → PROJECT_STATUS.md → WORK_LOG.md/LESSONS_LEARNED.md chung để hiểu lịch sử → WORK_LOG.md/LESSONS_LEARNED.md và production_state.json RIÊNG của agent_a → SOURCE_DECISIONS.md toàn bộ → IMAGE_CATALOG.md → MASTER_ART_DIRECTION.md → SPEECH_STYLE_V2.md → storyboard/hồ sơ/scan liên quan đúng trang.

Các lệnh workflow.py trong tài liệu cũ dành cho coordinator; với phần được giao, bạn dùng wrapper này:

```bash
python scripts/parallel_workflow.py --lane agent_a doctor
python scripts/check_repo.py
python scripts/parallel_workflow.py --lane agent_a check
python scripts/parallel_workflow.py --lane agent_a status
python scripts/parallel_workflow.py --lane agent_a next
```

Nếu trạng thái vẫn như mốc, packet tác vụ đầu là:
```bash
python scripts/parallel_workflow.py --lane agent_a packet PAGE14_ART
```
Nếu next trả task khác do đã có tiến độ mới, packet task thực tế trong phạm vi bạn. Đọc BRIEF/evidence/ghi chú trước khi start. Prerequisite baseline/SOURCE_EPILOGUE trong state riêng là snapshot read-only; không mutate chúng.

3. Ranh giới file bắt buộc — chống đụng nhau

Chỉ được ghi:
-10_agent_workflow/parallel/agent_a/**: state riêng, WORK_LOG.md, LESSONS_LEARNED.md, HANDOFF.md, yêu cầu hỗ trợ và script riêng.
-assets_generated/parallel/agent_a/**: đầu ra phụ, bản gộp lô, helper/snapshot riêng.
-10_agent_workflow/tasks/PAGE##_TEXT/**, PAGE##_ART/**, PAGE##_LAYOUT/**, PAGE##_QA/**, chỉ với ## thuộc 14–20.
-assets_generated/raw_pages/PAGE##_... và assets_generated/speech_clouds/PAGE##_..., đúng số trang được giao, gồm PNG/prompt/request/metadata.
-final_book_19x24/source/PAGE##_..., proofs/PAGE##_..., reading/PAGE##_..., đúng số trang được giao.

Không ghi bất kỳ đường dẫn nào ngoài danh sách trên. Đặc biệt KHÔNG sửa AGENTS.md, START_HERE.md, scripts/, requirements, tests/, .github/, Ngăn03/07/09, fonts/, assignments.json, state/log chung, README chung của source, trang của agent khác hoặc sách gộp cuối. Không đổi tên/xóa/ghi đè artifact cũ: tạo v002/v003/... sau khi kiểm tên chưa tồn tại. Có thể cập nhật state/log đang sống của CHÍNH lane qua CLI.

Cần sửa renderer/thiết kế/nguồn chung: ghi REQUESTS.vNNN.md trong lane, nêu lỗi + file + cách tái hiện + giải pháp đề nghị. Dùng helper riêng nếu phù hợp mà không thay nguồn/công cụ chung; nếu chưa giải được thì block đúng task và tiếp tục việc độc lập. Không tự nhận quyền sửa file chung để “làm cho xong”.

4. Quy trình sản xuất và kiểm chữ

Với mỗi bước, dùng lệnh bên dưới; TASK_ID và REPORT_PATH phải thay bằng ID/đường dẫn thật, đúng lane và phiên bản chưa có:

```bash
python scripts/parallel_workflow.py --lane agent_a packet TASK_ID
python scripts/parallel_workflow.py --lane agent_a start TASK_ID --owner agent_a --note "Đầu vào đã đọc; đầu ra sẽ tạo"
python scripts/parallel_workflow.py --lane agent_a checkpoint TASK_ID --note "File thực đã có; lỗi còn lại; bước tiếp"
python scripts/parallel_workflow.py --lane agent_a finish TASK_ID --evidence REPORT_PATH --note "Các kiểm tra thực đã đạt"
```

Mỗi lane chỉ một task in_progress. Dùng lại chữ đã done/evidence còn đúng hash. TEXT chưa khóa: mở scan/storyboard, đối chiếu sự kiện/quan hệ/số lượng; lời dẫn35–65tiếng đếm theo khoảng trắng sau bỏ dấu **; giữ các cụm **từ khóa** và chép ĐỦ từng thoại/người nói. Đừng coi text.draft hoặc request cũ là thành phẩm. Nếu sửa chữ đã done trong lô mình, dùng reopen đúng task để mở lại downstream, giữ báo cáo và phiên bản cũ. Không sửa nguồn chung để né stale hash. Phân biệt truyện chuyển thể với lời nói lịch sử đã xác thực.

Lưu ý riêng của lô:
- Trang14: không khẳng định tuyệt đối “vĩ đại nhất” nếu nguồn không hỗ trợ; dùng chữ đã khóa.
- Trang15: diễn biến sau hơn10ngày; không vẽ lại việc xử tử như sự kiện mới đang xảy ra.
- Trang16: hơn100thuyền, mỗi thuyền16mái chèo; KHÔNG160thuyền. Hát Môn có đúng8voi đực da xám/ngà trắng trong cảnh nguồn quy định. Không suy mọi cảnh khác cũng có8voi.
- Trang17: bài vị cần chữ đọc được và đúng tên; giữ tranh thô riêng sạch chữ, ghép nhãn bằng nguồn sửa được. Nếu cần chức năng renderer chưa có, viết script riêng trong thư mục agent_a; không sửa scripts/ chung.
- Trang18: giữ đủ toàn bộ lời hịch đã khóa, không cắt để vừa trang.
- Trang19:27củ huyết sâm là chi tiết huyền tích; không khẳng định trẻ dùng hết27củ hoặc trình bày như kiến thức y học.
- Trang20:7bộ tộc Phượng Hoàng, không nhầm thành17tộc Mê Linh.
- Đô Năng Tế là nam trưởng bối có râu; Cẩm Nương là nữ trưởng bối; Trưng Nhị lam sẫm. Đọc đúng giai đoạn trang phục Trưng Trắc trước khi chọn hình trên sheet.

5. Tạo tranh thật, giữ nhận diện

Mở trực tiếp pixel ảnh active trong IMAGE_CATALOG và hồ sơ liên quan trước khi vẽ. Chọn đúng ô/người trong sheet nhóm, đúng giai đoạn trang phục, mặt/vóc dáng/màu/vũ khí. Dùng baseline hiện hành để tạo bản nháp; không tự thiết kế lại nhân vật. Dùng công cụ tạo ảnh thật; ghi nguyên văn prompt đã gửi, các ảnh THỰC SỰ truyền vào công cụ với đường dẫn/hash SHA-256, phiên bản, generator, kích thước native thực, hash đầu ra.

Tranh nền sạch chữ, không bóng thoại/khung thoại/watermark; chừa khoảng20% đỉnh thoáng cho lời dẫn. Đúng Template A/B/C. Kiểm mặt, ngón tay/tay/chân, dây cung và vũ khí nối đúng, vị trí người/vật theo nguồn, không che/cắt chi tiết chính. Không kéo méo ảnh; sửa bằng công cụ ảnh hoặc crop/clip đồng tỷ lệ có ghi tọa độ. Không lấy ảnh trang khác đổi tên làm tranh mới.

6. Khung và chữ thoại mới phải được VẼ CÙNG NHAU

Đây là yêu cầu trực tiếp của chủ dự án, thay hộp thoại trắng cũ. Xem PAGE04_v003, PAGE12_v003, PAGE13_v002 và SPEECH_STYLE_V2.md. Tạo bằng công cụ ảnh một asset có cả khung organic và ĐỦ chữ Việt bên trong, ví dụ PNG RGBA rồi đặt như một thành phần trong SVG/PDF. Khung/nét mực/màu giấy/ánh sáng phải hợp từng cảnh; đừng dùng một đám mây vàng cho mọi cảnh. Không dùng hộp trắng bo góc kiểu UI hoặc chỉ đặt chữ sans-serif máy móc lên hình trắng.

Chữ rõ, đủ dấu, không thư pháp khó đọc. Đuôi tự nhiên đến đúng người, tránh xuyên mắt/mặt/tóc/tay/vũ khí. Không cắt ngắn/sửa từ để vừa khung. Mở asset và bản ghép đọc từng tiếng/dấu; sai thì tạo phiên bản sửa. Giữ nguyên văn khóa trong JSON/prompt, PNG native và placement sửa được. Chỉ đặt status visual_text_verified sau khi đã đọc ảnh thật. PDF extraction không kiểm được chính tả chữ trong ảnh; cần kiểm thị giác riêng. Nếu tool từ chối câu bắt buộc, lưu lỗi và block đúng task, không né bộ lọc hoặc giả đã có ảnh.

Lời dẫn ghép riêng bằng khung giấy cổ; chữ đen, từ khóa đỏ son #C81E1E. Trim190×240mm, bleed196×246mm; tọa độ/safe zone theo layout_tokens.json. Mục tiêu in300DPI nhưng phải ghi độ phân giải native/hiệu dụng thật; đổi DPI hay render300 không làm tăng chi tiết gốc. Không tự chốt ICC/gáy/ISBN/PRINT_READY.

7. QA và evidence đủ để kiểm lại

Lưu raw, prompt/request, metadata/hash, chữ khóa, placement, nguồn SVG/PDF sửa được, PDF bản đọc, PDF proof, PNG render và báo cáo. Mở lại PDF không rỗng, kiểm font Việt nhúng/box, giải mã PNG thật rồi mở ảnh. Kiểm toàn trang ở kích thước đọc và zoom100%: nguồn, nhận diện, tay/chân/vũ khí, từng dấu tiếng Việt, keywords đỏ, tràn chữ, vùng an toàn và đuôi thoại. Chưa đạt thì giữ nháp/issue, không finish.

Report copy từ template, có reviewer/summary/checks/artifacts/open_issues/reviewed_at đúng sự thật. Không đưa file chung có thể thay đổi vào evidence bất biến; dùng snapshot riêng nếu cần. QA của bạn là AGENT_QA; không tự ghi USER_APPROVED hoặc PRINT_READY. Thiếu tool/renderer/nguồn bắt buộc thì block đúng ID với lý do/việc đã thử/cách tiếp tục; làm các task đủ điều kiện khác trong lô. Không giả đang có job nền sau timeout/ngắt phiên; chỉ tính file thật đã trả và mở kiểm.

8. Checkpoint và đẩy main sau từng phần — dùng duy nhất đường này

Sau mỗi kết quả kiểm được: checkpoint → ghi WORK_LOG.md riêng (file/version/lỗi/bước tiếp) → thêm bài học hữu ích vào LESSONS_LEARNED.md riêng → chạy:

```bash
python scripts/check_repo.py
python scripts/parallel_workflow.py --lane agent_a check
python scripts/parallel_workflow.py --lane agent_a guard
python scripts/parallel_workflow.py --lane agent_a stage
python scripts/parallel_workflow.py --lane agent_a publish --message "agent_a: checkpoint trang được giao"
```

Không git add ., git add -A, commit/push thủ công, tạo nhánh/PR, force-push, reset --hard, git clean hoặc chọn ours/theirs để bỏ việc người khác. Wrapper kiểm file bẩn VÀ commit chưa đẩy, commit phần đã stage, fetch/rebase main rồi push. Người khác push chen vào thì wrapper retry; đây không phải lỗi cần force. Sau push wrapper đối chiếu SHA local/remote; chỉ báo đồng bộ khi verified_local_and_remote_sha có thật.

Guard/check lỗi: sửa nguyên nhân trong phạm vi; không sửa checker để qua. Nếu conflict thật, wrapper abort rebase và giữ commit local; ghi đường dẫn/lý do/yêu cầu coordinator, không sửa file agent khác. Nếu mạng/quyền ghi lỗi, giữ commit và artifact, báo chưa push, không bịa SHA. Không giữ nhiều giờ ảnh chỉ trong cache: khi có output thật hãy lưu/push checkpoint ngay. Sau phiên ngắt, clone/pull sạch, chạy status/next và tiếp tục đúng lane.

9. Bàn giao và điều kiện dừng

Mục tiêu là 28bước của7trang, gồm5TEXT được kế thừa và23bước còn lại được kiểm hợp lệ. Làm tiếp cho tới hết task thực hiện được trong phạm vi; không hỏi lại sau từng trang. Không mở rộng sang việc của coordinator hoặc agent kia khi lô mình xong/bị chặn. Nếu tất cả việc còn lại đều blocked, ghi đủ lý do và các file đã cứu được rồi báo cáo thật.

Tạo10_agent_workflow/parallel/agent_a/HANDOFF.md và manifest trong lane: từng trang, phiên bản text/raw/speech/layout, đường dẫn source/PDF/PNG/report, SHA-256 artifact, check đã làm, nativeDPI, blocker và yêu cầu coordinator. Bản gộp lô nếu tạo phải đặt assets_generated/parallel/agent_a/, không ghi file sách gộp chung. Commit/push theo wrapper, trả GitSHA cuối trong tin nhắn bàn giao; đừng cố nhúng SHA của chính commit chứa HANDOFF vào nội dung HANDOFF.

Không chạy integrate_parallel.py, không gộp state/log chung hoặc ghép32trang/4mặt bìa. Coordinator sẽ kiểm và tích hợp. Báo cáo cuối ngắn: trang đã qua4bước, file thật, điểm còn thiếu, GitSHA đã xác nhận và phần chưa user-approved/print-ready. BẮT ĐẦU NGAY bằng kiểm main, cài dependency, status/next/packet và tạo đầu ra đầu tiên.
