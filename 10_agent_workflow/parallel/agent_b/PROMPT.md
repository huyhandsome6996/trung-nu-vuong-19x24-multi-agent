Bạn là AGENT B của dự án truyện minh họa TRƯNG NỮ VƯƠNG, khổ19×24cm, dành cho học sinh lớp8–10. Tôi giao bạn SẢN XUẤT TRỌN LÔ TRANG 21–28 theo TEXT→ART→LAYOUT→QA. Bắt đầu thực hiện ngay trong phiên này, không dừng ở kế hoạch; không chờ tôi duyệt từng trang.

Repository: https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent
Nhánh duy nhất: main. Tôi cung cấp PAT riêng. Không chép PAT vào repo, file.env, remoteURL, script, nhật ký hoặc báo cáo; không in token ra màn hình. Dùng credential môi trường, hoặc truyền TNV_GIT_TOKEN vào môi trường tiến trình publish. Không tự spawn thêm agent.

1. Phân công và mốc tiếp quản

- Bạn CHỈ có trang 21, 22, 23, 24, 25, 26, 27, 28, lane agent_b.
- Agent còn lại có 14–20, lane agent_a; không nhận việc hoặc sửa file của họ.
- Coordinator giữ01–13, sửa thoại cũ,4trang phụ,4mặt bìa, công cụ/nguồn chung, tích hợp state và ghép sách cuối. Không tự làm thay các phần này dù queue chung có việc todo/blocked.
- Mốc đã kiểm trước khi viết prompt: main18d65f4. Chủ dự án xác nhận chưa gửi việc cho A/B. PAGE04v003/PAGE12v003/PAGE13v002 là mẫu bóng thoại mới; sách chưa hoàn chỉnh, chưa sẵn in. Clone main MỚI NHẤT để lấy cả hướng dẫn/công cụ sau mốc này, không checkout ngược về18d65f4.
- Trạng thái lô bạn: Cả32bước TEXT/ART/LAYOUT/QA của21–28 chưa hoàn tất trong lane. Một số tệp nháp/request có sẵn không chứng minh đã khóa chữ hoặc có tranh hợp lệ. Tác vụ đầu dự kiến PAGE21_TEXT; đọc next thực tế trước khi start.
- State chung đánh blocked các trang đã giao cho lane là để coordinator không nhận nhầm; đó không phải blocker của lane. Chỉ dùng state riêng để nhận việc. Khi khởi động muộn hoặc tiếp tục phiên, next/evidence trên main mới nhất có quyền hơn số liệu mốc trong prompt; không làm lại phần done hợp lệ.

2. Clone độc lập, đọc hồ sơ, kiểm môi trường

Tạo clone riêng; không dùng chung thư mục, working tree, Git index hoặc worktree với agent khác. Nếu tên thư mục đã tồn tại, kiểm tra nó thuộc đúng lane trước khi dùng; không xóa/reset để tạo chỗ. Chạy:

```bash
git clone --branch main --single-branch https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent.git tnv-agent-b
cd tnv-agent-b
git branch --show-current
git status --short
git pull --ff-only origin main
python -m pip install -r requirements.txt
```

Đọc theo thứ tự: AGENTS.md → START_HERE.md →10_agent_workflow/parallel/README.md → assignments.json → PROMPT.md trong thư mục lane →10_agent_workflow/WORKFLOW_A_TO_Z.md → PROJECT_STATUS.md → WORK_LOG.md/LESSONS_LEARNED.md chung để hiểu lịch sử → WORK_LOG.md/LESSONS_LEARNED.md và production_state.json RIÊNG của agent_b → SOURCE_DECISIONS.md toàn bộ → IMAGE_CATALOG.md → MASTER_ART_DIRECTION.md → SPEECH_STYLE_V2.md → storyboard/hồ sơ/scan liên quan đúng trang.

Các lệnh workflow.py trong tài liệu cũ dành cho coordinator; với phần được giao, bạn dùng wrapper này:

```bash
python scripts/parallel_workflow.py --lane agent_b doctor
python scripts/check_repo.py
python scripts/parallel_workflow.py --lane agent_b check
python scripts/parallel_workflow.py --lane agent_b status
python scripts/parallel_workflow.py --lane agent_b next
```

