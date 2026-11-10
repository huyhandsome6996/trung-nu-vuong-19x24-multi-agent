---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
book_size: "190mm x 240mm (Bleed: 196mm x 246mm @ 300 DPI)"
target_audience: "Học sinh Lớp 8 - Lớp 10 (13-16 tuổi)"
compartment: "08_project_memory"
agent_author: "ChatGPT / Lead Agent (onboarding và rà soát QA)"
status: "IN_REVIEW"
source_grounding: "59 file tại commit 65c2e5a7cf71a1344be7f916c9b675e4325d31c8 và chỉ dẫn trực tiếp ngày 2026-11-09"
review_date: "2026-11-09"
timezone: "Asia/Ho_Chi_Minh"
---

# Nhật ký công việc

## 2026-11-09 — ONBOARDING-001

- **Yêu cầu:** nạp toàn bộ 7 ngăn; giữ form 19×24 cm; chưa tạo ảnh; ghi kết quả và kinh nghiệm lên repo.
- **Căn cứ:** 59 file gốc tại commit `65c2e5a7cf71a1344be7f916c9b675e4325d31c8` và chỉ dẫn trực tiếp của chủ dự án trong phiên.
- **Đã làm:** clone; đọc 26 Markdown + .gitignore; xem 32 ảnh; kiểm dải 58 trang scan và 28 storyboard; đo độ dài/cụm đỏ của lời dẫn; đối chiếu prompt, Bible và thông số bố cục.
- **Kết quả cụ thể:** đủ 7 ngăn, baseline 59 file; phân trang A=14/B=10/C=4; 11 lời dẫn vượt 65 đơn vị cách trắng, 11 trang quá 5 cụm đỏ, 14 trang quá tỷ lệ đỏ 35%. Phát hiện chênh lệch nguồn và quy chuẩn; xem [sổ vấn đề](../06_qa_validation_and_delivery/ONBOARDING_ISSUES.md).
- **Hồ sơ tạo mới:** báo cáo sẵn sàng, manifest/hash, bảng kiểm, danh mục vấn đề ở 06; form ở 05; README/nhật ký/quyết định/kinh nghiệm ở 08.
- **Giới hạn:** không có PDF gốc trong repo; chưa xác minh chính sử ngoài tài liệu dự án; chưa tạo ảnh hoặc thực thi chế bản.
- **Bàn giao:** chủ dự án chọn khóa 10 sheets hoặc ưu tiên bìa/trang 01; cần xử lý các vấn đề ảnh hưởng đầu ra trước sản xuất phần tương ứng.
- **Git:** bản cập nhật chuẩn bị trên `agent-06/qa-review`. Xem `git log` để lấy SHA của commit chứa chính nhật ký này; SHA không tự chèn vào file cùng commit. Trạng thái remote phải được xác nhận sau push, không suy ra từ dòng nhật ký.

## 2026-11-09 — ART-001 / Bắt đầu bảng nhân vật

- **Yêu cầu mới:** chủ dự án yêu cầu bắt đầu làm truyện sau onboarding; tiếp tục tuân thủ nguyên tắc nhân vật trước trang truyện.
- **Đã làm:** xem lại Bible, prompt Trưng Trắc và ảnh mẫu ngăn 07; sinh một sheet hai bộ trang phục bằng công cụ tạo ảnh tích hợp.
- **Đầu ra:** [Trưng Trắc v001](../assets_generated/characters/CHAR_01_Trung_Trac_v001.png), [metadata](../assets_generated/characters/CHAR_01_Trung_Trac_v001.json), [prompt và kiểm tra](../04_art_direction_and_image_prompts/production_logs/CHAR_01_Trung_Trac_v001.md).
- **Kiểm tra:** PNG giải mã được; hai khuôn mặt tương đồng; đủ hình toàn thân và đạo cụ; quan sát chưa thấy chữ hoặc watermark. Ảnh gốc 1122×1402 px, chưa gắn nhãn in 300 DPI.
- **Giới hạn:** mũ bên phải đi vào vùng 20% đỉnh; sheet không dùng làm trang ruột; chưa có góc quay sau/nghiêng; chưa được chủ dự án duyệt.
- **Tiến độ:** 1/10 sheets tạo, 0/10 duyệt; 0/28 trang truyện; các vấn đề onboarding chưa tự coi là được giải quyết.
- **Git:** nhánh `agent-04/art-assets-part-1`, kế thừa hồ sơ onboarding; commit và trạng thái push đối chiếu qua Git. Không có token trong ảnh, metadata hoặc tài liệu.
- **Bước tiếp:** chủ dự án duyệt/sửa Trưng Trắc trước khi dùng làm tham chiếu; tiếp tục các bảng theo cùng chất liệu.

