# Bắt đầu ở đây — một repo, một nhánh main

Đây là lối vào hiện hành cho mọi agent. Người dùng yêu cầu ngày 09/11/2026 gộp toàn bộ công việc vào **main**, tiếp quản bằng file và làm từ A–Z. Một agent có thể lần lượt đảm nhiệm sáu vai trò; không bắt buộc khởi tạo sáu agent.

## Clone rồi chạy

```bash
git clone https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent.git
cd trung-nu-vuong-19x24-multi-agent
git switch main
git pull --ff-only origin main
python -m venv .venv
```

Kích hoạt môi trường: macOS/Linux `source .venv/bin/activate`; PowerShell `.venv\Scripts\Activate.ps1`; Windows CMD `.venv\Scripts\activate.bat`. Có thể dùng `python3` hoặc `py` thay `python` tùy máy.

```bash
python -m pip install -r requirements.txt
python scripts/workflow.py doctor
python scripts/check_repo.py
python scripts/workflow.py status
python scripts/workflow.py next
python scripts/workflow.py packet
```

`packet` tạo brief, danh sách ảnh tham chiếu thật và mẫu báo cáo cho việc tiếp theo. Đọc brief, mở ảnh, rồi làm việc. Không cần đoán tác vụ từ lịch sử hội thoại.

## Đọc theo thứ tự, sau đó làm

1. [AGENTS.md](AGENTS.md): quy tắc bắt buộc, main và cách giữ tiến độ.
2. [Quy trình A–Z](10_agent_workflow/WORKFLOW_A_TO_Z.md): đầu vào/đầu ra và điều kiện xong từng bước.
3. [Sự thật hiện có và phần còn thiếu](10_agent_workflow/PROJECT_STATUS.md).
4. [Quyết định nguồn](09_design_system/SOURCE_DECISIONS.md) → [album 30 bảng](09_design_system/IMAGE_CATALOG.md) → [nguyên tắc mỹ thuật](09_design_system/MASTER_ART_DIRECTION.md).
5. [Nhật ký](08_project_memory/WORK_LOG.md) và `production_state.json` để tiếp tục; đọc đúng storyboard/hồ sơ/scan cho trang đang làm, không cần đọc lại mọi ảnh mỗi phiên.

Nguồn sự kiện là scan/bằng chứng đã đối chiếu; chữ từng cảnh ở Ngăn 03; thiết kế ở Ngăn 09; tiến độ tác vụ ở `10_agent_workflow/production_state.json`. Brief được sinh lại không phải nguồn chữ mới.

## Vòng làm việc ngắn, có thể tiếp tục

```bash
python scripts/workflow.py start PAGE01_TEXT --owner "ten-agent" --note "Đọc nguồn và khóa chữ trang01"
python scripts/workflow.py checkpoint PAGE01_TEXT --note "Đã đối chiếu PDF06–07; còn chép thoại/kiểm chữ"
```

Có kết quả thì lưu vào repo, ghi nhật ký, commit/push ngay; không đợi tạo xong cả 28 trang. Sau ngắt phiên, clone/pull và chạy `next`: việc đang làm cùng ghi chú sẽ được ưu tiên. Xem [cách phục hồi](10_agent_workflow/RECOVERY_AND_MAIN.md).

Để kết thúc tác vụ, điền bản copy `report.v001.json` từ mẫu do packet tạo, thêm artifacts thật, ghi từng check đã kiểm. Sau đó:

```bash
python scripts/workflow.py finish PAGE01_TEXT --evidence 10_agent_workflow/tasks/PAGE01_TEXT/report.v001.json --note "Đã khóa chữ và đối chiếu nguồn"
python scripts/check_repo.py
git add <cac-file-da-kiem-tra>
git commit -m "text: lock page01 with source review"
git pull --rebase origin main
git push origin main
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Đối chiếu hai SHA cuối; nếu push chưa thành công phải ghi rõ, không báo đã đồng bộ. Thay `<cac-file-da-kiem-tra>` bằng đường dẫn thật; không gõ nguyên dấu ngoặc.

## Chỉ đưa repo là đủ để bắt đầu, công cụ vẫn phải có

- Repo public: clone/read không cần PAT. Push cần quyền ghi do môi trường/credential manager cấp, không nhúng PAT vào URL/file.
- Cần Python 3.10+, Git và Pillow để kiểm ảnh. **Repo không chứa mô hình tạo ảnh, API key hoặc công cụ in thương mại.** Agent có công cụ tạo ảnh thì dùng nó; thiếu công cụ thì block riêng bước ART, tiếp tục bước độc lập, báo đúng giới hạn.
- Có thể tự làm bản nháp bằng baseline. Không tự ghi chủ dự án đã duyệt; không tự chốt ICC/gáy/ISBN khi chưa có dữ liệu.
- Lệnh trong repo không tự gọi AI và không tự push; agent đọc quy trình rồi thực thi các công cụ sẵn có.

[Câu giao việc copy sẵn](10_agent_workflow/AGENT_PROMPT.md) · [Lệnh điều khiển](10_agent_workflow/COMMANDS.md) · [Bản đồ file](10_agent_workflow/REPO_MAP.md)