Nếu trạng thái vẫn như mốc, packet tác vụ đầu là:
```bash
python scripts/parallel_workflow.py --lane agent_b packet PAGE21_TEXT
```
Nếu next trả task khác do đã có tiến độ mới, packet task thực tế trong phạm vi bạn. Đọc BRIEF/evidence/ghi chú trước khi start. Prerequisite baseline/SOURCE_EPILOGUE trong state riêng là snapshot read-only; không mutate chúng.

3. Ranh giới file bắt buộc — chống đụng nhau

Chỉ được ghi:
-10_agent_workflow/parallel/agent_b/**: state riêng, WORK_LOG.md, LESSONS_LEARNED.md, HANDOFF.md, yêu cầu hỗ trợ và script riêng.
-assets_generated/parallel/agent_b/**: đầu ra phụ, bản gộp lô, helper/snapshot riêng.
-10_agent_workflow/tasks/PAGE##_TEXT/**, PAGE##_ART/**, PAGE##_LAYOUT/**, PAGE##_QA/**, chỉ với ## thuộc 21–28.
-assets_generated/raw_pages/PAGE##_... và assets_generated/speech_clouds/PAGE##_..., đúng số trang được giao, gồm PNG/prompt/request/metadata.
-final_book_19x24/source/PAGE##_..., proofs/PAGE##_..., reading/PAGE##_..., đúng số trang được giao.

Không ghi bất kỳ đường dẫn nào ngoài danh sách trên. Đặc biệt KHÔNG sửa AGENTS.md, START_HERE.md, scripts/, requirements, tests/, .github/, Ngăn03/07/09, fonts/, assignments.json, state/log chung, README chung của source, trang của agent khác hoặc sách gộp cuối. Không đổi tên/xóa/ghi đè artifact cũ: tạo v002/v003/... sau khi kiểm tên chưa tồn tại. Có thể cập nhật state/log đang sống của CHÍNH lane qua CLI.

Cần sửa renderer/thiết kế/nguồn chung: ghi REQUESTS.vNNN.md trong lane, nêu lỗi + file + cách tái hiện + giải pháp đề nghị. Dùng helper riêng nếu phù hợp mà không thay nguồn/công cụ chung; nếu chưa giải được thì block đúng task và tiếp tục việc độc lập. Không tự nhận quyền sửa file chung để “làm cho xong”.

4. Quy trình sản xuất và kiểm chữ

Với mỗi bước, dùng lệnh bên dưới; TASK_ID và REPORT_PATH phải thay bằng ID/đường dẫn thật, đúng lane và phiên bản chưa có:

```bash
python scripts/parallel_workflow.py --lane agent_b packet TASK_ID
python scripts/parallel_workflow.py --lane agent_b start TASK_ID --owner agent_b --note "Đầu vào đã đọc; đầu ra sẽ tạo"
python scripts/parallel_workflow.py --lane agent_b checkpoint TASK_ID --note "File thực đã có; lỗi còn lại; bước tiếp"
python scripts/parallel_workflow.py --lane agent_b finish TASK_ID --evidence REPORT_PATH --note "Các kiểm tra thực đã đạt"
```

Mỗi lane chỉ một task in_progress. Dùng lại chữ đã done/evidence còn đúng hash. TEXT chưa khóa: mở scan/storyboard, đối chiếu sự kiện/quan hệ/số lượng; lời dẫn35–65tiếng đếm theo khoảng trắng sau bỏ dấu **; giữ các cụm **từ khóa** và chép ĐỦ từng thoại/người nói. Đừng coi text.draft hoặc request cũ là thành phẩm. Nếu sửa chữ đã done trong lô mình, dùng reopen đúng task để mở lại downstream, giữ báo cáo và phiên bản cũ. Không sửa nguồn chung để né stale hash. Phân biệt truyện chuyển thể với lời nói lịch sử đã xác thực.

Lưu ý riêng của lô:
- Trang21 là kế hoạch; trang24 là diễn biến thực. Không biến kế hoạch thành hình khẳng định toàn bộ đã xảy ra.
-600quân là tổng quân viễn chinh, không mặc định toàn bộ600người cùng lọt vào khe. Tào Quyền/Lục Hiến ở nhà gỗ khi bộ phận đuổi bắt vào khe Mãng Xà; không vẽ họ đồng thời ở nơi khác trái nguồn.
- Trang26: đúng5cọc,2tù binh có tên và3tướng vô danh. Không tự gán3người vô danh thành Sầm Lân/Sầm Bá/Độc Cô Tấn. Thánh Thiên giáp lục, khăn tang trắng, giày da báo. Phù hợp lứa tuổi, không thêm cảnh thương tích ghê rợn ngoài nguồn.
- Trang27–28: đọc SOURCE_EPILOGUE/report.v002.json, sources.v001.json và COMPARISON.v001.md. SRC-05 ở cuối SOURCE_DECISIONS giải quyết ghi chú SCOPE-01 cũ; đọc toàn file, không kết luận thiếu nguồn chỉ từ bảng đầu.
- Phân biệt sự kiện chính sử, chi tiết tiểu thuyết và hình tượng montage. Không khẳng định trận Phượng Hoàng trực tiếp mở đường về Luy Lâu nếu nguồn không hỗ trợ.
- Đền Hạ Lôi/Mê Linh và đền Hát Môn là hai di tích khác nhau. E14 là công trình tưởng niệm biểu tượng, không tự nhận tái dựng di tích khảo chứng.
- Mốc khởi nghĩa là năm40 theo nguồn đã đối chiếu. Sửa lỗi trong text phiên bản mới kèm source_notes; không sửa storyboard chung làm đổi hash các trang khác.
- Nếu cần bổ sung dữ kiện, tự mở nguồn chính thống và lưu URL/ngày truy cập/mệnh đề đối chiếu trong task của trang hoặc thư mục agent_b; không sửa hồ sơ nguồn chung.

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
python scripts/parallel_workflow.py --lane agent_b check
python scripts/parallel_workflow.py --lane agent_b guard
python scripts/parallel_workflow.py --lane agent_b stage
python scripts/parallel_workflow.py --lane agent_b publish --message "agent_b: checkpoint trang được giao"
```

Không git add ., git add -A, commit/push thủ công, tạo nhánh/PR, force-push, reset --hard, git clean hoặc chọn ours/theirs để bỏ việc người khác. Wrapper kiểm file bẩn VÀ commit chưa đẩy, commit phần đã stage, fetch/rebase main rồi push. Người khác push chen vào thì wrapper retry; đây không phải lỗi cần force. Sau push wrapper đối chiếu SHA local/remote; chỉ báo đồng bộ khi verified_local_and_remote_sha có thật.

Guard/check lỗi: sửa nguyên nhân trong phạm vi; không sửa checker để qua. Nếu conflict thật, wrapper abort rebase và giữ commit local; ghi đường dẫn/lý do/yêu cầu coordinator, không sửa file agent khác. Nếu mạng/quyền ghi lỗi, giữ commit và artifact, báo chưa push, không bịa SHA. Không giữ nhiều giờ ảnh chỉ trong cache: khi có output thật hãy lưu/push checkpoint ngay. Sau phiên ngắt, clone/pull sạch, chạy status/next và tiếp tục đúng lane.

9. Bàn giao và điều kiện dừng

Mục tiêu là 32bước của8trang được kiểm hợp lệ. Làm tiếp cho tới hết task thực hiện được trong phạm vi; không hỏi lại sau từng trang. Không mở rộng sang việc của coordinator hoặc agent kia khi lô mình xong/bị chặn. Nếu tất cả việc còn lại đều blocked, ghi đủ lý do và các file đã cứu được rồi báo cáo thật.

Tạo10_agent_workflow/parallel/agent_b/HANDOFF.md và manifest trong lane: từng trang, phiên bản text/raw/speech/layout, đường dẫn source/PDF/PNG/report, SHA-256 artifact, check đã làm, nativeDPI, blocker và yêu cầu coordinator. Bản gộp lô nếu tạo phải đặt assets_generated/parallel/agent_b/, không ghi file sách gộp chung. Commit/push theo wrapper, trả GitSHA cuối trong tin nhắn bàn giao; đừng cố nhúng SHA của chính commit chứa HANDOFF vào nội dung HANDOFF.

Không chạy integrate_parallel.py, không gộp state/log chung hoặc ghép32trang/4mặt bìa. Coordinator sẽ kiểm và tích hợp. Báo cáo cuối ngắn: trang đã qua4bước, file thật, điểm còn thiếu, GitSHA đã xác nhận và phần chưa user-approved/print-ready. BẮT ĐẦU NGAY bằng kiểm main, cài dependency, status/next/packet và tạo đầu ra đầu tiên.
