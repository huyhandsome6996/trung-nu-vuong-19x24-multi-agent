---
project: "TRƯNG NỮ VƯƠNG"
book_size: "190mm x 240mm; bleed 196mm x 246mm @300 DPI for final story pages"
target_audience: "Lớp 8–10 (13–16 tuổi)"
compartment: "04_art_direction_and_image_prompts"
agent_author: "ChatGPT / AGENT-04 art production role"
status: "IN_REVIEW"
source_grounding: "CHARACTER_BIBLE_AND_FACTIONS.md mục Trưng Trắc; CHARACTER_DESIGN_PROMPTS.md mục 1; VISUAL_STYLE_BIBLE.md"
date: "2026-11-09"
asset: "assets_generated/characters/CHAR_01_Trung_Trac_v001.png"
use_case: "illustration-story"
generation_method: "built-in image_gen"
approval: "PENDING_USER_REVIEW"
---

# CHAR-01 — Trưng Trắc / bản 001

## Phạm vi

Bảng nhân vật đầu tiên, hai trang phục trên cùng một ảnh: bên trái tang bào trắng tại Cổ Lôi, bên phải giáp đồng vàng và chiến bào đỏ tại Hát Môn. Giữ cùng khuôn mặt để làm tham chiếu xuyên các giai đoạn. Đây là bản thiết kế để duyệt, chưa phải trang ruột hoặc ảnh in 300 DPI; 10 bảng tham chiếu không cộng vào 36 trang sách dự kiến.

Tuổi 26, hoa văn, màu và giáp là lựa chọn thiết kế theo hồ sơ dự án, không phải xác nhận phục dựng khảo cổ. Vùng trống trên cùng dành cho bố cục bảng; không ghép khung dẫn truyện lên sheet.

## Nguồn và cách dùng ảnh mẫu

- Hồ sơ Trưng Trắc trong `02_historical_fairy_tale_adaptation/CHARACTER_BIBLE_AND_FACTIONS.md`.
- Prompt số 1 trong `04_art_direction_and_image_prompts/CHARACTER_DESIGN_PROMPTS.md`.
- Đã xem lại ảnh mẫu `07_reference_assets/sample_an_duong_vuong_sorted/01_Page_01_TemplateA_Mo_Dau_Co_Loa.jpg` để mô tả nét mực/hạt chì. Ảnh này không được truyền làm input pixel và không dùng làm tham chiếu khuôn mặt.
- Không dùng các hồ sơ đang mâu thuẫn như sheet Đô Năng Tế để tạo ảnh này.

## Prompt đã dùng

