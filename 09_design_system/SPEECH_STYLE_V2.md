# Bóng thoại v2 — chữ và khung được vẽ cùng nhau

Yêu cầu trực tiếp của chủ dự án10/11/2026 thay cách làm thoại trước đây. Mẫu hiện có: `final_book_19x24/proofs/PAGE12_v003.png`; asset có alpha: `assets_generated/speech_clouds/PAGE12_SPEECH01_v001.png`. Đây là bản agent đã kiểm, chưa phải chủ dự án duyệt.

- Vẽ **khung và toàn bộ chữ thoại thành cùng một asset bằng công cụ tạo ảnh thực**. Có thể vẽ trực tiếp vào bản chế bản hoặc tạo asset RGBA rồi đặt vào cảnh; với asset riêng phải giữ nguyên màu/nét, không kéo méo. Đặt asset là một thành phần có thể di chuyển trong SVG/PDF.
- Bóng thoại organic bằng nét mực có độ nhấn, hình mây/oval mềm; sắc ngà, xám kem hoặc phản quang ấm/lạnh tùy cảnh. Giấy và grain nhẹ; đường viền hợp độ đậm nét tranh. Không dùng thẻ trắng tinh bo góc kiểu giao diện, bóng đổ3D hay đuôi tam giác dài xuyên mặt.
- Chữ được vẽ sẵn trong khung, mực tối tương phản, humanist/serif hoặc nét lettering truyện Việt dễ đọc, đầy đủ dấu. Không dùng thư pháp rối. Người nói bình tĩnh: nét mềm; tiếng hô/giận dữ: biên mạnh hơn phù hợp diễn xuất. Không coi một mẫu màu vàng là đáp án cho mọi cảnh.
- Soạn nguyên văn thoại đã khóa trước khi sinh. Chừa đủ khoảng cho số dòng thực; không rút câu, sửa tên, bỏ từ/dấu để làm vừa khung. Mở ảnh và đọc từng tiếng/dấu ở kích thước đọc và zoom; lỗi chữ thì sửa/sinh lại asset.
- Đuôi ngắn, cong tự nhiên, đến góc miệng đúng người; không che mắt, tay, vũ khí hoặc đi qua mặt người khác. Với nhóm hô, bố trí theo nhóm thay vì một đường dài xuyên đám đông. Tranh thô vẫn giữ riêng sạch chữ; lời dẫn vẫn theo parchment/từ khóa đỏ trong layout_tokens.
- Lưu PNG native, prompt chính xác, actual_references và SHA thật, nguyên văn thoại, người nói, bản vẽ và tọa độ đặt. Giữ mọi bản cũ. Không đổi DPI hoặc resize rồi báo có thêm chi tiết gốc.
- `scripts/render_page.py` hỗ trợ placement có `lettered_asset` và `bbox_mm`. JSON cạnh PNG phải chứa `text` đúng thoại, `sha256`, `status: visual_text_verified` **chỉ sau kiểm thị giác thật**. Không tự gắn nhãn này bằng OCR hoặc chỉ vì lệnh sinh thành công. PDF extraction không chứng minh chính tả của chữ nằm trong ảnh.

Các trang cũ có thoại03/04/06/07/09/10/11 thuộc coordinator để sửa tiếp; AgentA14–20 và AgentB21–28 áp dụng ngay v2. Không sửa file `SOURCE_DECISIONS.md`/storyboard/registry dùng chung trong lúc hai lane hoạt động.
