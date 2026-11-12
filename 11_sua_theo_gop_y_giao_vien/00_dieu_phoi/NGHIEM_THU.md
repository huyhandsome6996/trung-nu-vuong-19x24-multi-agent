# Nghiệm thu và ghép sau cùng

1. Fetch đúng nhánh; đọc HANDOFF, STATUS, QA của 5 lane, không chỉ tin dòng READY.
2. Chạy check_packet.py và validate_lane.py agent_N --ready cho cả 5 lane. Chỉ kiểm kỹ thuật/evidence, không thay kiểm bằng mắt.
3. Mở cạnh nhau16–21 để kiểm Thánh Thiên khác Trưng Trắc và nhất quán giữa lane 4/5. Rà cờ01–21, trang phục theo phe, ô vàng, câu thoại đúng người, chữ Hoàng/thủ và chú giải.
4. Yêu cầu lane phụ trách sửa phần còn lệch; không sửa file của agent đang chạy mà không phối hợp.
5. Chạy `python3 11_sua_theo_gop_y_giao_vien/06_cong_cu/assemble.py`; mặc định xuất 07_tong_hop/BAN_SUA_GIAO_VIEN.pdf,manifest và contact sheet. Nó sẽ từ chối nếu thiếu bất cứ trang/QA nào.
6. Render và kiểm đủ 21 trang sau ghép. Ghi FINAL_REVIEW.md với kết quả từng yêu cầu và hạn chế nguồn. Trạng thái này là sẵn sàng gửi giáo viên, không tự đặt TEACHER_APPROVED.
7. Commit/push nhánh sửa, kiểm commit nằm trên remote. Chỉ merge main nếu người dùng yêu cầu riêng.