## Mẫu ghi tiếp theo

- Mã việc / ngày / người thực hiện.
- Yêu cầu và nguồn đang dùng (file, phiên bản, trang).
- Đầu ra cụ thể và đường dẫn.
- Kiểm tra đã chạy, kết quả, giới hạn.
- Vấn đề còn mở và quyết định cần có.
- Bước tiếp theo, nhánh và commit bàn giao.

## 2026-11-09 — DESIGN-002 / Bộ thiết kế toàn bộ

- **Ủy nhiệm:** chủ dự án yêu cầu tự triển khai thiết kế đầy đủ, chi tiết thành phần, thống nhất và có hướng dẫn cho agent sau; không cần hỏi lại từng lựa chọn mỹ thuật thông thường.
- **Phạm vi:** 41 hồ sơ nhân vật; 12 bối cảnh; 36 nhóm đạo cụ/phương tiện; 4 động vật; 28 trang có bảng phụ thuộc; bộ SVG cho layout và token máy đọc.
- **Đã làm ở checkpoint đầu:** registry/profiles, prompt cho27 ảnh bổ sung, hướng dẫn nhập dự án, tóm tắt truyện2phút, quy chuẩn nét/màu/diễn xuất, sửa8 tài liệu cũ theo scan và hướng nhận diện.
- **Hình đang làm:** ảnh đã tạo được lưu dần có PNG/JSON/hash; xem IMAGE_CATALOG để có số thực tế, không lấy tổng số kế hoạch làm số hoàn thành.
- **Bản chuẩn sử dụng:** DESIGN_BASELINE để agent tiếp tục bản nháp nhất quán; chưa tự ghi chủ dự án duyệt từng ảnh hoặc ảnh in300DPI.
- **Kiểm:** validator kiểm ID, liên kết, file, kích thước/hash; `git diff --check`. Kết quả thị giác và giới hạn sẽ ghi riêng ở QA_DESIGN_REPORT khi đóng bộ.
- **Giới hạn còn lại:** biên tập lời dẫn dài, nguồn phần kết27–28, địa điểm đền, font/ICC/gáy in thuộc bước dựng sách tiếp theo.

### DESIGN-002 — Đóng bộ v1

