# Phạm vi đợt sửa giáo viên

Chỉ làm trên nhánh `sua-theo-gop-y-giao-vien`. Đây là chỉ thị mới ngày12/11/2026, thay phân công2 agent/main-only cũ trong phạm vi đợt sửa. Nguồn hình là PDF Gemini21 trang, không phải thiết kế cũ. Đọc README.md của ngăn này, quy chuẩn và BRIEF trong lane trước khi làm.

Mỗi agent chỉ ghi `04_agents/agent_N/`. File nguồn/chung/prompt/công cụ do coordinator giữ. Được đọc mọi lane để đối chiếu, không ghi lane khác. Không tự thêm nhánh, không push main, không force-push. Không gọi workflow.py/parallel_workflow.py cũ để sửa state đợt này.

Mở ảnh gốc và ảnh khoanh thật; chỉnh đủ trang được giao thành PNG/PDF và nguồn chỉnh sửa, kiểm bằng mắt, ghi evidence. Thiếu công cụ tạo/chỉnh tranh: đánh BLOCKED_ART đúng trang, làm trước chữ/brief/mask/QA độc lập; không báo đã sửa ảnh chỉ vì có prompt. Trước commit chạy `python3 11_sua_theo_gop_y_giao_vien/06_cong_cu/check_packet.py`, và `python3 11_sua_theo_gop_y_giao_vien/06_cong_cu/validate_lane.py agent_N --staged` sau stage. Trước READY chạy validate_lane.py agent_N --ready. Không nhận xét toàn sách đã đạt nếu mới xem lane mình.

Lưu checkpoint sau từng trang, fetch/rebase nhánh này trước push, kiểm SHA commit của mình còn trong nhánh remote. Mọi thay đổi chung cần ghi ở requests.md trong lane; coordinator quyết định. Không ghi credential vào bất cứ file/URL/log nào.
