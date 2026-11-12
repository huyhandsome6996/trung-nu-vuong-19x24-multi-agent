# Hợp đồng đầu ra và schema để agent không phải đoán

Mỗi agent chỉ ghi trong lane của mình. `XX` là số trang PDF hai chữ số, tính bìa là 01. Giữ nguyên nguồn bất biến.

| Đường dẫn trong lane | Nội dung |
|---|---|
| `text/PDF_XX.json` | Toàn bộ chữ cuối cùng của trang, các câu thoại và người nói, ghi chú thay đổi |
| `text/changes.md` | Quyết định tên/chính tả, đối chiếu cốt truyện, lời thoại chuyển thể |
| `source/PDF_XX.*` | Nguồn chỉnh sửa/dàn trang, ảnh đã sửa và layer/mask/script cần để tái tạo; có thể dùng thư mục `PDF_XX/` |
| `output/PDF_XX.png` | Ảnh trang sửa, ít nhất 896×1200 px, cùng tỉ lệ nguồn |
| `output/PDF_XX.pdf` | PDF một trang, MediaBox 430,08×576 pt |
| `qa/PDF_XX.json` | Kết quả từng yêu cầu của trang và kiểm bằng mắt |
| `output/LO_TRANG.pdf` | Chỉ các trang lane sở hữu, theo thứ tự tăng dần |
| `HANDOFF.md` | Trang đã làm, file thật, điều đã sửa, kiểm đã chạy, hạn chế và yêu cầu kiểm liên trang |

Ví dụ schema chữ; thay bằng nội dung thật, không dùng câu mẫu làm sản phẩm:

```json
{
  "pdf_page": 14,
  "narration": "Toàn bộ lời dẫn cuối cùng của trang...",
  "footnote": null,
  "dialogue": [
    {"speaker": "Trưng Trắc", "panel": 2, "order": 1, "text": "Lời khấn đã biên tập..."}
  ],
  "changes": ["Thu gọn ô vàng", "Thêm lời khấn chuyển thể theo góp ý"]
}
```

Copy `qa/TEMPLATE.json` thành `qa/PDF_XX.json`. Mỗi yêu cầu trong `03_nhiem_vu_tung_trang/PDF_XX.json` cần một phần tử tương ứng, cùng thứ tự, trong `teacher_requirement_results`:

```json
{
  "requirement_index": 1,
  "status": "PASS",
  "note": "Mô tả cụ thể vùng đã sửa và bằng chứng đã xem"
}
```

Đường dẫn ở `visual_review.evidence` tính từ thư mục lane, ví dụ `output/PDF_14.png` và `qa/PDF_14_render.png`. Thật sự render PDF ra ảnh `qa/PDF_XX_render.png`, mở cả ảnh đầu ra và ảnh render, kiểm đủ chữ/tranh rồi mới đặt `reviewed: true`. `reviewer` ghi định danh agent đang kiểm. Tất cả khóa trong `checks` phải PASS trước khi trang đạt PASS. Không đặt PASS bằng việc chỉ đọc metadata.

`cross_lane_identity` có thể PENDING nếu chưa có reference lane khác; ghi rõ trong HANDOFF và STATUS. Đây là việc coordinator phải kiểm cuối, không che giấu giới hạn đó. Các tiêu chí ngay trong trang vẫn phải PASS. Khi reference đã có, agent 5 đối chiếu Thánh Thiên ở lane 4 và sửa nếu lệch.

Khi đủ toàn bộ trang, đặt `STATUS.json.status` thành `READY_FOR_COORDINATOR`, `completed_pages` đủ trang mình, `blocked_pages` rỗng và `artifacts` chứa đường dẫn thật. Agent 4 còn xuất `source/THANH_THIEN_REFERENCE.png`. Đang làm dở dùng `IN_PROGRESS`; thiếu công cụ tranh dùng `BLOCKED_ART` cùng số trang và nguyên nhân. Không báo READY nếu chỉ có chữ/prompt.

Kiểm riêng bằng `validate_lane.py agent_N --ready`; sau stage kiểm thêm `--staged`. Công cụ kiểm kỹ thuật và sự hiện diện evidence, không thể tự chứng minh chất lượng mỹ thuật hoặc việc người kiểm đã nhìn đúng.
