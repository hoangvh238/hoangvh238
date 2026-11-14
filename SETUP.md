# Cài đặt profile README

1. Tạo hoặc mở repository public `hoangvh238/hoangvh238` trên GitHub.
2. Upload `README.md` và cả thư mục `assets/` vào thư mục gốc của repository.
3. Commit thay đổi, rồi mở profile `https://github.com/hoangvh238` để xem.

Không cần upload file hướng dẫn này hoặc `generate_assets.py` nếu không muốn.

## Những gì đã chuẩn bị

- README tiếng Anh với nội dung lấy từ profile công khai và ảnh GitHub bạn cung cấp.
- Banner aurora và thẻ thành tích GIF: mỗi ảnh 48 frame, chu kỳ 6 giây, loop liên tục.
- Ảnh PNG dự phòng qua `picture` cho thiết bị có cài đặt giảm chuyển động (tùy hỗ trợ trình duyệt / bộ lọc GitHub).
- Ảnh và README không có doanh thu, MRR, lifetime earnings hoặc hourly rate.
- Không gắn hyperlink về UpworkRank, Upwork hay referral/tracking URL.
- Chỉ giữ link GitHub, LinkedIn và LeetCode của bạn.

## Vì sao không nhúng script đã gửi?

GitHub README loại bỏ script, style và CSS inline. Đoạn `w.js` không chạy trong profile README.
Bản này tái tạo phong cách aurora và hiển thị số liệu bằng ảnh GIF nội bộ trong repo; không tải widget bên thứ ba.
Không phải live widget. Không có cơ chế tự đồng bộ số liệu.

## Số liệu

Đã đọc trực tiếp profile công khai ngày 14/11/2026: Top Rated, 100% Job Success, 31 completed jobs, AI Development #703 / Top 8%.
Giữ tên nguồn bằng chữ, không gắn link. Rank là chỉ số của dịch vụ bên thứ ba, không phải điểm đánh giá kỹ năng.
Các tuyên bố về quy mô người dùng, mức cải thiện hiệu năng và thời gian tiết kiệm không đưa vào README vì chưa xác minh độc lập.

## Cập nhật ảnh

Sửa số liệu / ngày trong `generate_assets.py` và alt text / ngày trong `README.md`.
Cài Python, Pillow và NumPy; cập nhật FONT/BOLD/MONO trong script thành đường dẫn font trên máy bạn, rồi chạy:

```bash
python generate_assets.py
```

Upload lại các ảnh vừa tạo. File đầu tiên và cuối cùng nối tiếp theo chu kỳ; GIF không có link ngoài.
