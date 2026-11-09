---
project: "TRƯNG NỮ VƯƠNG"
book_size: "190x240mm; bleed 196x246mm @300 DPI for final pages"
target_audience: "Lớp 8–10 (13–16 tuổi)"
agent_author: "ChatGPT / design system production"
status: "DESIGN_BASELINE"
user_approved: false
date: "2026-11-09"
---

# Bộ thiết kế tổng thể TRƯNG NỮ VƯƠNG

> Quy trình hiện hành: [START_HERE](../START_HERE.md). Toàn bộ thiết kế đã hợp nhất vào main; Ngăn09 chuyên về thiết kế, Ngăn10 quản lý tác vụ sản xuất.

Dành cho chủ dự án muốn xem ngay hình và agent cần tiếp tục công việc. Đây là **bộ thiết kế v1 dùng thống nhất cho sản xuất bản nháp** theo ủy nhiệm ngày 09/11/2026, không tự ghi chủ dự án đã duyệt từng ảnh.

## Xem nhanh

1. Mở [IMAGE_CATALOG.md](IMAGE_CATALOG.md) để xem toàn bộ bảng hình, tên người và vị trí trên ảnh.
2. Muốn hiểu truyện trong hai phút: [STORY_IN_2_MINUTES.md](STORY_IN_2_MINUTES.md).
3. Tra người: [41 hồ sơ nhân vật](CHARACTER_INDEX.md). Tra cảnh: [14 bối cảnh](ENVIRONMENTS.md). Tra đồ vật: [36 nhóm đạo cụ và 4 động vật](PROPS_AND_ANIMALS.md).
4. Muốn giao agent làm trang: dùng [AGENT_HANDOFF.md](AGENT_HANDOFF.md) và [PAGE_ASSET_MATRIX.md](PAGE_ASSET_MATRIX.md).
5. Muốn gửi ngay cho AI khác: copy [AGENT_START_PROMPT.md](AGENT_START_PROMPT.md); có sẵn lệnh clone main và quy trình tiếp quảnA–Z.

## Bộ này gồm những gì

- 17 bảng casting: 10 bảng gốc + 7 bảng bổ sung, bao phủ 41 hồ sơ. Một số bảng có nhiều người, tên và vị trí được ghi ngoài ảnh để không làm lỗi chữ.
- 1 bảng góc quay/biểu cảm Trưng Trắc; các nhân vật chính khác có mặt cận cảnh và tư thế trên sheet. Không nói mọi người đã có turnaround đủ 360°.
- 5 bảng bối cảnh, 4 bảng đạo cụ/phương tiện, 1 bảng quân đội/quần chúng, 1 bảng động vật, 1 bảng24 mặt tộc trưởng tập thể.
- Thành phần dàn trang dạng SVG và thông số có thể tái sử dụng: A/B/C, khung giấy cổ, bóng thoại, số trang, bìa và màu.
- Registry JSON, prompt nguyên văn, metadata kích thước/hash và bảng QA để agent sau tìm đúng ảnh, không vẽ lại từ trí nhớ.

Tiến độ ảnh thực tế và giới hạn được ghi trong IMAGE_CATALOG.md / QA_DESIGN_REPORT.md. File thiết kế luôn khác ảnh in thành phẩm: không dùng các bảng nhiều người hoặc nhiều cảnh này làm thẳng một trang truyện.

## Nguyên tắc không tự thay đổi

Trưng Trắc đỏ-đồng / trắng tang; Trưng Nhị lam sẫm; Thi Sách tía và hổ phù ngực; Thánh Thiên lục và khăn tang. Mặt và đạo cụ không đổi theo từng trang. Mỗi trang có hành động rõ và biểu cảm, không chỉ xếp người đứng. Mọi chữ tiếng Việt được chế bản riêng. Chưa sinh 28 trang truyện trong nhiệm vụ làm bộ thiết kế này.

## Bàn giao đã đóng bộ

Bộ30 bảng hình đã hoàn thành; xem [báo cáo QA](QA_DESIGN_REPORT.md), [24 mã mặt tập thể](CROWD_FACE_KEYS.md) và [thành phần dàn trang](layout_components/README.md). Mở `XEM_THIET_KE.html` từ bản clone repo để lọc theo nhóm/tên; trên GitHub xem IMAGE_CATALOG.md.
