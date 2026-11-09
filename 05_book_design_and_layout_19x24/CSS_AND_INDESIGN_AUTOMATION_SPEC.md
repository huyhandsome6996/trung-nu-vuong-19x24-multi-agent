# MÃ NGUỒN TỰ ĐỘNG HÓA DÀN TRANG KHỔ 19x24 CM (HTML/CSS & PYTHON COMPOSITING PIPELINE)

Tài liệu này cung cấp sẵn bộ khung mã nguồn **HTML5/CSS3 chuẩn in ấn `@page { size: 190mm 240mm; }`** và hàm chuyển đổi Markdown `**từ khóa đỏ**` sang thẻ `<span class="red-kw">` để `AGENT-05` có thể tự động hóa 100% việc đóng cuốn PDF khổ 19×24 cm bằng Headless Chromium hoặc Pillow.

## 1. Bản Mẫu CSS Chuẩn Khổ Sách 19x24 cm (`book_19x24_template.css`)

```css
/* Thiết lập khổ trang in vật lý 190mm x 240mm (Khổ 19x24cm) */
@page {
  size: 190mm 240mm;
  margin: 0;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  width: 190mm;
  font-family: 'Noto Sans', 'Baloo 2', 'Segoe UI', sans-serif;
  background-color: #111827;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* Mỗi trang sách là một khung cố định 190mm x 240mm */
.story-page {
  position: relative;
  width: 190mm;
  height: 240mm;
  overflow: hidden;
  page-break-after: always;
  break-after: page;
  background-color: #fef3c7;
}

/* Lớp tranh minh họa nền toàn trang */
.story-page .bg-illustration {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

/* Khung dẫn truyện giấy cổ ở đỉnh trang (Học từ 22 ảnh JPG mẫu) */
.narration-scroll-box {
  position: absolute;
  top: 8mm;
  left: 11mm;
  right: 11mm;
  min-height: 36mm;
  padding: 4.5mm 6.5mm;
  z-index: 10;
  background: radial-gradient(circle at center, #FFFBEB 0%, #FEF3C7 68%, #FDE68A 92%, #F59E0B 100%);
  border: 1.1mm solid #1C1917;
  border-radius: 4.5mm;
  box-shadow:
    0 1.2mm 3.5mm rgba(0, 0, 0, 0.55),
    inset 0 0 2.5mm rgba(180, 83, 9, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.narration-scroll-box p {
  font-size: 12.8pt;
  line-height: 1.42;
  font-weight: 700;
  color: #1A1A1A;
  letter-spacing: 0.1px;
}

/* Từ khóa tô đỏ (#C81E1E) giống hệt mẫu An Dương Vương */
.narration-scroll-box .red-kw {
  color: #C81E1E;
  font-weight: 800;
}

/* Bóng thoại nhân vật (Speech Bubble) */
.speech-bubble {
  position: absolute;
  z-index: 15;
  max-width: 78mm;
  padding: 3.5mm 4.5mm;
  background: #FFFFFF;
  border: 0.8mm solid #111827;
  border-radius: 50% / 38%;
  box-shadow: 0 1mm 2.5mm rgba(0, 0, 0, 0.35);
  text-align: center;
  font-size: 10.8pt;
  line-height: 1.35;
  font-weight: 700;
  color: #111827;
}

/* Huy hiệu số trang ở góc dưới */
.page-folio {
  position: absolute;
  bottom: 6mm;
  right: 8mm;
  width: 8mm;
  height: 8mm;
  border-radius: 50%;
  background: #991B1B;
  border: 0.5mm solid #F59E0B;
  color: #FEF3C7;
  font-size: 9pt;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 20;
}
```

## 2. Hàm Python Chuyển đổi Kịch bản Markdown sang HTML Tô Đỏ Tự động (`render_helper.py`)

Khi `AGENT-05` đọc phần **Text Khung Dẫn Truyện** từ Ngăn 03 (ví dụ: `"Trước vòng vây của hơn hai ngàn quân giặc, **Huyện lệnh Thi Sách** dứt khoát..."`), hãy dùng hàm Python dưới đây để tự động chuyển cặp dấu `**...**` thành `<span class="red-kw">...</span>`:

```python
import re

def format_narration_html(md_text: str) -> str:
    """
    Chuyển đổi chuỗi Markdown có **từ khóa** thành HTML có class .red-kw (#C81E1E)
    theo đúng mẫu truyện cổ tích An Dương Vương.
    """
    clean = md_text.strip().lstrip(">").strip()
    html_text = re.sub(
        r"\*\*(.+?)\*\*",
        r'<span class="red-kw">\1</span>',
        clean
    )
    return f'<div class="narration-scroll-box"><p>{html_text}</p></div>'
```
