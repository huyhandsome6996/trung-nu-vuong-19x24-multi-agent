# TRƯNG NỮ VƯƠNG — truyện minh họa 19×24 cm

**Một repo, một nhánh `main`, một lối vào cho agent.** Dành cho học sinh lớp 8–10; chuyển thể Hồi 7–8 từ tư liệu dự án, phong cách mực đen đan nét kết hợp màu nước/chì màu cổ điển hào hùng.

## Bắt đầu ngay

- **Agent nhận việc:** mở [START_HERE.md](START_HERE.md), làm theo lệnh clone → kiểm tra → nhận việc → sản xuất → QA → push main.
- **Chủ dự án xem hình:** mở [album 30 bảng thiết kế](09_design_system/IMAGE_CATALOG.md).
- **Giao cho AI khác:** copy [một câu lệnh đầy đủ](10_agent_workflow/AGENT_PROMPT.md).
- **Xem hiện trạng:** [PROJECT_STATUS.md](10_agent_workflow/PROJECT_STATUS.md), [bảng tiến độ máy đọc](10_agent_workflow/production_state.json).

```bash
git clone https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent.git
cd trung-nu-vuong-19x24-multi-agent
python -m pip install -r requirements.txt
python scripts/check_repo.py
python scripts/workflow.py next
python scripts/workflow.py packet
```

Python 3.10+ và Git. Xem START_HERE để tạo môi trường và dùng trên Windows. Không cần chọn nhánh thiết kế nữa.

## Đã có / việc tiếp theo

Đã có 59 file nền được kiểm kê, 30 bảng hình tham chiếu, 41 hồ sơ nhân vật, 24 mặt tộc trưởng, 14 bối cảnh, 36 nhóm đạo cụ, 4 động vật và thành phần dàn trang SVG. **Chưa có 28 trang truyện thành phẩm hoặc file in đã duyệt.** Việc tiếp theo là kiểm nguồn và khóa chữ từng trang rồi dùng thiết kế hiện hành để vẽ. Một số lời dẫn thực tế vượt 65 tiếng; trang 27–28 cần nguồn phần kết ngoài đoạn trích.

## Bản đồ ngăn

| Ngăn | Dùng để làm gì |
| --- | --- |
| [01](01_source_material_analysis/README.md) | Phân tích 58 trang scan và mẫu bố cục |
| [02](02_historical_fairy_tale_adaptation/README.md) | Giọng văn 13–16 tuổi và hồ sơ chuyển thể |
| [03](03_storyboards_and_scripts/README.md) | Kịch bản 28 trang, chữ/thoại/template |
| [04](04_art_direction_and_image_prompts/README.md) | Mỹ thuật và thư viện prompt |
| [05](05_book_design_and_layout_19x24/README.md) | Dàn trang 19×24 và đặc tả chế bản |
| [06](06_qa_validation_and_delivery/README.md) | QA, kiểm kê và báo cáo |
| [07](07_reference_assets/README.md) | 22 ảnh mẫu  +10 contact sheets nguồn, giữ nguyên |
| [08](08_project_memory/README.md) | Nhật ký, quyết định, kinh nghiệm |
| [09](09_design_system/00_READ_FIRST.md) | Thiết kế/ảnh tham chiếu/registry hiện hành |
| [10](10_agent_workflow/WORKFLOW_A_TO_Z.md) | Queue, workflow, phục hồi, checklist và mẫu báo cáo |
| [assets_generated](assets_generated/README.md) | Ảnh tham chiếu và tranh nền có phiên bản |
| [final_book_19x24](final_book_19x24/README.md) | Nguồn chế bản, bản xem, bản in và manifest khi tạo |

32 trang ruột = 28 truyện +4 trang phụ; thêm 4 mặt bìa. Trim 190×240 mm; bleed 196×246 mm; mục tiêu 300 DPI. Chữ tiếng Việt ghép riêng, **từ khóa** đỏ #C81E1E. [Quy chuẩn hợp nhất](05_book_design_and_layout_19x24/STANDARD_OUTPUT_CONTRACT.md), [quyết định nguồn](09_design_system/SOURCE_DECISIONS.md).

`main` chứa cả bản nháp có nhãn trạng thái lẫn sản phẩm đã kiểm. Vào main không có nghĩa là đã được chủ dự án duyệt hoặc sẵn in. Các hướng dẫn chia nhánh cũ đã được thay bằng [quy trình main](06_qa_validation_and_delivery/GITHUB_COLLABORATION_PROTOCOL.md).
