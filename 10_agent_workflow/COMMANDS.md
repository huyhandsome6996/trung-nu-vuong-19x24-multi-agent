# Các lệnh hằng ngày

Chạy từ gốc repo, Python 3.10+. Các lệnh không tự gọi AI và không tự push.

| Lệnh | Tác dụng |
| --- | --- |
| `python scripts/workflow.py doctor` | Kiểm Python, Pillow, nhánh và các công cụ cần có |
| `python scripts/workflow.py status` | Xem done/todo/blocked và việc đang làm |
| `python scripts/workflow.py next` | Ưu tiên việc đang dở, sau đó chọn việc đủ phụ thuộc |
| `python scripts/workflow.py packet PAGE01_TEXT` | Tạo brief, bản nháp chữ, ảnh ứng viên và mẫu báo cáo |
| `python scripts/workflow.py start PAGE01_TEXT --owner agent --note "Bắt đầu đối chiếu nguồn"` | Nhận việc; từ chối nếu đã có task active |
| `python scripts/workflow.py checkpoint PAGE01_TEXT --note "Đã có…; còn…; file…"` | Lưu điểm tiếp tục vào state/history, chưa nâng done |
| `python scripts/workflow.py block PAGE01_ART --note "Thiếu công cụ ảnh"` | Ghi lý do, cho phép tiếp tục việc độc lập |
| `python scripts/workflow.py unblock PAGE01_ART --note "Đã có công cụ ảnh"` | Đưa về todo; khi start vẫn phải đủ phụ thuộc |
| `python scripts/workflow.py finish PAGE01_TEXT --evidence 10_agent_workflow/tasks/PAGE01_TEXT/report.v001.json --note "Đã khóa chữ"` | Kiểm báo cáo, file và hash trước khi done |
| `python scripts/workflow.py reopen PAGE01_TEXT --note "Sửa lời dẫn theo nguồn"` | Mở lại task và chuỗi phụ thuộc, giữ bằng chứng cũ |
| `python scripts/workflow.py check` | Kiểm DAG, nguồn, storyboard, evidence và tiến độ |
| `python scripts/check_repo.py` | Kiểm workflow, ảnh thiết kế, link Markdown, mẫu token và git diff |
| `python scripts/workflow.py check --release` | Yêu cầu mọi task done; phải fail khi sách chưa xong |
| `python -m unittest discover -s tests -v` | Kiểm logic tiếp tục, phụ thuộc, evidence và helper |

## Báo cáo chuẩn

Packet tạo `report.template.json` với trạng thái draft/not_checked. Copy thành report.v001.json, điền reviewer, summary, reviewed_at, artifacts và checks. Đường dẫn artifacts tính từ gốc repo; open_issues phải rỗng trước finish. Chỉ đánh pass sau khi thực sự kiểm.

Task TEXT cần JSON chữ đã khóa: đúng page/template, narration 35–65 tiếng và cặp **từ khóa**, hash storyboard hiện hành, status và dialogues_status đều locked. Chép đủ thoại từ storyboard; nếu trang không có thoại, dùng dialogues rỗng và xác nhận đã đối chiếu. Draft do packet tạo chưa chép thoại, không được dùng thẳng để chế bản.

Task ART cần ảnh thật và JSON theo [mẫu metadata](templates/RAW_IMAGE_METADATA.json). Kích thước, hash và actual_references được kiểm bằng máy. Nhận diện khuôn mặt, chất lượng tranh và không có chữ vẫn cần agent mở ảnh kiểm thật.

Các task khác cần báo cáo và đầu ra theo instructions. CLI không thể xác minh mọi lời khẳng định của reviewer; không dùng file rỗng hoặc báo cáo giả để qua kiểm tra.

## Ghép thử một trang

```bash
python scripts/typeset_preview.py --text 10_agent_workflow/tasks/PAGE01_TEXT/text.v001.json --raw assets_generated/raw_pages/PAGE01_v001.png --font path/to/licensed-vietnamese-font.ttf --out final_book_19x24/proofs/PAGE01_v001.html
```

Thay đường dẫn bằng file thật. Helper từ chối chữ chưa locked, ảnh sai tỷ lệ cần crop/outpaint và thoại chưa có bbox_mm/tail_mm. Tọa độ mm tính từ mép trim; helper cộng 3 mm bleed.

Mở HTML bằng renderer thật, chờ font nạp, kiểm tràn chữ, 3–5 dòng lời dẫn, glyph Việt và vị trí hình. HTML này là bản kiểm, không phải PDF/X hoặc file in đã duyệt. Cần điều chỉnh bố cục và nội dung hợp lý; không thu nhỏ font tùy tiện để hết tràn.

[Mẫu CI GitHub](templates/github-actions-validate.yml) hiện chưa bật do token thiếu quyền workflow. Có thể dùng đầy đủ bộ kiểm local mà không bật Actions.
