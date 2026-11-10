# Agent B — checkpoint bị ngắt, chưa hoàn thành lô21–28

13/32bước đã done;3trang21–23 đủTEXT→ART→LAYOUT→QA. Trang24 chỉTEXTdone, ARTblocked vì lệnhảnh bịngắt, khôngoutput. Trang25–28 còn todo; các TEXT vẫn cóthể làmđộc lập, không giả là toàn bộ việc còn lại blocked.

| Trang | TEXT | raw | speech | layout / placement | Trạng thái |
| --- | --- | --- | --- | --- | --- |
|21|v001|v001|v001|v001 / v001|4bước done|
|22|v003|v001|v002|v007 / v006|4bước done; giữ các nháp cũ|
|23|v001|v001|v001|v001 / v001|4bước done|
|24|v001|chưa có|không thoại|chưa có|ARTbịngắt; attemptv001/promptv001|
|25–28|chưa khóa|chưa có|chưa làm|chưa có|todo|

## File và bằng chứng

- Manifest: `10_agent_workflow/parallel/agent_b/manifest.v001.json`, từng artifact/path/SHA256/bytes, phiên bản và DPI đo thật.
- Bản đọc3trang: `assets_generated/parallel/agent_b/AGENT_B_PAGES21_23_CHECKPOINT_v001.pdf` (đã mở bằngpypdf,3trang có nội dung).
- Từng trang có JSON chữ, nguyênthoại/promptthực, rawPNG/metarefhash, speechPNG-RGBA/metatext, SVG/PDFproof/PDFđọc, PNG150/300/detail, placementvàreport4bước.
- Source chỉnh sửa đúng phạm vi; renderer chung không sửa, snapshot byte tronglane. Không đổi source/storyboard/registry/state/logchung.

## Kiểm và giới hạn

Đã mở pixel scan43–58, các sheet thực truyền, raw/speech và render toàntrang150/detail300; đọc từngtiếng/dấu. NotoSansRegular/Bold nhúng, fontglyph/overflow/PDFkhôngrỗng/media196×246/trim190×240 kiểmđạt. Lời dẫn21=51tiếng,22=42,23=46,24=54. Báo cáo và metadata có số native thực; raw21=1122×1402(~145DPI),raw22=1119×1405(~145DPI),raw23 xemmetrics. ĐổiDPI/render300khônglàm tăngchitiết. AGENT_QA, khôngUSER_APPROVED/PRINT_READY.

Trang21là kếhoạch. Trang24khôngcho toàn600vàokhe, Tào/Lụcởnhàgỗ, khôngbịa lướimây/gỗđáchặnkhe. Trang23khôngvẽTàocưỡingựa vìscan khôngxácnhận. Đoàn30thuyền được thuật lại bằng chữ; tranh chỉ thểhiện mộtphần, không khai đãđếm30vậtthể.

## Tiếp tục

Lệnhảnh24bị người dùng ngắt sau79giây, không còn jobnền nào đượcxácnhận; không có raw24trongcache đãkiểm. `unblock PAGE24_ART` rồi `start` và tạo requestv002 bấtbiến, sinh/mở ảnhthật. Hoặc `next` chọn TEXT25. Đọc SRC-05và SOURCE_EPILOGUE trước27–28; E14chỉlà biểu tượng, khởi nghĩa năm40.

Không chạy integrate_parallel. Coordinator cóthể xem3trang đãQA, nhưng chưa tích hợp toànlane. Không nhúng SHA của commit chứaHANDOFF; SHAđồngbộ cuối được trả trong tin nhắn sauwrapper.
