Bạn là AGENT_B của dự án truyện minh họa TRƯNG NỮ VƯƠNG19×24cm, dành cho lớp8–10. Tôi giao bạn hoàn thành RIÊNG trang21–28; bắt đầu sản xuất ngay. Coordinator giữ01–13, sửa thoại cũ, bìa, trang phụ và ghép sách; agent còn lại có phạm vi khác. Không tự mở rộng việc.

Repository: https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent
Làm trực tiếp trên main, không nhánh/PR. PAT tôi cung cấp riêng chỉ dùng trong tiến trình Git, không lưu vào repo, URL hay nhật ký.

Đọc AGENTS.md → START_HERE.md → 10_agent_workflow/parallel/README.md → assignments.json → PROMPT.md của lane → WORKFLOW_A_TO_Z.md → WORK_LOG riêng → SOURCE_DECISIONS.md → SPEECH_STYLE_V2.md. Quy trình lane là phân công hiện hành được chủ dự án cho phép; không dùng queue/global log cũ để nhận việc của người khác.

Tạo clone RIÊNG theo tên bên dưới; không dùng clone/index của coordinator hay agent kia. Cài requirements, chạy doctor, check_repo, status, next và packet bằng CLI lane. Tiếp tục việc đủ điều kiện trong phạm vi đến khi hết lô, không dừng ở kế hoạch, không chờ duyệt từng trang.

Sản xuất TEXT→ART→LAYOUT→QA. Chữ đã done có evidence thì dùng lại; chữ chưa khóa phải đối chiếu scan,35–65tiếng lời dẫn, giữ keyword và đủ nguyên văn thoại. Xem trực tiếp pixel ảnh baseline và hồ sơ nhân vật trước khi sinh; dùng công cụ ảnh thật, lưu prompt thực/actual_references+SHA và native pixels, không bịa kết quả.

YÊU CẦU MỸ THUẬT MỚI: bóng thoại và chữ Việt phải được VẼ CÙNG NHAU, hợp nét mực/màu nước và ánh sáng bối cảnh; hình mây/oval organic, đuôi ngắn cong đến đúng góc miệng, chữ rõ đủ dấu nằm gọn bên trong. Xem mẫu PAGE12_v003 và SPEECH_STYLE_V2.md. Không dùng hộp trắng bo góc kiểu UI, không đặt chữ sans-serif máy móc lên hình trắng. Có thể sinh asset RGBA chứa cả khung+chữ, đặt như một thành phần trong SVG/PDF; kiểm từng chữ/dấu trên ảnh. Tranh thô giữ riêng sạch chữ; lời dẫn giấy cổ, chữ đen và keyword đỏ#C81E1E theo layout_tokens. Không che mặt/tay/vũ khí, không kéo méo ảnh. Trim190×240mm,bleed196×246mm; không gọi ảnh145DPI thành300DPI.

CHỐNG ĐỤNG FILE: chỉ ghi task/art/proof/source/reading của đúng trang được giao và thư mục lane riêng theo README. Nhật ký và kinh nghiệm ghi vào WORK_LOG.md/LESSONS_LEARNED.md của lane. Không sửa production_state/WORK_LOG/LESSONS chung, storyboard, scan, registry, design, font, script chung, assignments hay trang người khác. Cần thay công cụ/nguồn dùng chung thì ghi yêu cầu trong lane và tiếp tục việc độc lập. Giữ bản cũ, tạo version mới. Thiếu công cụ thì block đúng task, không giả QA.

Sau MỖI kết quả nhỏ, checkpoint kèm file/lỗi/bước tiếp; stage/publish bằng lệnh dưới. Không git add .; không force-push/reset --hard, không tự giải conflict bằng ours/theirs. Publish đã có gate quyền file và fetch/rebase/retry, tự đối chiếu SHA local/remote. Truyền PAT qua biến môi trường tiến trình TNV_GIT_TOKEN nếu môi trường chưa có credential; tuyệt đối không ghi token vào file. Nếu conflict thật ngoài dự kiến, giữ commit và báo trong lane; không sửa file người khác.

Chỉ ghi agent đã QA, không tự ghi USER_APPROVED/PRINT_READY. Khi hoàn tất lô: ghi HANDOFF.md trong lane, liệt kê từng trang/version/file/SHA, kết quả QA và blocker; lane check phải pass. Không ghép sách toàn bộ và không nhập state chung, coordinator sẽ kiểm rồi tích hợp.

Lưu ý nguồn:21kế hoạch và24diễn biến phải phân biệt;600là tổng quân viễn chinh, TàoQuyền/LụcHiến ở nhà gỗ khi bộ phận đuổi bắt vào khe MãngXà. Trang26 đúng5cọc,2tù binh có tên+3tướng vô danh, không gán thành SầmLân/SầmBá/ĐộcCôTấn. ThánhThiên giáp lục, khăn tang trắng, giày da báo. Nguồn bổ sung27–28 đã được lưu ở SOURCE_EPILOGUE: đọc đối chiếu rồi khóa chữ; montage hợp quân và đềnE14 là hình tượng, không phải đội hình/di tích khảo chứng. Không sửa storyboard chung để sửa lỗi Năm40; sửa trong text phiên bản mới có source_notes.

Lệnh khởi động (chạy từ gốc clone sau khi cd):

```bash
git clone --branch main --single-branch https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent.git tnv-agent-b
cd tnv-agent-b
python -m pip install -r requirements.txt
python scripts/parallel_workflow.py --lane agent_b doctor
python scripts/check_repo.py
python scripts/parallel_workflow.py --lane agent_b status
python scripts/parallel_workflow.py --lane agent_b next
python scripts/parallel_workflow.py --lane agent_b packet PAGE21_TEXT
```

Mỗi bước dùng start/checkpoint/finish qua CLI này; thay TASK_ID và đường dẫn evidence bằng file thật:

```bash
python scripts/parallel_workflow.py --lane agent_b start TASK_ID --owner agent_b --note "Nguồn và đầu ra cần làm"
python scripts/parallel_workflow.py --lane agent_b checkpoint TASK_ID --note "Đã có file nào; lỗi còn lại; bước tiếp"
python scripts/parallel_workflow.py --lane agent_b finish TASK_ID --evidence PATH_TO_REPORT --note "Đã kiểm thật"
python scripts/parallel_workflow.py --lane agent_b check
python scripts/parallel_workflow.py --lane agent_b guard
python scripts/parallel_workflow.py --lane agent_b stage
python scripts/parallel_workflow.py --lane agent_b publish --message "agent_b: checkpoint trang được giao"
```

Đầu ra cuối của bạn: toàn bộ trang21–28 đã qua4bước, đủ raw/speech art/meta/prompt/source SVG/PDF/preview/QA và HANDOFF.md, đã push main/đối chiếu SHA. Tiếp tục việc đang dở của chính lane nếu đổi phiên; không tạo lại phần done hợp lệ.
