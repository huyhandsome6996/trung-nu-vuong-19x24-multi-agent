# Lệnh trực tiếp cho Agent 5: sửa PDF theo góp ý giáo viên

Bạn là Agent 5 trong đợt sửa truyện TRƯNG NỮ VƯƠNG. Bắt đầu làm thật ngay trong phiên này, làm từ đọc nguồn → sửa chữ/tranh → dàn trang → QA → commit/push, không chỉ phân tích hoặc đưa prompt cho người khác. Không hỏi lại các lựa chọn thường nhật đã quy định.

REPO: https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent
NHÁNH DUY NHẤT: `sua-theo-gop-y-giao-vien` (tên tiếng Việt không dấu).
NGĂN GIAO VIỆC: `11_sua_theo_gop_y_giao_vien/`.
LANE CHỈ ĐƯỢC GHI: `11_sua_theo_gop_y_giao_vien/04_agents/agent_5/`.
TRANG BẠN SỞ HỮU: PDF18, PDF19, PDF20, PDF21. Đây là số trang PDF vật lý, bìa=01, tổng21; không phải bộ28 trang trong workflow cũ.

## 1. Lấy đúng nhánh rồi đọc

Clone riêng, không dùng chung thư mục làm việc với agent khác. Repo public có thể đọc không cần token. Nếu dùng clone mới:

```bash
git clone --filter=blob:none --no-checkout --single-branch --branch sua-theo-gop-y-giao-vien https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent.git trung-nu-vuong-agent_5
cd trung-nu-vuong-agent_5
git sparse-checkout init --no-cone
git sparse-checkout set '/AGENTS.md' '/README.md' '/START_HERE.md' '/11_sua_theo_gop_y_giao_vien/' '/01_source_material_analysis/' '/03_storyboards_and_scripts/' '/09_design_system/SOURCE_DECISIONS.md'
git checkout sua-theo-gop-y-giao-vien
```

Lệnh trên chỉ lấy gói sửa và các tài liệu chữ cần thiết, tránh tải toàn bộ tài sản thiết kế cũ. Nếu máy chủ không hỗ trợ lọc blob, vẫn giữ sparse-checkout và checkout đúng nhánh. Không mở ảnh thiết kế cũ của repo để làm nền. Với clone có sẵn, bảo toàn thay đổi đang có, fetch và switch đúng nhánh; không reset --hard.

Đọc theo thứ tự: AGENTS.md đầu repo (đã có ngoại lệ cho nhánh này) → ngăn 11/README.md → ngăn 11/AGENTS.md → 02_quy_chuan/NGUYEN_TAC_SUA.md → 02_quy_chuan/GOI_Y_THOAI.md → 04_agents/agent_5/BRIEF.md → các03_nhiem_vu_tung_trang/PDF_XX.md của bạn. Mở trực tiếp JPEG nguồn của từng trang và ảnh khoanh tương ứng. PDF gốc là `01_nguon_bat_bien/ban_goc_gemini.pdf`; tất cả đường dẫn ngắn này nằm dưới ngăn 11. 4 ảnh trang phục người dùng gửi cũng đã có trong nguồn. Không cần nhờ người dùng gửi lại các đầu vào này.

Chỉ thị mới ngày12/11/2026 của chủ dự án ưu tiên hơn luật main-only/phân côngA-B cũ. Không chạy queue28 trang cũ, không sửa main, không dùng thiết kế cũ thay hình Gemini. Tất cả 5 agent cùng nhánh sửa nhưng ghi file ở5 lane riêng. Không tự tạo nhánh khác hoặc mở việc ngoài phạm vi.

## 2. Sửa đúng các trang sau

- PDF18: Thêm thoại Thánh Thiên/địch đúng cảnh, thể hiện chủ động dụ địch và sự chủ quan của giặc; không cho địch biết trước toàn bộ bẫy.; Giữ nhận diện Thánh Thiên đã quy định, sửa phục trang quân Lĩnh Nam và rà cờ, ô vàng.
- PDF19: Khung dưới đã khoanh: thêm thoại Tào Quyền/Lục Hiến hoảng sợ, tìm cách chuồn; thêm lời nghĩa quân vạch rõ đã bị vây/bắt, cho thấy trí mưu của đội quân Thánh Thiên.; Rà trang phục lính bắt giặc; giữ hai khung và hành động, không biến cảnh thành trò hề quá mức.
- PDF20: Dàn lại nguyên cụm “Trảm thủ!” cùng dòng, tuyệt đối không để “thủ!” rơi riêng dòng cuối.; Thay cờ trang này và kiểm đồng bộ cờ trang sau PDF21.; Giữ mặt Thánh Thiên đồng bộ; rà trang phục lính. Không bổ sung hình chém đầu trực diện.
- PDF21: Thay cờ toàn cảnh, kể cả cờ nhỏ xa; đồng bộ với các trang trước.; Sửa trang phục nghĩa quân/Hai Bà; giữ hai voi, đoàn quân và bố cục kết Gemini. Nếu có Thánh Thiên, dùng khóa nhận diện mới.; Thu gọn ô vàng và rà chữ cuối sách; không tự thêm trang hoặc chuyển thành bộ truyện 28 trang.

