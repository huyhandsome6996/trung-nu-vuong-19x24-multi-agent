# Công cụ và đầu ra

| Năng lực | Repo cung cấp | Agent thực hiện |
| --- | --- | --- |
| Đọc/soạn Markdown, JSON, Git | Hồ sơ và script | Làm ngay trong phạm vi đã giao |
| Giải mã ảnh, hash | Pillow trong requirements | Cài dependency và chạy kiểm tra |
| Tạo/sửa ảnh AI | Tham chiếu và prompt; không có model/key | Dùng công cụ ảnh của agent, truyền ảnh thật; thiếu công cụ thì block ART |
| Khóa chữ, brief, queue | workflow.py | Đối chiếu nguồn và khóa chữ bằng bằng chứng thật |
| Ghép HTML proof | typeset_preview.py | Cần text locked, raw thật và file font Việt |
| Render HTML/PDF/PNG | Không bundle browser/InDesign | Dùng renderer có sẵn; ghi công cụ/phiên bản, mở bản render kiểm chữ và hình |
| PDF in, ICC, gáy | Đặc tả chưa chốt nhà in | Dùng công cụ chế bản đủ năng lực, kiểm box/font/resolution/profile |
| Push GitHub | Git, cần quyền ghi | Xác thực qua môi trường, đối chiếu SHA remote |

## Đường dẫn thống nhất

- Brief/báo cáo: `10_agent_workflow/tasks/PAGE01_TEXT/`; chữ `text.v001.json`, báo cáo `report.v001.json`.
- Tranh nền: `assets_generated/raw_pages/PAGE01_v001.png` và JSON; bìa FRONT/BACK theo cùng quy ước.
- Nguồn sửa được: `final_book_19x24/source/`; bản kiểm: `final_book_19x24/proofs/`.
- Pagination, print_profile, delivery_manifest đặt tại `final_book_19x24/` khi đã có dữ liệu thật.
- File in: `final_book_19x24/print/`; bản đọc: `final_book_19x24/reading/`.
- Nhật ký và kinh nghiệm: Ngăn 08. Không đưa hàng loạt file debug/scratch vào repo.

File trên 100 MB không push Git thường. Chọn gói nguồn nhẹ hoặc LFS/release theo quyền sẵn có, ghi link và hash bền vững; không tự gửi tới dịch vụ bên ngoài. Repo đang bỏ qua PSD/AI/INDD: nếu cần lưu các nguồn đó, chọn cách lưu phù hợp và bàn giao đủ nguồn sửa được, không chỉ ảnh xuất.

## CI trên GitHub

Workflow thực thi ở [.github/workflows/validate-main.yml](../.github/workflows/validate-main.yml), chạy tests và check_repo sau mỗi push main hoặc khi chạy thủ công. Chỉ có quyền đọc nội dung repo; không gọi AI, không tự push hay xuất bản.

Xem [kết quả chạy thực](https://github.com/huyhandsome6996/trung-nu-vuong-19x24-multi-agent/actions/workflows/validate-main.yml). CI xanh chỉ xác nhận bộ kiểm kỹ thuật; QA nguồn, hình ảnh và in vẫn phải thực hiện. [Mẫu YAML](templates/github-actions-validate.yml) được giữ để tham khảo.
