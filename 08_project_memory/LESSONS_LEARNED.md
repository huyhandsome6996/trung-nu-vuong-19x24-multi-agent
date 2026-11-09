---
project: "TRƯNG NỮ VƯƠNG - Truyện Cổ Tích Lịch Sử Hào Hùng"
book_size: "190mm x 240mm (Bleed: 196mm x 246mm @ 300 DPI)"
target_audience: "Học sinh Lớp 8 - Lớp 10 (13-16 tuổi)"
compartment: "08_project_memory"
agent_author: "ChatGPT / Lead Agent (onboarding và rà soát QA)"
status: "IN_REVIEW"
source_grounding: "59 file tại commit 65c2e5a7cf71a1344be7f916c9b675e4325d31c8 và chỉ dẫn trực tiếp ngày 2026-11-09"
review_date: "2026-11-09"
timezone: "Asia/Ho_Chi_Minh"
---

# Kinh nghiệm thực tế từ lần onboarding đầu

## 1. Đếm bằng Git và gắn commit

**Đã gặp:** yêu cầu xác nhận “59 file” nhưng còn phải tạo tài liệu mới. **Cách làm:** chụp danh mục `git ls-tree` ở commit nền, đếm loại file, lập hash. **Bài học:** số file gốc và số file hiện tại là hai số khác nhau; không tiếp tục nói repo chỉ có 59 file sau khi bổ sung.

## 2. Ảnh scan là căn cứ khi các bản Markdown bất đồng

**Đã gặp:** rồng/khổng tước bị đổi chiều, số voi thành 78, số phát tên không nhất quán và giới tính sư phụ khác mô tả scan. **Cách làm:** xem đủ 10 contact sheets, ghi trang PDF/trang sách/file liên quan vào sổ vấn đề. **Bài học:** một khẳng định được sao chép qua nhiều `.md` chưa trở thành bằng chứng. Khi làm chi tiết, crop trang scan đủ nét rồi mới sửa đồng bộ nguồn phân tích → Bible → storyboard → prompt.

## 3. Đọc đúng vai trò của từng tài liệu

Bible hướng dẫn nhận diện; storyboard khóa cảnh/chữ; prompt điều khiển tranh; thông số chế bản điều khiển hình học. **Đã gặp:** Trưng Nhị lam sẫm ở sheet nhưng đỏ/vàng ở prompt cảnh. **Bài học:** mỗi lần sinh trang cần đối chiếu cả hồ sơ và ảnh đã duyệt, không chỉ copy prompt trang.

## 4. Đọc hết không đồng nghĩa sẵn sàng sản xuất

**Đã gặp:** đầy đủ 28 storyboard và 30 prompt bìa/trang nhưng chưa có sheets được chốt, trang kết vượt đoạn nguồn và safe zone mâu thuẫn. **Bài học:** báo cáo riêng tiến độ đọc, tiến độ quyết định và tiến độ sản phẩm; IN_REVIEW không phải APPROVED.

## 5. Đơn vị và hệ tọa độ phải có tên rõ ràng

**Đã gặp:** khung top=8 mm được mô tả đồng thời nằm trọn trong vùng cách trim 14 mm; CSS cắt ở trim nhưng gọi là sẵn in bleed. **Cách làm:** ghi hệ gốc trim và phép dịch +3 mm sang bleed. **Bài học:** kiểm bằng bất đẳng thức tọa độ và hộp PDF thực, không chỉ nhìn con số 300 DPI. Khi crop raster có chênh lẻ 71 px phải phân 35/36 px có chủ ý.

## 6. Không tin nhãn đếm từ có sẵn

**Đã gặp:** nhãn số từ trong storyboard thấp hơn phép đếm theo khoảng trắng. **Cách làm:** chỉ trích lời dẫn, đếm lại và thống kê cụm/tỷ lệ đỏ. **Bài học:** công bố phương pháp đếm; dùng bản dựng font thật để quyết định có đủ 3–5 dòng. Không xóa tự động các dấu tô đỏ cho đạt tỷ lệ.

## 7. Ví dụ mã trong Markdown chưa là công cụ hoàn chỉnh