```text
Use case: illustration-story.
Asset type: first master character reference sheet for a Vietnamese historical fairy-tale comic for ages 13–16, TRUNG NU VUONG, book trim 19×24 cm.
Primary request: Create a polished character sheet of TRUNG TRAC, depicting THE SAME Vietnamese woman, designed age 26, in two full-body costumes side-by-side. Both faces must have identical facial structure and features. This is a clean concept reference, not a finished story page.
Composition: portrait 4:5 canvas, two clearly separated complete figures of equal height with feet and all headdress feathers inside the canvas. Left figure occupies the left half, right figure occupies the right half. Leave generous breathing room around both silhouettes and about 20% quiet neutral parchment at the top. Plain warm cream parchment background, subtle paper grain, no scenery, no border, no captions. Both figures shown in a calm three-quarter standing pose, faces large enough to read, looking slightly toward the viewer. Hands, sword, and scroll must not obscure the faces.
Character identity: dignified, athletic adult Vietnamese woman, natural semi-realistic heroic proportions about 7.5 heads tall, oval face with gently defined jaw, high cheekbones, straight nose, long dark almond-shaped eyes, arched black brows, black hair gathered neatly behind the head, resolute solemn expression, warm medium complexion. Convey commanding intelligence and restrained grief, no smile. Same eye shape, nose, jaw, hairline and skin tone in both figures.
Left costume — Co Loi mourning phase: sacred all-white Lac Viet martial mourning robes, layered ivory-white woven fabric, practical long sleeves, modest full coverage, a simple white mourning headband with trailing white strips, dark hair tied in a bun, no crown, no gold armor, no red fabric. She holds a modest ancient bronze straight sword pointed down at her side, complete blade visible.
Right costume — Hat Mon commander phase: ornate golden-bronze chest and scale armor over a deep crimson-red long war robe, restrained Dong Son concentric sun and Lac-bird patterns, flowing crimson cape, bronze-gold ceremonial headdress with upright white-and-gold feathers. Practical leather belt, fully clothed, armored boots. She holds an ancient bronze straight sword down at her side in one hand and a rolled bamboo edict in the other; bamboo surfaces completely blank. Preserve the same woman beneath the headdress.
Art direction: traditional Vietnamese heroic fairy-tale comic illustration, crisp hand-drawn black ink outlines with bold-to-fine line variation, detailed visible cross-hatching in shadows, vibrant textured watercolor and colored-pencil grain, hand-made printed storybook feeling, rich bronze-gold and crimson contrasting the ivory left costume, controlled warm light, convincing anatomy and expressive faces. Dense hand-worked ink and pencil texture like a classic historical comic, not smooth digital concept art.
Constraints: absolutely text-free, no letters, no pseudo-writing, no labels, no speech bubbles, no watermark, no logo, no color-swatch labels. Exactly two full-body depictions of ONE character; no extra people, no portraits floating on the page. No chibi, no large anime eyes, no 3D, no photorealism, no fantasy plate armor, no modern objects, no exposed midriff, no cropped feet or weapons.
```

## Kiểm tra sau sinh

- Đã mở xem ảnh sinh và kiểm file PNG giải mã được: **1122×1402 px**, chế độ **RGB**; SHA-256 `3387a36a801705d08b9eac3dd778aca3533fced07300db8188cd71439eeec3c3`.
- Đúng hai hình toàn thân, cùng nhân vật; khuôn mặt tương đồng rõ về mắt, mũi, cằm và đường tóc. Chưa có ảnh gốc khuôn mặt do chủ dự án duyệt để đo đồng nhất.
- Tang bào trắng và khăn tang bên trái; giáp vàng đồng, áo/choàng đỏ, mũ lông vũ, kiếm và thẻ tre bên phải hiện rõ. Hai chân và mũi kiếm nằm trong khung.
- Quan sát chưa thấy chữ, nhãn, watermark hoặc bóng thoại; hoa văn là trang trí. Chưa kiểm OCR tự động.
- Nét mực và hạt chì rõ; tông giấy ấm khá đồng đều, cần chủ dự án duyệt độ rực màu và gương mặt trước khi dùng làm style master.
- Đỉnh mũ của hình bên phải đi vào 20% phía trên; **không đạt khoảng trống 20% trên toàn bề ngang nếu coi đây là trang ruột**. Đây là sheet tham chiếu, không dùng trực tiếp làm tranh nền trang có khung dẫn.
- Hai hình đứng tương tự nhau; chưa có góc nghiêng, phía sau hay biểu cảm bổ sung. Chưa gọi đây là turnaround đầy đủ.
- Kích thước trên là ảnh gốc công cụ, **chưa phải 2315×2906 px / 300 DPI để in trang truyện**. Không nội suy ảnh chỉ để gắn nhãn đạt chuẩn in.
- Trạng thái: **IN_REVIEW / PENDING_USER_REVIEW**; chưa APPROVED, chưa dùng để sinh các trang 01–28.

## Bàn giao

Chủ dự án xem khuôn mặt, mức trưởng thành, mũ/giáp và chất liệu nét vẽ. Nếu cần sửa, tạo `v002` và giữ `v001` để so sánh; nếu được chốt, ghi thông tin duyệt rồi dùng đúng ảnh đó làm tham chiếu cho cảnh có Trưng Trắc. Các sheets còn lại tiếp tục theo cùng chất liệu sau khi mẫu đầu đã được duyệt.