- Hoàn thành30 bảng hiện hành:17 casting cho41 hồ sơ,1 turnaround,5 bối cảnh,4 đạo cụ,1 quân đội,1 động vật,1 bộ24 mặt tập thể.
- Đã thêm E13/E14 để trang28 có concept nền riêng; E14 là công trình tưởng niệm biểu tượng, không dùng làm ảnh xác minh một di tích thật.
- Sửa ảnh có mục tiêu: PROP04 v001→v002 (bỏ đèn kính/chi tiết yên ngoài thiết kế); PROP03 v001→v002 (huyết sâm đỏ đồng nhất). Giữ ảnh cũ, đánh SUPERSEDED và cập nhật album.
- Registry có41 người,24 mã tộc trưởng tập thể,14 cảnh,36 nhóm đạo cụ,4 động vật. Ma trận bao phủ28 trang; chưa sinh trang truyện.
- Mỗi ảnh mới có prompt, reference_paths thực tế, metadata kích thước/hash. Album30 preview nhẹ, bấm mở gốc; có HTML tìm theo tên/mã và nhóm; không dùng thư viện ngoài.
- Đã xem các bảng hình và khuôn SVG; chạy validator và kiểm link/file/hash. HTML chưa kiểm thị giác Chromium do thiếu binary, đã kiểm asset/cú pháp.
- Tiếp nhận từ `09_design_system/00_READ_FIRST.md` → SOURCE_DECISIONS → IMAGE_CATALOG → PAGE_ASSET_MATRIX → AGENT_HANDOFF. Chuẩn v1 dùng làm bản nháp theo ủy nhiệm, không tự ghi chủ dự án duyệt từng ảnh.
- Git: checkpoint đầu `00b65f2`; bản đóng bộ có commit tiếp theo trên `agent-04/art-assets-part-1`. Xem git log/remote để xác nhận SHA, không nhúng SHA của chính file này vào cùng commit.

## WORKFLOW-003 — Chuẩn hóa repo/main và vận hành A–Z (09/11/2026)

- Yêu cầu: tập trung main, một lối vào cho agent clone và thực hiện A–Z, có phục hồi sau ngắt phiên.
- Hợp nhất fast-forward toàn bộ lịch sử thiết kế/QA vào main, giữ nguồn và ảnh; thay hướng dẫn branch/PR đang vận hành. Các nhánh cũ chỉ dọn sau khi kiểm main remote chứa đủ commit.
- Tạo START_HERE, cập nhật AGENTS/README, thêm Ngăn 10 với quy trình, prompt giao agent, queue 125 task, ma trận công cụ/đầu ra, phục hồi và đổi phiên bản. Tạo packet PAGE01_TEXT thật với nguồn chữ và đường dẫn/hash ảnh ứng viên active.
- Thêm CLI doctor/status/next/packet/start/checkpoint/block/unblock/finish/reopen/check; evidence và dependency có kiểm. Thêm helper HTML proof từ chữ locked/ảnh/font thật, không tự coi là file in.
- Thêm check_repo, requirements, mẫu cấu hình GitHub Actions kiểm main (chưa kích hoạt) và 8 kiểm thử logic phục hồi/phụ thuộc/report/hash/stale source/ảnh native/path/keyword. Tests chạy đạt; check workflow/design/link/hash/whitespace đã đạt. GitHub từ chối kích hoạt CI vì PAT thiếu workflow scope; mẫu YAML được giữ ở Ngăn 10, không có workflow hoạt động. Bộ kiểm tra local đã chạy đạt.
- Sửa BOOK_STRUCTURE còn sót “78 voi” thành 8 voi đực da xám ở Hát Môn; không sửa 32 JPG nguồn. Đánh dấu riêng phân biệt QA pass/USER_APPROVED/PRINT_READY ở các đặc tả cũ.
- Phạm vi hoàn thành là hạ tầng vận hành và hợp nhất, chưa sinh 28 trang truyện hoặc file in. Queue ban đầu vẫn 2 baseline done, 122 todo, SOURCE_EPILOGUE blocked; bước tiếp PAGE01_TEXT. Thiếu công cụ/dữ liệu thì block đúng bước, không tự bịa kết quả.

- Giới hạn push đã xử lý: lần push đầu bị GitHub từ chối vì tạo workflow mà PAT không có workflow scope. Chuyển YAML thành mẫu trong Ngăn 10, sửa commit local chưa công bố để không yêu cầu quyền đó; không tìm cách vượt kiểm soát quyền GitHub.

### Kết quả đồng bộ WORKFLOW-003

