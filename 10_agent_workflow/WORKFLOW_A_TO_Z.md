# Workflow sản xuất từ A–Z

Hiệu lực 09/11/2026. Main chứa toàn bộ công việc có trạng thái rõ. Một agent có thể lần lượt đảm nhiệm sáu vai trò: tư liệu, chuyển thể, kịch bản, mỹ thuật, chế bản và QA.

## Các bước và điều kiện chuyển tiếp

| Bước | Đầu vào | Thực hiện | Đầu ra cần có |
| --- | --- | --- | --- |
| A. Tiếp quản | START_HERE, AGENTS, WORK_LOG, state | Pull main, doctor/check, ưu tiên việc đang dở | Biết tình trạng thật, không làm lại phần đã có |
| B. Khóa chữ | Ngăn 01/02/03, scan 07, SOURCE_DECISIONS | Kiểm nguồn; lời dẫn 35–65 tiếng; chép đủ thoại, từ khóa, template | PAGE##_TEXT: text JSON locked, nguồn và hash, report pass |
| C. Tham chiếu | Registry/album 09 và packet | Mở ảnh, chọn đúng người/vị trí, trang phục theo giai đoạn | Prompt cuối và đường dẫn/hash ảnh thực truyền |
| D. Vẽ | Text locked, ảnh tham chiếu | Sinh tranh nền không chữ, chừa 20% đỉnh, đúng A/B/C; kiểm mặt/tay/vũ khí | PAGE##_ART: PNG native, metadata và báo cáo thị giác |
| E. Ghép chữ | Text và tranh đã kiểm, layout_tokens | Khung giấy cổ, từ khóa đỏ #C81E1E, đủ thoại và số trang | PAGE##_LAYOUT: nguồn sửa được và bản render, đúng khổ, không tràn/che mặt |
| F. QA trang | Scan, sheet, text locked, bản render | Kiểm lịch sử/mỹ thuật/ngôn ngữ/chế bản ở kích thước đọc và zoom 100% | PAGE##_QA: báo cáo bốn lớp, hết lỗi trong phạm vi |
| G. Bìa và trang phụ | Spec bìa, book structure, registry | Bìa trước bốn tầng chữ; bìa sau; hai trang phụ trước và hai trang phụ sau | FRONT/BACK: art → layout → QA; FRONT_MATTER: pagination |
| H. Nhà in | Dữ liệu nhà in thực cấp | Chốt giấy, kiểu đóng, gáy, ICC, PDF preset, font và quyền sử dụng | PRINT_SPEC: profile và bằng chứng; không dùng số ước tính làm số chốt |
| I. Đóng sách | 28 QA, bìa, trang phụ, print profile | Bản đọc riêng, file in riêng; kiểm thứ tự, box PDF, nhúng font và resolution | ASSEMBLY: 32 trang ruột, 4 mặt bìa, delivery manifest có hash |
| J. Bàn giao | Toàn bộ render, file in và manifest | Mở kiểm mọi mặt, check --release, push main và đối chiếu SHA | RELEASE: báo cáo cuối, file sửa được, hướng dẫn sử dụng/nhà in |

Có 125 task: 2 baseline đã hoàn thành, 112 bước cho 28 trang, 6 bước bìa và 5 việc nguồn/trang phụ/in/ghép/phát hành. Việc viết workflow không nâng các task sản xuất thành done.

## Cách agent đi hết quy trình

1. `next` ưu tiên in_progress; nếu không có, chọn todo đã đủ phụ thuộc. Blocked không làm dừng việc độc lập.
2. `packet [ID]` tạo brief, ảnh ứng viên và mẫu báo cáo. Đây chưa phải lệnh sinh ảnh hay tạo thành phẩm.
3. `start ID --owner ... --note ...`; làm phần việc có kết quả thật, rồi checkpoint và commit/push main.
4. Điền bản copy report.v001.json, ghi artifact thật và từng check đã kiểm. `finish` kiểm cấu trúc, file/hash và các điều kiện chữ/ảnh đo được. Sử học và chất lượng thị giác vẫn cần kiểm thật.
5. Chạy check_repo, ghi nhật ký và kinh nghiệm mới, push sau từng phần đã kiểm. Tiếp tục next trong phạm vi đã được người dùng giao; không hỏi lại sau mỗi ảnh nếu đã giao sản xuất trọn phạm vi.
6. Nếu chỉ được giao một phần nhỏ, thực hiện phần đó. Workflow A–Z không tự mở rộng thành lệnh xuất bản thương mại hoặc gửi file cho bên thứ ba.

## Ý nghĩa trạng thái

| Trạng thái | Ý nghĩa |
| --- | --- |
| DESIGN_BASELINE | Thiết kế hiện hành để làm nhất quán, chưa phải chủ dự án duyệt |
| todo / in_progress / blocked / done | Tiến độ tác vụ trong production_state.json |
| report passed | Agent đã kiểm và có bằng chứng trong phạm vi báo cáo |
| USER_APPROVED | Chỉ khi có xác nhận thực từ người dùng và ghi được nguồn xác nhận |
| PRINT_READY | Sau dữ liệu nhà in, QA kỹ thuật và thị giác toàn bộ file in |

## Giới hạn và cách xử lý

Script tự xếp việc, giữ tiến độ, tạo brief, kiểm hash và tạo HTML proof khi có đầu vào thật. Repo không chứa model ảnh, API key, browser hoặc công cụ in thương mại. Agent dùng công cụ sẵn có theo [ma trận năng lực](CAPABILITIES_AND_OUTPUTS.md); thiếu thì block đúng task, ghi cách tiếp tục và làm việc độc lập khác. CI xanh không thay kiểm thị giác hay nguồn.

Trang 27–28 cần nguồn ngoài đoạn trích. Agent có thể chủ động tra cứu nguồn chính thống, mở lại SOURCE_EPILOGUE để làm và ghi đối chiếu. Dữ kiện nhà in/ISBN/quyền sử dụng chưa có phải ghi đúng thiếu; chỉ hỏi dữ liệu bắt buộc còn thiếu khi tới bước cần nó. Các trang và bản xem trước độc lập vẫn tiếp tục được.