Tất cả trang đều phải rà ô vàng cho gọn, chữ không lẻ dòng, cờ và trang phục đúng quy chuẩn chung. Giữ bố cục, phong cách Gemini và nội dung ngoài phạm vi sửa. Không chỉ sửa đúng chỗ khoanh rồi bỏ qua cờ nhỏ/trang phục phía xa. Mẫu cờ đỏ đất trơn và khóa mặt/trang phục Thánh Thiên đã ghi sẵn để5 lane đồng bộ. Các mẫu là quy ước minh họa, không tuyên bố khảo chứng lịch sử.

## 3. Làm thành sản phẩm thật

Sử dụng công cụ chỉnh/tạo ảnh có ảnh gốc làm tham chiếu cho sửa cờ, trang phục, nền, gương mặt. Giữ hình gốc ngoài vùng sửa; không vẽ code đè hình học thô lên nhân vật/cờ. Phần chữ có thể dàn riêng bằng font Việt để dễ sửa và kiểm chính tả. Không tạo lại toàn trang tùy hứng, không đổi số khung hay tự viết cốt truyện khác. Thoại bổ sung là lời chuyển thể phù hợp sự kiện, không gán thành trích dẫn lịch sử.

Mỗi trang xuất đủ trong lane: `text/PDF_XX.json`, nguồn chỉnh sửa tái tạo được dưới `source/`, `output/PDF_XX.png`, `output/PDF_XX.pdf` một trang, `qa/PDF_XX.json` theo TEMPLATE.json. Chữ cuối cùng và người nói phải đọc được từ file text. Giữ MediaBox430,08×576pt của PDF nguồn, không kéo méo sang19×24 chỉ vì tên repo. Ảnh nguồn896×1200, không nâng nhãn DPI rồi gọi đã đạt in 300 DPI. Mở PNG sửa, render PDF và kiểm bằng mắt trước PASS.

Sau mỗi trang, cập nhật STATUS.json/WORK_LOG.md trong lane và commit checkpoint đã kiểm. Khi xong lô, xuất `output/LO_TRANG.pdf`, `HANDOFF.md`; agent 4 còn xuất ảnh khóa Thánh Thiên theo BRIEF. Agent5 đối chiếu reference lane 4 khi đã có, ghi trung thực nếu kiểm liên lane còn PENDING. Thiếu công cụ ART thì ghi BLOCKED_ART đúng trang, làm trước chữ/nguồn độc lập còn làm được; không nhận đã hoàn thành tranh chỉ vì đã viết prompt. Không xóa bản gốc hoặc ghi đè file lane khác.

## 4. Kiểm và đẩy an toàn

```bash
python3 11_sua_theo_gop_y_giao_vien/06_cong_cu/check_packet.py
python3 11_sua_theo_gop_y_giao_vien/06_cong_cu/validate_lane.py agent_5 --ready
git add -- 11_sua_theo_gop_y_giao_vien/04_agents/agent_5/
python3 11_sua_theo_gop_y_giao_vien/06_cong_cu/validate_lane.py agent_5 --staged
git diff --cached --check
git commit -m "sua giao vien: agent_5 hoan thanh lo trang"
git fetch origin sua-theo-gop-y-giao-vien
git rebase origin/sua-theo-gop-y-giao-vien
git push origin HEAD:refs/heads/sua-theo-gop-y-giao-vien
```

Chỉ dùng --ready khi thực sự đã có đủ output; checkpoint đang dở vẫn có thể commit/push, ghi rõ trạng thái, không gọi là xong. Nếu push bị từ chối vì agent khác vừa đẩy: fetch/rebase lại và thử lại; không force-push, không đổi lane, không sửa state/file chung để qua check. Dùng xác thực an toàn do môi trường hoặc người dùng cấp riêng; không đưa PAT vào prompt/file/URL/commit. Nếu chưa có quyền push thì vẫn hoàn thiện file và bàn giao commit/ZIP rõ giới hạn, không khai đã đẩy.

Sau push, kiểm commit của bạn là tổ tiên của đầu nhánh remote (HEAD remote có thể đã tiến do agent khác). Chỉ báo thành công khi commit đã hiện trên nhánh remote. Trả lại: trang hoàn thành, các file thật, commit/link nhánh, kiểm đã chạy, phần còn BLOCKED hoặc cần coordinator rà liên trang. Bạn không chịu trách nhiệm ghép cả21 trang; coordinator sẽ ghép sau khi cả 5 lane đủ điều kiện.

Đọc thêm `02_quy_chuan/DAU_RA_VA_QA.md` trong ngăn sửa để dùng đúng schema chữ, QA, evidence và trạng thái READY_FOR_COORDINATOR.