**Đã gặp:** ngăn 05 có CSS và hàm regex nhưng không có entrypoint, tài nguyên font, script ghép đủ sách hoặc kiểm hộp in. **Bài học:** chỉ mô tả là bộ khung đặc tả; ở nhiệm vụ lập trình sau phải tạo pipeline chạy được rồi kiểm sản phẩm xuất thực tế.

## 8. Git phải giữ thay đổi nhỏ và bí mật ngoài repo

**Cách làm:** dùng remote HTTPS sạch, nhánh QA và commit tài liệu theo phạm vi; chỉ xem push là xong sau khi đối chiếu SHA remote. Thông tin đăng nhập chỉ dùng tạm cho xác thực, không đưa vào docs hay log. **Bài học:** mỗi lần bàn giao ghi nhánh/commit; nếu push lỗi ghi đúng lỗi, không báo đã đồng bộ.

## 9. Tạo mẫu đầu để duyệt ngoại hình, giữ nguyên bản gốc

**Đã làm:** sheet Trưng Trắc v001 chứa cùng một gương mặt ở tang bào và giáp chiến, tên file có phiên bản, prompt nguyên văn và JSON kèm hash. **Quan sát:** nét mực/chì lên rõ nhưng vùng trống 20% không được giữ toàn bề ngang vì mũ lông vũ. **Bài học:** bảng nhân vật và nền trang truyện có công năng khác nhau; không gọi sheet là trang in sẵn. Đo kích thước thực tế sau sinh, chờ chủ dự án duyệt rồi mới dùng làm tham chiếu. Không tự resize để tạo cảm giác đạt độ phân giải in.

## 10. Một kiểu nét không có nghĩa một khuôn mặt

Tạo cả dàn từ cùng ảnh Trưng Trắc giúp giữ chất liệu, nhưng dễ khiến nữ tướng giống nhau. Gán riêng dáng hàm, mày, tóc, độ tuổi, màu và đạo cụ; ghi tên/mã/vị trí trên bảng nhóm. Khi vẽ lại một người mới giữ mặt, khi vẽ người khác chỉ giữ phong cách. Không tuyên bố “đồng nhất100%” nếu chưa kiểm bản trang.

## 11. Prompt không phải bằng chứng kiểm đạt

Bảng phương tiện vẫn sinh đèn kính dù yêu cầu cổ xưa; huyết sâm ở một bảng ra màu vàng trong khi bối cảnh dùng đỏ. Phải xem ảnh, sửa đúng ô/vật và lưuv002, không đổi vài chữ prompt rồi báo ảnh đã sửa. Sau sửa cập nhật file hiện hành trong registry/catalog/metadata; giữ bản cũ và gắn SUPERSEDED.

## 12. Bảng đông người cần khóa vị trí

Bộ24 tộc trưởng dùng4hàng×6cột, mã ML01..ML17 rồi PH01..PH07. Cần tính đúng chỉ số: PH03 là người thứ20, hàng4/cột2. Đếm bằng lưới và xem ảnh; cập nhật màu khăn thực tế. Không chỉ dựa tên “họ Bạch/Khúc” vì các nhân vật khác nhau có thể cùng họ.

## 13. Tách concept, bản trang và file in

Bảng nhân vật/bối cảnh nhiều ô hữu ích để tham chiếu, không đủ điều kiện làm ngay trang in19×24. Lấy kích thước thật sau sinh; giữ hash bản gốc; chỉ tạo preview nhỏ để album tải nhanh. Khi làm trang phải sinh tranh riêng có khoảng trống đỉnh, rồi ghép chữ và kiểm kỹ thuật in thực tế.

## 14. Tạo lối vào ngắn cho người không muốn đọc truyện

Một album hình có tên, mã và vị trí, cộng bản tóm tắt2phút giúp chủ dự án đánh giá nhanh hơn hàng chục file mô tả. Agent vẫn có41 hồ sơ chi tiết, ma trận28trang, JSON và hướng dẫn. Không bắt chủ dự án trả lời lại thông tin vốn có trong nguồn.

## 15. Kiểm toàn chuỗi tham chiếu sau khi sửa phiên bản

