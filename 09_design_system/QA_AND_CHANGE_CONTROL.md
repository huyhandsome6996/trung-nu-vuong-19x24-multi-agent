---
project: "TRƯNG NỮ VƯƠNG"
book_size: "190x240mm; bleed 196x246mm @300 DPI for final pages"
target_audience: "Lớp 8–10 (13–16 tuổi)"
agent_author: "ChatGPT / design system production"
status: "DESIGN_BASELINE"
user_approved: false
date: "2026-11-09"
---

# Kiểm chất lượng và kiểm soát thay đổi

## Ba mức trạng thái

- PLANNED: có thiết kế/prompt nhưng chưa có ảnh.
- DESIGN_BASELINE / GENERATED: đã chọn phương án để agent sản xuất bản nháp nhất quán. Người dùng chưa mặc nhiên duyệt từng ảnh.
- APPROVED: chỉ ghi sau khi có lời duyệt rõ ràng và phạm vi duyệt. Print-ready là kiểm khác, không tự đi cùng APPROVED concept.

## Kiểm một bảng nhân vật

- Đúng số và thứ tự người; mỗi người có mã riêng.
- Cùng người trong nhiều tư thế giữ mắt–mũi–hàm/tóc/tuổi biểu kiến.
- Phân biệt Trưng Trắc, Trưng Nhị, Thánh Thiên bằng cả mặt và màu; không chỉ đổi áo.
- Đúng giới tính/trang phục theo SOURCE_DECISIONS; không quên khăn tang.
- Không cắt chân/mũi vũ khí; tay cầm và cơ chế cung/nỏ hợp lý.
- Không chữ rác, watermark, biểu tượng hiện đại hoặc màu giáp lệch phe.
- Nét hatching rõ ở100%, mặt không nát khi thu về kích thước dùng; ảnh concept không đủ cho cận cảnh phải sinh cận cảnh riêng.

## Kiểm bối cảnh và đạo cụ

Địa hình/lối đi ổn định giữa các góc; lư khác đỉnh, hổ phù cầm tay khác huy hiệu ngực, cung khác nỏ. Concept board nhiều ô chỉ ghi nhóm vật mẫu; các mã nhỏ cùng nhóm vẫn cần tuân thủ mô tả từng mã. Các số lượng lớn như99 cờ không kiểm được chỉ bằng prompt; cần kiểm hoặc ghép có chủ đích.

## Tự động hóa

Validator kiểm ID duy nhất, mã tham chiếu tồn tại, 41 hồ sơ hiện hữu, ảnh giải mã được và hash đúng metadata, job không còn PLANNED khi bàn giao bộ hình, đường dẫn nội bộ. Không giả tạo OCR, đo điểm tương đồng khuôn mặt, kiểm khảo cổ hoặc xác nhận màu in khi chưa chạy.

## Khi thay một thành phần

Ví dụ đổi mũ Trưng Trắc: tạo CHAR01_v002, cập nhật TURN01 và các trang10–14/17–18/27–28/bìa có ảnh hưởng; kiểm lại mặt sau và áo choàng. Không âm thầm thay file v001. Sửa metadata nguồn và log quyết định, commit mô tả tác động.
