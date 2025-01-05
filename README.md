
# HỆ THỐNG ĐIỂM DANH TỰ ĐỘNG
Hệ thống điểm danh tự động được phát triển nhằm tự động hóa quy trình ghi nhận sự có mặt trong các buổi học, họp hoặc làm việc. Hệ thống sử dụng công nghệ nhận diện khuôn mặt để tăng tính chính xác, giảm thiểu sai sót, và tiết kiệm thời gian.



## Tính năng nổi bật

- Nhận diện khuôn mặt nhanh và chính xác.
- Ghi nhận và lưu trữ thông tin điểm danh tự động.
- Xuất báo cáo thống kê chi tiết.
- Quản lý danh sách người tham gia dễ dàng.
- Tích hợp với camera laptop hoặc camera rời.
- Phần cứng: Raspberry Pi (tùy chọn), camera laptop hoặc camera USB



## Các công nghệ sử dụng
- Ngôn ngữ: Python 3.12.
- Ngôn ngữ đánh dấu: HTML, CSS.
- Thư viện: OpenCV, NumPy, Face Recognition, Pandas
- Cơ sở dữ liệu: SQLite/MySQL



## Các thư viện yêu cầu

asgiref (3.8.1)
Django (5.1.4)
PyMySQL (1.1.1)
sqlparse (0.5.3)

- Q: Làm thế nào để cài đặt những thư viện này nhanh nhất ?
- A: Rất đơn giản hãy cài đặt những thư viện thông qua file requirements.txt trong project này

```bash
  pip install -r requirements.txt
```
- Lưu ý: ta cần cập nhật pip thông qua python venv để tăng sự hiểu quả
- Q: Nếu tôi có thử tải những thư viện về và muốn thêm vào requirements.txt để cho các thành viên thì ta nên làm gì ?
- A: Ta cần dùng lệnh cd vào thư mục cần tìm thư viện sau đó thử lệnh này
  
```bash
  pip freeze
```

## Làm thế nảo để tải project về máy ?
- Để cần clone project này ta cần đảm bảo đã tải git.
- Bước 1: Vào Visual Studio Code tạo một thư mục trống để chứa project
- Bước 2: clone repository ta cần thực hiện câu lệnh này ở Teminal
```bash
    git clone https://github.com/LeMinhSang2k5/Nhom-9_PhanMemDiemDanh_Raspberry-Pi.git
 ```
## Cài đặt phần cứng (nếu sử dụng Raspberry Pi)

- Kết nối camera và Raspberry Pi theo hướng dẫn.
- Đảm bảo Raspberry Pi OS đã cài driver cho camera.


## Hướng dẫn sử dụng

1. Nhập danh sách người tham gia bằng tay hoặc import từ file CSV.
2. Bật camera và bắt đầu quá trình điểm danh.
3. Xem báo cáo chi tiết trong giao diện quản lý.




## Tác giả
- Project này được đóng góp bởi những người sau đây
- [@LeMinhSang](https://github.com/LeMinhSang2k5)
- [@NguyenHoaiLinh](https://github.com/linh0526)
- [@TrinhMinhKhang](https://github.com/MinhKhangVN)
- [@KhuuTanPhat](https://github.com/tanphat2108)
- [@LeHoanToan](https://github.com/lehoangtoan)
- [@NguyenCaoKyDuyen](https://github.com/KyDuyen09)
- [@LeMinhNhut](https://github.com/minhut205)
## Liên Hệ

Mọi góp ý, hãy liên hệ qua Email này sanglm1900@gmail.com


## Project này được nghiên cứu và phát triển tại Trường Đại Học Giao Thông Vận Tải TP.HCM
<p align="center">
  <img src="https://github.com/user-attachments/assets/a41dc4b7-6d14-4618-8f7a-f3afe9b83784" alt="Logo-GTVT-300x205" width="300"/>
</p>