- Main remote đã nhận commit3fec447, SHA local/remote khớp. Hai nhánh agent-04/art-assets-part-1 và agent-06/qa-review đã được xác nhận là tổ tiên của main rồi xóa trên remote và local; toàn bộ lịch sử vẫn nằm trong main.
- Tạo một bản clone sạch từ commit main đã lưu, chạy check_repo và8tests đều đạt; next chọn PAGE01_TEXT, packet sinh lại không làm bẩn working tree. Đây là kiểm bản clone local, không phải khẳng định đã tải và kiểm trên mọi máy.
- CI tự động chưa kích hoạt do token thiếu workflow scope; mẫu cấu hình sẵn ở Ngăn10. Các lệnh kiểm local dùng được đầy đủ.

## CI-004 — Kích hoạt kiểm tra GitHub Actions (09/11/2026)

- Chủ dự án cấp thông tin xác thực mới để xử lý giới hạn quyền workflow ở phiên trước. Chỉ dùng xác thực tạm trong tiến trình; không lưu token vào repo/remote/log.
- Đưa cấu hình đã chuẩn bị vào .github/workflows/validate-main.yml, cập nhật tài liệu vận hành và liên kết kết quả chạy. Workflow có quyền contents:read, chạy Python3.11, cài Pillow, chạy8tests và check_repo khi push main hoặc workflow_dispatch; không tự gọiAI hay ghi repo.
- Báo cáo trước về thiếu quyền là lịch sử ở thời điểm đó. Kết quả chạy mới được ghi sau khi kiểm Actions thực tế; không suy thành công chỉ từ việc push file YAML.

### CI-004: kết quả đã xác nhận

- GitHub Actions thực chạy thành công cho commit `583590432e22a1e47510be78dc66c935bb81bda2`: [run 42610672432](https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent/actions/runs/42610672432). Đã chạy cài dependency, 8 unit tests và check_repo trên runner GitHub; không chỉ kiểm local.
- Thông tin xác thực mới giải quyết giới hạn workflow trước đây. CI có hiệu lực trên main; token chỉ dùng tạm khi push và đọc trạng thái, không lưu trong file dự án.

## PROD-005 — Sản xuất trang01 (09/11/2026)

- Tiếp quản bản main sạch, pull thành công; cài Pillow12.3, doctor/check_repo/status/next/packet đạt. Queue ban đầu2done/1blocked/122todo.
- Đã mở scan06–07, CHAR12 và ENV01; đọc hồ sơNV21/NV22 và E01/E02. Khóa text.v001:59tiếng,5cụm đỏ, không thoại, TemplateB; có nhãn huyền tích để không biến niên đại tiểu thuyết thành sử liệu.
- PAGE01_TEXT đã finish có report và đối chiếu nguồn. PAGE01_ART đang làm với ảnh tham chiếu thực CHAR12/ENV01; chưa gọi là bản in hoặc người dùng duyệt.
- Bước tiếp: lưu nền native và hash, kiểm thị giác, ghép chữ rồi QA.

### PROD-005 — Đóng chuỗi trang01

- Trang01 đã có TEXTv002(50tiếng/5cụmđỏ/0thoại), ARTv002 native1120×1405, SVG sửađược, PDFbleed/PDFđọc vàPNG render thực.
- Kiểm font thật phát hiện chữv00159tiếng quá hộp29mm; đã reopen đúng chuỗi, rút câu nối rồi finish lạiTEXT/ART. LAYOUTv001 lộ mất khoảngtrắng sát từkhóa; đã sửa parser và dùngLAYOUTv002, giữv001.
- Đã xem toàntrang150DPI và crop100% từrender300DPI; fontViệt nhúng,4dòng12.8pt, nguồn/nhậndiện/hìnhhọc đạt bảnđọc. Native tranh khoảng145DPI, chưain300DPI.
- Push checkpoint trước dùngcache credential bị môi trường từchối kết nối daemon; commit6ce03be đãlưu local nhưng chưađồngbộ ở mốc đó. Dùng credential tạm trong tiếntrình đểpush tiếp, không ghi tokenvàofile.
- Bước tiếp: đóngQA, hoànthiện nguồn27–28, rồiPAGE02_TEXT.

