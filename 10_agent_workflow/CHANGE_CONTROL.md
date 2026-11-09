# Thay đổi nội dung đã khóa

- Không sửa ảnh hoặc báo cáo v001 đã finish. Tạo v002 cùng metadata; giữ bản cũ để so sánh.
- Đổi chữ trang 01: `python scripts/workflow.py reopen PAGE01_TEXT --note "Lý do và phạm vi"`. Chỉ đổi ảnh thì reopen PAGE01_ART. CLI đưa task và toàn bộ chuỗi phụ thuộc về todo, kể cả ASSEMBLY/RELEASE; evidence cũ chuyển vào previous_evidence, file cũ được giữ.
- Nếu sửa một file storyboard, các text khóa theo hash cả file cần rà lại. Reopen các TEXT chịu ảnh hưởng, kiểm và khóa với hash mới; không sửa hash báo cáo mà không kiểm nội dung.
- Đổi thiết kế nhân vật cần ảnh v002, cập nhật registry/job/catalog và thống kê các trang bị ảnh hưởng. Reopen các ART liên quan. CLI không reopen hai task baseline; quyết định đổi chuẩn phải ghi vào SOURCE_DECISIONS/DECISION_LOG cùng metadata phiên bản.
- Ngăn 07 giữ nguyên. Tư liệu bổ sung phải là file mới có xuất xứ, quyền sử dụng và hash riêng. `source_hashes.json` kiểm 32 JPG gốc; không ghi sửa ảnh scan để đổi bằng chứng.
- Đổi code/quy trình: chạy tests và check_repo, cập nhật hướng dẫn ở main cùng nhật ký. Báo cáo ngày cũ là lịch sử; thêm chú thích thay thế nếu cần.
