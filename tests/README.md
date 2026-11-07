# 🧪 TÀI LIỆU HỆ THỐNG KIỂM THỬ TỰ ĐỘNG (UNIT TESTS)

Thư mục `tests/` chứa toàn bộ các bài kiểm thử tự động (Unit Tests) được xây dựng theo chuẩn thư viện `unittest` của Python, tương thích 100% với barem chấm thi của đề thi kết thúc môn học **Lập trình Python - Mã đề 11301** (Trường Cao đẳng Công Thương TP.HCM).

---

## 📋 Bảng Phân Bổ Điểm & Ánh Xạ Test Cases

Tổng điểm bài thi là **10.0 điểm**, được chia đều cho 5 câu hỏi (mỗi câu 2.0 điểm):

| Câu hỏi | Ý | Nội dung yêu cầu | Điểm tối đa | File kiểm thử tương ứng | Test methods |
| :---: | :---: | :--- | :---: | :--- | :--- |
| **Câu 1** | a | Kiểm tra giá trị $n \in [1; 99]$, yêu cầu nhập lại nếu sai | 0.5 | `test_cau1.py` | `test_kiem_tra_n_valid`<br>`test_kiem_tra_n_invalid`<br>`test_nhap_n_single_try`<br>`test_nhap_n_retry` |
| | b | Viết hàm `TongUocSo(n)` tính tổng các ước số | 0.75 | `test_cau1.py` | `test_tong_uoc_so_standard`<br>`test_tong_uoc_so_prime`<br>`test_tong_uoc_so_edge_cases` |
| | c | Viết hàm con tính $S = 1 + 2^2 + 3^3 + \dots + n^n$ | 0.75 | `test_cau1.py` | `test_tinh_s`<br>`test_main_cau1` |
| **Câu 2** | a | Đếm số ký tự chữ thường có trong chuỗi $s$ | 1.0 | `test_cau2.py` | `test_dem_chu_thuong`<br>`test_main_no_lowercase` |
| | b | Kiểm tra xem chuỗi $s$ có đối xứng hay không (`DoiXung`) | 0.5 | `test_cau2.py` | `test_doi_xung`<br>`test_main_palindrome_with_lowercase`<br>`test_main_non_palindrome` |
| | c | Đổi tất cả ký tự đầu tiên của mỗi từ thành chữ hoa | 0.5 | `test_cau2.py` | `test_viet_hoa_dau_tu` |
| **Câu 3** | a | Nhập số nguyên vào danh sách, dừng khi nhập 0 | 0.75 | `test_cau3.py` | `test_nhap_danh_sach` |
| | b | Lọc và in ra các số dương chẵn trong danh sách | 0.75 | `test_cau3.py` | `test_loc_duong_chan_mixed`<br>`test_loc_duong_chan_none` |
| | c | Đếm số lần xuất hiện của phần tử $k$ trong danh sách | 0.5 | `test_cau3.py` | `test_dem_phan_tu`<br>`test_main_has_even_and_found_k`<br>`test_main_no_even_and_not_found_k` |
| **Câu 4** | a | Nhập thông tin máy tính lưu vào từ điển theo cấu trúc danh sách | 1.5 | `test_cau4.py` | `test_them_may_tinh`<br>`test_main_delete_success` |
| | b | Nhập số hiệu máy tính, xóa nếu có hoặc thông báo không tìm thấy | 0.5 | `test_cau4.py` | `test_xoa_may_tinh_thanh_cong`<br>`test_xoa_may_tinh_khong_ton_tai`<br>`test_main_delete_fail` |
| **Câu 5** | a | Lớp `MonHoc` có thuộc tính và phương thức `thongtinmonhoc()` | 1.0 | `test_cau5.py` | `test_khoi_tao_mon_hoc_csdl`<br>`test_phuong_thuc_thongtinmonhoc` |
| | b | Khởi tạo 2 đối tượng mẫu và gọi `thongtinmonhoc()` | 1.0 | `test_cau5.py` | `test_khoi_tao_mon_hoc_ta1`<br>`test_main_cau5` |
| **TỔNG** | | **5 câu hỏi** | **10.0** | **5 file tests** | **30 test cases** |

---

## 🚀 Hướng Dẫn Chạy Kiểm Thử

### 1. Chạy chấm điểm tự động (Khuyên dùng)
Ở thư mục gốc dự án, chạy script chấm điểm tự động:
```bash
python cham_diem.py
```
Script sẽ chạy qua tất cả các bài test, chấm điểm từng câu theo barem chính thức và xuất bảng điểm chi tiết ra màn hình.

### 2. Chạy toàn bộ Unit Tests với `unittest`
```bash
python -m unittest discover tests -v
```

### 3. Chạy từng file kiểm thử riêng biệt
```bash
# Kiểm thử Câu 1
python -m unittest tests/test_cau1.py -v

# Kiểm thử Câu 2
python -m unittest tests/test_cau2.py -v

# Kiểm thử Câu 3
python -m unittest tests/test_cau3.py -v

# Kiểm thử Câu 4
python -m unittest tests/test_cau4.py -v

# Kiểm thử Câu 5
python -m unittest tests/test_cau5.py -v
```