## SRC-006 — Bổ sung nguồn phần kết (09/11/2026)

- Đã mở và đọc bài tổng quan của Bảo tàng Lịch sử Quốc gia cùng hai hồ sơ di tích của Cục Di sản văn hóa. Lưu URL, ngày truy cập, phạm vi hỗ trợ và đối chiếu từng mệnh đề tại SOURCE_EPILOGUE.
- Sửa storyboard27–28: bỏ khẳng định tuyến hành quân Phượng Hoàng trực tiếp mở đường về Luy Lâu; phân biệt Mê Linh/Hát Môn; giữ E14 là công trình tưởng niệm biểu tượng. Giữ bản storyboard trước sửa. Chưa khóa chữ27–28.
- Check_repo đạt trước finish SOURCE_EPILOGUE. Trang01 đã push c5e4572 và đối chiếu remote khớp. Trang02 đã khóa chữ51tiếng,5cụm đỏ, không thoại; đang tạo tranh với5ảnh tham chiếu thực đã xem.

## PROD-007 — Trang02–03 và kiểm metadata (09/11/2026)

- Trang02 hoàn thành TEXT/ART/LAYOUT/QA cho bản đọc. Giữ v001/v002; bố cục cuối dùng clip vector từng khung đã chọn thủ công, không sửa pixel hoặc kéo méo. Có SVG, PDFbleed, PDFđọc, PNG và thông số crop/DPI đo được.
- Trang03 hoàn thành TEXT/ART/LAYOUT/QA:6cụm đỏ,1thoại đầy đủ, TemplateC,5nhân vật đúng sheet. Đã kiểm toàn trang và crop300DPI; bóng thoại chỉ Tô Định và không che mặt/tay trao hổ phù.
- Trang04 đã khóa chữ49tiếng/1thoại; tranh v001 đẹp nhưng cần chừa thêm vùng thoại, đang chờ bản sửa v002, input/prompt đã lưu.
- Phát hiện một metadata lấy prompt trước lúc kết quả async hoàn tất nên ghi placeholder; đã reopen đúng chuỗi02, giữ hồ sơ cũ, tạo metadata/promptv003 đúng nguyên văn, finish lại bằng hash ảnh và thành phẩm không đổi. Thêm guard và kiểm thử ngăn finish với placeholder.
- Tách script kết xuất dùng chung khỏi evidence bất biến của trang01: lưu snapshot render_page.v001.py có cùng byte; thành phẩm01 không đổi. Trang02 dùng snapshotv002 và placementJSON riêng.
- Bước tiếp: hoàn thiện vùng thoại04, tiếp tục PAGE05_TEXT. Chưa tạo đủ28trang; không báo hoàn tất sách.

## PROD-008 — Sáu trang đầu có bản đọc kiểm được (09/11/2026)

- Trang04–06 đã hoàn thành chuỗi TEXT→ART→LAYOUT→QA. Hiện6/28trang truyện có bản đọc và nguồnSVG/PDF/PNG; bảng phiên bản cập nhật trong final_book_19x24/source/README.md.
- Tạo PDF checkpoint6trang đầu và manifest hash; chưa có trang phụ/bìa, không gọi sách hoàn chỉnh.
- Trang05 có trích thư ghép dạng giấy, không gán thoại cho người trong cảnh; clipvector giữ cánh/mũ. PDFproofv001 bị phát hiện rỗng nên không dùng; rendererv003 ghi qua tệp tạm, v002 đã mở lại và render kiểm.
- Trang06 giữ nguyên bộ tía/hổ phù, đủcung/thương; cliptrim giữ trọnủng, lớpbleed làbảnxem chưain.
- Trang07–08 đã khóa chữ, tranhv001 có lỗi thực (dâycung; ủngđứngngoàiyên/đỉnhthiếukhoảngtrống), đãlưu bản cũ và yêu cầu sửa bằngcôngcụảnh. Đang chờ job110/112, khôngđánhdấupass.
- Côngcụảnh chỉ nhận tốiđa5đườngdẫn: request07v0016ref bịtừchốitrướcsinh; requestv0025ref mới làlệnh thực. Metadata ghi đúng5ảnh thực dùng.
- Bước tiếp: kiểm bản sửa07–08; tiếp tục trang09. PRINT_SPEC vẫn blocked do thiếu nhàin/quyền và tranh native dưới300DPI.

