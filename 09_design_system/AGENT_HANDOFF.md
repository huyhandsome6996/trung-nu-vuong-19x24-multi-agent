---
project: "TRƯNG NỮ VƯƠNG"
book_size: "190x240mm; bleed 196x246mm @300 DPI for final pages"
target_audience: "Lớp 8–10 (13–16 tuổi)"
agent_author: "ChatGPT / design system production"
status: "DESIGN_BASELINE"
user_approved: false
date: "2026-11-09"
---

# Hướng dẫn cho agent tiếp nhận

> Bắt đầu phiên ở [START_HERE](../START_HERE.md) và workflowNgăn10. Mọi công việc ởmain; tài liệu này mô tả riêng cách dùng thiết kế.

## Đọc đúng phần, lấy đúng ảnh

1. Đọc `00_READ_FIRST.md`, `SOURCE_DECISIONS.md`, `MASTER_ART_DIRECTION.md`.
2. Tìm trang trong `PAGE_ASSET_MATRIX.md`; lấy mã NV/E/P/A.
3. Mở các hồ sơ NV và xem **pixel ảnh** trong `IMAGE_CATALOG.md`, không chỉ đọc prompt.
4. Kiểm `design_registry.json`, `image_jobs.json` và JSON cạnh PNG để chọn phiên bản. GENERATED/DESIGN_BASELINE khác với APPROVED.
5. Đọc nguyên trang storyboard để giữ hành động, lời dẫn **...** và thoại; áp dụng bản đính chính nguồn trước prompt cũ.

## Quy trình vẽ một trang

- Soạn brief JSON như mẫu dưới; nêu rõ ai làm gì, ai nói, giai đoạn trang phục, nơi diễn ra và giờ/ánh sáng.
- Dùng 1 ảnh style, ảnh nhân vật xuất hiện và bối cảnh liên quan. Nếu công cụ giới hạn số ảnh, chia theo khung hoặc làm reference pack; ghi đúng tệp đã truyền. Không dùng 17 bảng cùng lúc.
- Với bảng nhóm: prompt chỉ rõ tên/mã, vị trí trái–phải trong sheet; tránh sinh cả bốn người khi chỉ muốn một.
- Sinh nền sạch chữ, chừa y0..48mm (khoảng20% đỉnh) cả mũ/kiếm/đầu. 4:5 ưu tiên; không kéo méo để đủ 19×24.
- Kiểm mặt, giáp, tay/chân, vũ khí, hướng di chuyển và cửa/sân. Nếu sai, sửa mục tiêu cụ thể; không đổi cả phong cách mỗi lần.
- Sau khi ảnh đạt chất lượng, ghép khung giấy cổ, chữ và bóng thoại riêng. Mọi cặp **...** trong lời dẫn tô #C81E1E, không tự bớt dấu sao cho vừa khung.
- Chỉ gọi print-ready sau kiểm hộp PDF, font, kích thước và ảnh có đủ chi tiết; không gắn DPI rồi coi là đã tăng chất lượng.

```json
{
  "page": 23,
  "template": "A",
  "characters": [{"id":"NV04","costume":"đoản giáp lục, khăn tang","action":"chỉ kiếm nhử địch"},{"id":"NV17","costume":"giáp sắt, choàng tím","action":"đối diện dưới sân"}],
  "environment":"E10",
  "props":["P09","P10","P23"],
  "lighting":"sáng, hướng trái-trên",
  "references": ["CHAR04_v001.png","CHAR10_v001.png","ENV04_v001.png"],
  "text_free":true,
  "top_clearance_mm":48,
  "source":"STORYBOARD_PART_2, trang23 + SOURCE_DECISIONS"
}
```

## Bàn giao sau mỗi phần việc

Ghi đầu ra, prompt nguyên văn, tệp tham chiếu thực dùng, số lần sinh, lỗi đã sửa, lỗi còn lại, kích thước/hash, trạng thái kiểm và bước tiếp. Commit theo nhóm có ý nghĩa rồi push; không để ảnh chỉ ở thư mục tạm. Không lưu token vào repo. Không tự ghi người dùng đã duyệt nếu họ chỉ yêu cầu tiếp tục.

## Lệnh kiểm

Chạy `python 09_design_system/validate_design_system.py` từ gốc repo. Báo cáo kiểm ID/file/hash/đường dẫn chỉ là kỹ thuật, không thay thế kiểm thị giác. Muốn đổi chuẩn: tạo v002, cập nhật registry/catalog/page matrix, liệt kê trang chịu ảnh hưởng, giữ bản cũ so sánh.
