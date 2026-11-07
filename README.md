# 🐍 LẬP TRÌNH PYTHON - BÀI THI KẾT THÚC MÔN HỌC

<p align="center">
  <a href="https://github.com/VuDinhDang216/vudinhdang/actions/workflows/python-tests.yml">
    <img src="https://github.com/VuDinhDang216/vudinhdang/actions/workflows/python-tests.yml/badge.svg" alt="Python Tests Status">
  </a>
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=flat&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Tests-30%20Passed-success?style=flat&logo=checkmarx" alt="Unit Tests Passed">
  <img src="https://img.shields.io/badge/Author-VuDinhDang216-orange?style=flat&logo=github" alt="Author">
</p>

---

## 📌 Thông Tin Học Phần & Đề Thi

- **Trường**: Trường Cao đẳng Công Thương TP.HCM (HITC)
- **Khoa**: Công nghệ Thông tin
- **Bộ môn**: Công nghệ Phần mềm
- **Môn học**: Lập trình Python (Mã môn học: `229152` - Số ĐVHT/Tín chỉ: `02`)
- **Mã đề thi**: `11301`
- **Hình thức**: Thực hành (Thời gian làm bài: 90 phút)
- **Tác giả**: [Vũ Đình Đăng (VuDinhDang216)](https://github.com/VuDinhDang216)
- **Repository**: [https://github.com/VuDinhDang216/vudinhdang.git](https://github.com/VuDinhDang216/vudinhdang.git)

---

## 📁 Cấu Trúc Dự Án

Dự án được cấu trúc theo chuẩn mã nguồn mở hiện đại, tách biệt giữa mã nguồn (`src/`), bộ kiểm thử tự động (`tests/`), và tích hợp Continuous Integration (`.github/`):

```text
vudinhdang/
├── .github/
│   └── workflows/
│       └── python-tests.yml       # GitHub Actions CI tự động kiểm thử
├── src/
│   ├── __init__.py                # Package init
│   ├── cau1.py                    # Câu 1: Ước số, lũy thừa S(n), kiểm tra 1 <= n <= 99
│   ├── cau2.py                    # Câu 2: Đếm chữ thường, kiểm tra đối xứng, viết hoa chữ cái đầu
│   ├── cau3.py                    # Câu 3: Xử lý danh sách, lọc dương chẵn, đếm phần tử k
│   ├── cau4.py                    # Câu 4: Quản lý từ điển máy tính, xóa theo số hiệu
│   └── cau5.py                    # Câu 5: Lớp MonHoc và in thông tin môn học
├── tests/
│   ├── README.md                  # Hướng dẫn chi tiết & bảng phân bổ điểm
│   ├── __init__.py
│   ├── test_cau1.py               # 9 test cases cho Câu 1
│   ├── test_cau2.py               # 6 test cases cho Câu 2
│   ├── test_cau3.py               # 6 test cases cho Câu 3
│   ├── test_cau4.py               # 5 test cases cho Câu 4
│   └── test_cau5.py               # 4 test cases cho Câu 5
├── cham_diem.py                   # Script tự động chấm điểm theo barem 10 điểm
├── cau1.py                        # Root wrapper chạy trực tiếp Câu 1
├── cau2.py                        # Root wrapper chạy trực tiếp Câu 2
├── cau3.py                        # Root wrapper chạy trực tiếp Câu 3
├── cau4.py                        # Root wrapper chạy trực tiếp Câu 4
├── cau5.py                        # Root wrapper chạy trực tiếp Câu 5
├── requirements.txt               # Các phụ thuộc bổ sung (tùy chọn)
├── .gitignore                     # Bỏ qua các tệp không cần thiết
└── README.md                      # Tài liệu dự án
```

---

## 📝 Tóm Tắt Đề Bài & Giải Pháp Thực Hiện

### 🔹 Câu 1 (2.0 điểm) - Số học & Vòng lặp
1. **Kiểm tra giá trị $n$**: Nhập vào số nguyên dương $n$, nếu nằm ngoài đoạn $[1; 99]$ yêu cầu người dùng nhập lại.
2. **Hàm `TongUocSo(n)`**: Tính tổng tất cả các ước số nguyên dương của $n$.
   - *Ví dụ*: $n = 12 \rightarrow 1 + 2 + 3 + 4 + 6 + 12 = 28$.
3. **Hàm `S(n)`**: Tính $S = 1 + 2^2 + 3^3 + \dots + n^n$.

### 🔹 Câu 2 (2.0 điểm) - Xử lý chuỗi ký tự
1. **Đếm ký tự thường**: Đếm số lượng ký tự chữ thường (`islower()`) có trong chuỗi $s$.
2. **Kiểm tra đối xứng**: Hàm `DoiXung(s)` kiểm tra chuỗi có đối xứng hay không ($s == s[::-1]$).
3. **Đổi chữ hoa đầu từ**: Chuyển tất cả các ký tự đầu tiên của mỗi từ thành chữ hoa (`s.title()`).

### 🔹 Câu 3 (2.0 điểm) - Thao tác Danh sách (List)
1. **Nhập danh sách**: Tạo danh sách rỗng, nhập các phần tử số nguyên liên tục cho đến khi người dùng nhập `0`. In danh sách vừa nhập.
2. **Lọc số dương chẵn**: In ra các số vừa lớn hơn 0 vừa chia hết cho 2 (`i > 0 and i % 2 == 0`).
3. **Đếm tần suất**: Nhập số nguyên $k$, đếm số lần $k$ xuất hiện trong danh sách (`lst.count(k)`).

### 🔹 Câu 4 (2.0 điểm) - Quản lý Từ điển (Dictionary)
1. **Nhập thông tin máy tính**: Nhập thông tin gồm `Số hiệu`, `Dung lượng bộ nhớ`, `Dung lượng ổ cứng`, `Hãng sản xuất`, `Năm sản xuất`. Lưu vào từ điển theo cấu trúc:
   ```python
   dict[SoHieu] = [BoNho, OCung, HangSanXuat, NamSanXuat]
   ```
2. **Xóa máy tính**: Nhập số hiệu máy tính cần tìm. Nếu tồn tại thì xóa khỏi từ điển và thông báo thành công, ngược lại thông báo không có số hiệu cần xóa.

### 🔹 Câu 5 (2.0 điểm) - Lập trình hướng đối tượng (OOP)
1. **Lớp `MonHoc`**:
   - **Thuộc tính**: `MaMonHoc`, `TenMonHoc`, `SoTinChi`, `KhoaPhuTrach`.
   - **Phương thức**:
     - `__init__()`: Khởi tạo giá trị cho 4 thuộc tính trên.
     - `thongtinmonhoc()`: In thông tin chi tiết của môn học ra màn hình.
2. **Tạo đối tượng thực thi**:
   - `CSDL = MonHoc(229008, "Cơ sở dữ liệu", 3, "Công nghệ thông tin")`
   - `TA1 = MonHoc(224604, "Tiếng Anh 1", 2, "Ngoại ngữ")`
   - Gọi `thongtinmonhoc()` cho cả 2 đối tượng.

---

## 🚀 Hướng Dẫn Sử Dụng

### 1. Yêu cầu môi trường
- Python 3.10 trở lên.
- Không bắt buộc cài thêm thư viện ngoài (sử dụng thư viện chuẩn của Python).

### 2. Chạy thử các bài làm
Bạn có thể chạy trực tiếp từng câu từ thư mục gốc hoặc thư mục `src/`:

```bash
# Chạy Câu 1
python cau1.py

# Chạy Câu 2
python cau2.py

# Chạy Câu 3
python cau3.py

# Chạy Câu 4
python cau4.py

# Chạy Câu 5
python cau5.py
```

---

## 🎯 Chấm Điểm Tự Động (Grading System)

Dự án cung cấp công cụ chấm điểm tự động **[`cham_diem.py`](file:///d:/de1/cham_diem.py)** trực tiếp ở thư mục gốc, bám sát 100% barem điểm đề thi kết thúc môn học (thang điểm 10.0):

```bash
python cham_diem.py
```

### 📊 Bảng Điểm Thực Tế Khi Chạy:
```text
================================================================================
      HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG BÀI THI LẬP TRÌNH PYTHON (MÃ ĐỀ: 11301)
                 Trường Cao đẳng Công Thương TP.HCM
================================================================================

--- CÂU 1 (Tối đa 2.0 điểm) ---
  [✓ PASS] Ý a: Kiểm tra giá trị n nếu ngoài đoạn [1;99] thì yêu cầu nhập lại
         Điểm: 0.50 / 0.50 đ (4/4 test cases đạt)
  [✓ PASS] Ý b: Viết hàm con TongUocSo(n) tính tổng tất cả các ước số của n
         Điểm: 0.75 / 0.75 đ (3/3 test cases đạt)
  [✓ PASS] Ý c: Viết hàm con tính S = 1 + 2² + 3³ + ... + nⁿ
         Điểm: 0.75 / 0.75 đ (2/2 test cases đạt)

--- CÂU 2 (Tối đa 2.0 điểm) ---
  [✓ PASS] Ý a: Đếm số ký tự chữ thường có trong chuỗi s
         Điểm: 1.00 / 1.00 đ (2/2 test cases đạt)
  [✓ PASS] Ý b: Kiểm tra xem chuỗi s có đối xứng hay không (DoiXung)
         Điểm: 0.50 / 0.50 đ (3/3 test cases đạt)
  [✓ PASS] Ý c: Đổi tất cả các ký tự đầu tiên của mỗi từ thành chữ hoa
         Điểm: 0.50 / 0.50 đ (1/1 test cases đạt)

--- CÂU 3 (Tối đa 2.0 điểm) ---
  [✓ PASS] Ý a: Nhập các phần tử số nguyên vào danh sách, dừng khi nhập 0
         Điểm: 0.75 / 0.75 đ (1/1 test cases đạt)
  [✓ PASS] Ý b: In ra màn hình các số dương chẵn có trong danh sách
         Điểm: 0.75 / 0.75 đ (2/2 test cases đạt)
  [✓ PASS] Ý c: Đếm số lần xuất hiện của phần tử k có trong danh sách
         Điểm: 0.50 / 0.50 đ (3/3 test cases đạt)

--- CÂU 4 (Tối đa 2.0 điểm) ---
  [✓ PASS] Ý a: Nhập thông tin máy tính lưu vào từ điển theo cấu trúc danh sách
         Điểm: 1.50 / 1.50 đ (2/2 test cases đạt)
  [✓ PASS] Ý b: Nhập số hiệu máy tính, xóa nếu có hoặc thông báo không tìm thấy
         Điểm: 0.50 / 0.50 đ (3/3 test cases đạt)

--- CÂU 5 (Tối đa 2.0 điểm) ---
  [✓ PASS] Ý a: Lớp MonHoc: khởi tạo thuộc tính và phương thức thongtinmonhoc()
         Điểm: 1.00 / 1.00 đ (2/2 test cases đạt)
  [✓ PASS] Ý b: Tạo 2 đối tượng mẫu (CSDL và Tiếng Anh 1) và thực thi thongtinmonhoc()
         Điểm: 1.00 / 1.00 đ (2/2 test cases đạt)

================================================================================
                             BẢNG TỔNG KẾT ĐIỂM
================================================================================
  - Tổng số test cases thực thi : 30
  - Số test cases vượt qua (PASS): 30
  - Số test cases thất bại (FAIL): 0
  - TỔNG ĐIỂM BÀI THI           : 10.00 / 10.00 ĐIỂM
  - ĐÁNH GIÁ XẾP LOẠI           : XUẤT SẮC (ĐẠT ĐIỂM TỐI ĐA)
================================================================================
```

---

## 🧪 Kiểm Thử Tự Động (Unit Testing)

Chi tiết về tài liệu kiểm thử xem tại **[`tests/README.md`](file:///d:/de1/tests/README.md)**.
Dự án đi kèm bộ test toàn diện gồm **30 test cases** kiểm tra toàn bộ các hàm xử lý logic, biên điều kiện, ngoại lệ và tương tác dòng lệnh (CLI mock).

### Chạy toàn bộ kiểm thử:
```bash
python -m unittest discover tests -v
```

### Kết quả chạy kiểm thử mẫu:
```text
test_kiem_tra_n_invalid (test_cau1.TestCau1) ... ok
test_kiem_tra_n_valid (test_cau1.TestCau1) ... ok
test_main_cau1 (test_cau1.TestCau1) ... ok
test_nhap_n_retry (test_cau1.TestCau1) ... ok
test_nhap_n_single_try (test_cau1.TestCau1) ... ok
test_tinh_s (test_cau1.TestCau1) ... ok
test_tong_uoc_so_edge_cases (test_cau1.TestCau1) ... ok
test_tong_uoc_so_prime (test_cau1.TestCau1) ... ok
test_tong_uoc_so_standard (test_cau1.TestCau1) ... ok
test_dem_chu_thuong (test_cau2.TestCau2) ... ok
test_doi_xung (test_cau2.TestCau2) ... ok
test_main_no_lowercase (test_cau2.TestCau2) ... ok
test_main_non_palindrome (test_cau2.TestCau2) ... ok
test_main_palindrome_with_lowercase (test_cau2.TestCau2) ... ok
test_viet_hoa_dau_tu (test_cau2.TestCau2) ... ok
test_dem_phan_tu (test_cau3.TestCau3) ... ok
test_loc_duong_chan_mixed (test_cau3.TestCau3) ... ok
test_loc_duong_chan_none (test_cau3.TestCau3) ... ok
test_main_has_even_and_found_k (test_cau3.TestCau3) ... ok
test_main_no_even_and_not_found_k (test_cau3.TestCau3) ... ok
test_nhap_danh_sach (test_cau3.TestCau3) ... ok
test_main_delete_fail (test_cau4.TestCau4) ... ok
test_main_delete_success (test_cau4.TestCau4) ... ok
test_them_may_tinh (test_cau4.TestCau4) ... ok
test_xoa_may_tinh_khong_ton_tai (test_cau4.TestCau4) ... ok
test_xoa_may_tinh_thanh_cong (test_cau4.TestCau4) ... ok
test_khoi_tao_mon_hoc_csdl (test_cau5.TestCau5) ... ok
test_khoi_tao_mon_hoc_ta1 (test_cau5.TestCau5) ... ok
test_main_cau5 (test_cau5.TestCau5) ... ok
test_phuong_thuc_thongtinmonhoc (test_cau5.TestCau5) ... ok

----------------------------------------------------------------------
Ran 30 tests in 0.003s

OK
```

---

## ⚙️ Tích Hợp GitHub Actions (CI)

Tệp workflow `.github/workflows/python-tests.yml` sẽ tự động kích hoạt kiểm thử trên GitHub Actions mỗi khi có commit mới được `push` hoặc tạo `pull_request` lên nhánh chính (`main`), kiểm tra tương thích trên nhiều phiên bản Python (`3.10`, `3.11`, `3.12`).

---

## 👤 Tác Giả

- Họ & Tên: **Vũ Đình Đăng**
- GitHub: [@VuDinhDang216](https://github.com/VuDinhDang216)
- Repository: [VuDinhDang216/vudinhdang](https://github.com/VuDinhDang216/vudinhdang)