## 2026-11-09 — Recovery and pages07–08 checkpoint

- Remote93095a2 retained six completed pages. Recovered seven raw outputs for07–12 from surviving session files; archived unchanged under assets_generated/recovered_session.
- PAGE07 fresh logged v004 retains corrected bowstring and minor soldier turned away; finished LAYOUTv002/QA. Taller TemplateB upper panel preserves bow and quote. PAGE08 recovered v002 exact edit prompt and input path available; finished LAYOUT/QA v001.
- Opened both final renders, verified fonts and full quote/page07. Eight-page reading checkpoint and manifest created.
- Original prompts for09–12 were not committed; do not invent them. Keep recovered outputs pending and use in fresh logged tool calls before ART acceptance. Continue09TEXT. Printer remains blocked.

## 2026-11-09 — Pages09–12 verified; text13–18 locked

- Fresh logged reference-based renders replace unauditable recovered prompt provenance for09–12. All four pages finished TEXT→ART→LAYOUT→QA. Exact full PDF dialogue, embedded Noto fonts and geometry checked; every final render opened. Rejected larger balloon09 and tails11/12 retained in earlier versions.
- Twelve-page reading checkpoint created with source SVG, raw PNG, placement JSON, proofs/reports. Native raster remains below300DPI; not print-ready/user-approved.
- TEXT13–18 locked against scans32–42. Corrected unsupported superlative14, chronology15 (>10days), and16: source says morethan100boats;16is oars perboat, not160boats. No storyboard-file mutation that would invalidate earlier locks.
- Six exact requests13–18 saved, baseline pixels viewed; image calls pending. Continue returned outputs and complete layouts; do not mark timeout as success without actual file/pixel review.

## 2026-11-10 — Resume from verified remote dc5b152

- Re-cloned main after environment reset. Verified remote retains12completed pages and TEXT01–18. Later local-only work/commit from the interrupted session was not pushed; do not count it as delivered.
- Generated-image cache and available saved files did not contain the later13–24 outputs. Retain committed requests, restart image generation with explicit new versions. No pending background generation is assumed alive.
- Source27–28 remains verified; their TEXT tasks still need finishing in queue. Continue PAGE13_ART first, push each completed page.

## 2026-11-10 — User-requested illustrated speech, page12v003

- User rejects modern white rounded rectangles and straight tails. Created actual RGBA lettered-cloud artwork with image_gen:2172×724px, matching warm ink/watercolor scene. Exact3-line Vietnamese quote manually verified.
- NewPAGE12_LAYOUT/QA v003 use separate editable-placement SVG and native cloud with lettering already drawn inside; raw illustration remains textfree. Oldv002 retained. Caption unchanged, tail onmouthcorner and faces/hands unobscured. Not user-approved/print-ready.
- Parallel handoff being prepared under new user authorization: coordinator01–13/covers/matter/assembly, A14–20, B21–28. Per-lane progress/logs and staged-path gate will prevent shared-file editing.

## 2026-11-10 — Two external agents, disjoint main-only publication