Đổi filev002 phải đổi ảnh album, thumbnail, metadata, prompt sửa, trạng thái bản cũ và nguồn ảnh thực sự đã truyền. Validator kiểm ID/file/hash/phiên bản và link; không thay kiểm mắt. Khuôn SVG có thể render bằng Inkscape ngay cả khi runtime Python không có CairoSVG. Không báo đã kiểm Chromium khi máy không có browser binary.

## Workflow một main và tiếp tục sau ngắt phiên

**Đã gặp:** chủ dự án khó biết công việc có mất sau phiên dài bị ngắt, thiết kế đầy đủ nằm ở nhánh phụ nên mở main không thấy.

**Cách làm:** hợp nhất lịch sử vào main; README có một lối vào. Tách queue theo TEXT → ART → LAYOUT → QA cho từng trang, phụ thuộc cụ thể và evidence có hash. Checkpoint ghi file thật và bước tiếp, commit/push sau từng phần; next ưu tiên task đang dở. Reopen một đầu vào phải mở lại downstream, giữ bằng chứng và phiên bản cũ.

**Bài học:** tác vụ được ghi “done” phải có sản phẩm và kiểm chứng. Một danh sách TODO trong Markdown chưa đủ để agent xác định việc đang dở; một báo cáo pass chưa đủ chứng minh chất lượng hình. Repo dùng main vẫn cần một người ghi tại một thời điểm và pull trước push. Không hứa chống mất dữ liệu nếu artifact chưa được lưu/push.

## Đếm thật trước khi khóa chữ

Tiêu đề cũ ghi 52–60 từ nhưng một số lời dẫn thực tế dài hơn 65 tiếng. Đếm theo khoảng trắng trên chữ thực, giữ từ khóa, đối chiếu nguồn và kiểm 3–5 dòng bằng renderer. Không tin nhãn đếm cũ, không cắt thoại hoặc thu nhỏ font chỉ để vừa hộp. Draft do packet tạo chưa chép thoại phải có nhãn rõ, tránh chế bản thiếu lời nhân vật.

## Sản xuất trang đầu: kiểm font và pixel thực

50–65tiếng không bảođảm vừa29mm: đo NotoSans thực trướckhóa. Giữcỡfont, rút câunối, giữtừkhóa vàthoại; reopen downstream cóevidence cũ. Parser tôđỏ phảigiữ khoảngtrắng ở cảhai phía dấu**, và kiểmmắt vì sochuỗi bỏwhitespace sẽbỏsót lỗi dínhchữ.

Ảnhsinh cóthể khôngđúng tỷlệ dù prompt ghi kíchthước. Giữnative, sửa bố cục bằngcôngcụảnh, khôngkéoméo; ghi referencev002 thực tế làv001,khôngkhai sheettruyềngián tiếp làinputtrực tiếp.

Renderer cóthểtrả mã0 nhưngPNGthiếu dữliệu; dùngPillow.verify vàPoppler hệthống thực. Render300DPI khôngbiến tranh145DPI thànhtranhchi tiết300DPI.

## Clip tranh trong dàn trang và provenance bất biến

Công cụ ảnh có thể tạo đúng hai cảnh nhưng rãnh không đúng tọa độ. Dùng crop vector từng cảnh sau khi xem pixel để đặt đúng khung, giữ tỷ lệ đồng nhất, kiểm đầu/tay/chân lại trên render; không kéo méo hoặc sửa ảnh native rồi gọi là nguyên bản. Lưu cropJSON và độ phân giải hiệu dụng riêng từng khung.

Không đưa script dùng chung vào evidence bất biến của trang đã khóa: lưu snapshot đúng byte, để các trang sau phát triển renderer mà không làm stale báo cáo cũ.

Khi sinh ảnh bất đồng bộ, lưu request hoàn chỉnh trước lúc gọi; chỉ ghi kết quả sau khi công cụ trả xong. Dữ liệu store trong cell đang chạy có thể chưa khả dụng ở cell khác. Từ chối các prompt placeholder như undefined trong validator; nếu đã ghi sai phải giữ phiên bản cũ và mở lại chuỗi để sửa có bằng chứng.
