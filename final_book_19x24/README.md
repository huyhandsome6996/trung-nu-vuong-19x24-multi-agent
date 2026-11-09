# Đầu ra chế bản và bàn giao

Chưa có file in sẵn sàng. Các đường dẫn dưới đây dành cho sản phẩm thật khi tác vụ tương ứng hoàn thành.

| Đường dẫn | Nội dung |
| --- | --- |
| `source/` | Nguồn chế bản có thể sửa |
| `proofs/` | HTML/PNG/PDF để đọc và kiểm |
| `reading/` | Bản đọc, không mặc định coi là file in |
| `print/` | Ruột 32 trang và bìa trải với gáy thực đã chốt |
| `pagination.json` | 2 trang phụ trước +28 truyện +2 trang phụ sau; 4 mặt bìa riêng |
| `print_profile.json` | Nhà in, font, ICC, kiểu đóng, gáy và quyền sử dụng |
| `delivery_manifest.json` | File bàn giao, kích thước, hash và trạng thái QA |

Thông số theo [layout_tokens](../09_design_system/layout_components/layout_tokens.json). File in cần TrimBox 190×240 mm, BleedBox 196×246 mm, nhúng font và đủ độ phân giải hiệu dụng. Gáy 3.5 mm là ước tính chưa chốt. Không tự tạo ISBN, nhà xuất bản hoặc giấy phép giả.