- Saved exact handoff prompts: AgentA14–20, AgentB21–28. Coordinator retains01–13, legacy speech restyle, covers/matter/assembly and shared files. Delegated unfinished global tasks are blocked with lane pointers; each lane has its own queue, logs and immutable prerequisite evidence.
- Added file-scope guard, guarded staging, main-only fetch/rebase/push retry and matching-head verification. Shared source/design/registry/fonts/tools are read-only to lanes. Agents cannot mutate global tasks through the standard queue. Coordinator imports only a completed, verified lane.
- Ran15 tests successfully, including a real bare Git remote and two independent clones publishing commits from the same base; both results survived the rebase and only main existed. Scope/deletion/foreign-file and full dependency-graph checks passed. check_repo and both lane evidence checks passed. This does not replace content/visual QA or protect against an agent deliberately bypassing the workflow.
- Reopened LAYOUT/QA03,04,06,07,09,10,11 for the newly requested illustrated lettering. Old12-page PDF is a historical draft; PAGE12v003 is the corrected sample. PAGE13_ART paused before generation while user feedback/handoff was handled; no background image job is claimed.

- PAGE13 actual fresh rawv002 saved1122×1402 with submitted prompt/5ref hashes. Figure identities/anatomy reviewed; top sword enters caption zone, so ART remains in_progress. Exact composition editv003 prepared, no success claimed before returned file.

- PAGE13_ART v003 actual recompose returned and visually passed: sword fully below30percent, caption area clear, white mourning/normal hands and full boots. Saved native1122×1402, exact submitted prompt/refs/hash; began drawn-lettering LAYOUT with full locked quote.

- PAGE13_LAYOUT/QA v002 finished after reopening real PDF/PNG: complete4line illustrated quote, warm organic cloud with full lettering drawn inside, tail adjusted to mouth corner. Noto narrator4lines/5redphrases, exact51tokens; bleed196×246/trim190×240 and embeddedfonts checked. Raw144.76DPI/speech461.62DPI; agent-reviewed only. Seven legacy speech pages still reopened; no full-book completion claimed. Saved editableSVG/placement/exactprompt/raw/meta/QA and immutable renderv004 snapshot.

## 2026-11-10 — Continued after status question

- Fetched remote: still6aeb79f, no newer A/B commits visible. Started PAGE03 speech restyle. Actual image call rejected HTTP400 moderation_blocked/violence (output stage); no output. Preserved exact locked quote and request/error, blocked layout, continuing independent PAGE04. No running image job remains from the rejected request.

- PAGE04_LAYOUT/QA v003 completed with actual illustrated cloud+letteringv002, exact3line quote and RGBA/nativeprompt/hash. Opened final render: all three faces/hands clear, tail reaches Phùng. PDF geometry/fonts/narration checked. PAGE03 remains toolblocked; independent06/07/09/10/11 restyle remains.

## 2026-11-10 — Expanded two-agent prompts before launch

- User explicitly confirms neither external agent has been sent the assignment yet. Verified remote production checkpoint18d65f4 and queues: A has TEXT14–18 done/23steps todo; B has32steps todo; SOURCE_EPILOGUE done. Coordinator retains01–13/covers/matter/assembly; no page ownership changes.
- Preserved old promptsv001 and saved full standalone promptsv002/currentPROMPT.md for each lane: exact startup/read order, allowed/forbidden paths, private queues/logs, source pitfalls, drawn-lettering standard, evidence/QA, timeout/rejection handling, guarded publication, final manifest and integration boundary.
- Hardened publish to inspect every unpublished local commit as well as staged/unstaged/untracked paths; an already-committed foreign edit in a clean tree is rejected before rebase/push. Added real-Git regression tests for that case and for A pushing between B fetch/push, causing a real non-fast-forward rejection followed by successful retry.17tests pass; both results survive and main-only history remains.
- No new illustration or full-book completion is claimed in this handoff preparation. PAGE03 image rejection stays a coordinator blocker; independent speech06/07/09/10/11 and all covers/matter remain coordinator work.
