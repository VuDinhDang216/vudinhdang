"""
HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG BÀI THI LẬP TRÌNH PYTHON
Trường Cao đẳng Công Thương TP.HCM
Mã môn học: 229152 - Mã đề thi: 11301
"""
import io
import sys
import unittest

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Import các lớp kiểm thử
from tests.test_cau1 import TestCau1
from tests.test_cau2 import TestCau2
from tests.test_cau3 import TestCau3
from tests.test_cau4 import TestCau4
from tests.test_cau5 import TestCau5

# Định nghĩa barem chấm điểm chi tiết theo đáp án chính thức
BAREM_DIEM = [
    {
        "cau": "Câu 1",
        "y": "a",
        "noi_dung": "Kiểm tra giá trị n nếu ngoài đoạn [1;99] thì yêu cầu nhập lại",
        "diem_toi_da": 0.5,
        "test_class": TestCau1,
        "test_methods": ["test_kiem_tra_n_valid", "test_kiem_tra_n_invalid", "test_nhap_n_single_try", "test_nhap_n_retry"],
    },
    {
        "cau": "Câu 1",
        "y": "b",
        "noi_dung": "Viết hàm con TongUocSo(n) tính tổng tất cả các ước số của n",
        "diem_toi_da": 0.75,
        "test_class": TestCau1,
        "test_methods": ["test_tong_uoc_so_standard", "test_tong_uoc_so_prime", "test_tong_uoc_so_edge_cases"],
    },
    {
        "cau": "Câu 1",
        "y": "c",
        "noi_dung": "Viết hàm con tính S = 1 + 2² + 3³ + ... + nⁿ",
        "diem_toi_da": 0.75,
        "test_class": TestCau1,
        "test_methods": ["test_tinh_s", "test_main_cau1"],
    },
    {
        "cau": "Câu 2",
        "y": "a",
        "noi_dung": "Đếm số ký tự chữ thường có trong chuỗi s",
        "diem_toi_da": 1.0,
        "test_class": TestCau2,
        "test_methods": ["test_dem_chu_thuong", "test_main_no_lowercase"],
    },
    {
        "cau": "Câu 2",
        "y": "b",
        "noi_dung": "Kiểm tra xem chuỗi s có đối xứng hay không (DoiXung)",
        "diem_toi_da": 0.5,
        "test_class": TestCau2,
        "test_methods": ["test_doi_xung", "test_main_palindrome_with_lowercase", "test_main_non_palindrome"],
    },
    {
        "cau": "Câu 2",
        "y": "c",
        "noi_dung": "Đổi tất cả các ký tự đầu tiên của mỗi từ thành chữ hoa",
        "diem_toi_da": 0.5,
        "test_class": TestCau2,
        "test_methods": ["test_viet_hoa_dau_tu"],
    },
    {
        "cau": "Câu 3",
        "y": "a",
        "noi_dung": "Nhập các phần tử số nguyên vào danh sách, dừng khi nhập 0",
        "diem_toi_da": 0.75,
        "test_class": TestCau3,
        "test_methods": ["test_nhap_danh_sach"],
    },
    {
        "cau": "Câu 3",
        "y": "b",
        "noi_dung": "In ra màn hình các số dương chẵn có trong danh sách",
        "diem_toi_da": 0.75,
        "test_class": TestCau3,
        "test_methods": ["test_loc_duong_chan_mixed", "test_loc_duong_chan_none"],
    },
    {
        "cau": "Câu 3",
        "y": "c",
        "noi_dung": "Đếm số lần xuất hiện của phần tử k có trong danh sách",
        "diem_toi_da": 0.5,
        "test_class": TestCau3,
        "test_methods": ["test_dem_phan_tu", "test_main_has_even_and_found_k", "test_main_no_even_and_not_found_k"],
    },
    {
        "cau": "Câu 4",
        "y": "a",
        "noi_dung": "Nhập thông tin máy tính lưu vào từ điển theo cấu trúc danh sách",
        "diem_toi_da": 1.5,
        "test_class": TestCau4,
        "test_methods": ["test_them_may_tinh", "test_main_delete_success"],
    },
    {
        "cau": "Câu 4",
        "y": "b",
        "noi_dung": "Nhập số hiệu máy tính, xóa nếu có hoặc thông báo không tìm thấy",
        "diem_toi_da": 0.5,
        "test_class": TestCau4,
        "test_methods": ["test_xoa_may_tinh_thanh_cong", "test_xoa_may_tinh_khong_ton_tai", "test_main_delete_fail"],
    },
    {
        "cau": "Câu 5",
        "y": "a",
        "noi_dung": "Lớp MonHoc: khởi tạo thuộc tính và phương thức thongtinmonhoc()",
        "diem_toi_da": 1.0,
        "test_class": TestCau5,
        "test_methods": ["test_khoi_tao_mon_hoc_csdl", "test_phuong_thuc_thongtinmonhoc"],
    },
    {
        "cau": "Câu 5",
        "y": "b",
        "noi_dung": "Tạo 2 đối tượng mẫu (CSDL và Tiếng Anh 1) và thực thi thongtinmonhoc()",
        "diem_toi_da": 1.0,
        "test_class": TestCau5,
        "test_methods": ["test_khoi_tao_mon_hoc_ta1", "test_main_cau5"],
    },
]


def cham_diem():
    print("=" * 80)
    print("      HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG BÀI THI LẬP TRÌNH PYTHON (MÃ ĐỀ: 11301)")
    print("                 Trường Cao đẳng Công Thương TP.HCM")
    print("=" * 80)

    tong_diem_dat_duoc = 0.0
    tong_diem_toi_da = 0.0
    tong_so_test = 0
    tong_test_pass = 0

    cau_hien_tai = None

    for muc in BAREM_DIEM:
        if muc["cau"] != cau_hien_tai:
            cau_hien_tai = muc["cau"]
            print(f"\n--- {cau_hien_tai.upper()} (Tối đa 2.0 điểm) ---")

        suite = unittest.TestSuite()
        for method in muc["test_methods"]:
            suite.addTest(muc["test_class"](method))

        runner = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0)
        result = runner.run(suite)

        so_test_muc = len(muc["test_methods"])
        so_loi = len(result.errors) + len(result.failures)
        so_pass = so_test_muc - so_loi

        tong_so_test += so_test_muc
        tong_test_pass += so_pass

        # Tính điểm theo tỷ lệ test pass trong ý đó
        diem_dat = round(muc["diem_toi_da"] * (so_pass / so_test_muc), 2)
        tong_diem_dat_duoc += diem_dat
        tong_diem_toi_da += muc["diem_toi_da"]

        trang_thai = "[✓ PASS]" if so_loi == 0 else "[✗ FAIL]"
        print(f"  {trang_thai} Ý {muc['y']}: {muc['noi_dung']}")
        print(f"         Điểm: {diem_dat:.2f} / {muc['diem_toi_da']:.2f} đ ({so_pass}/{so_test_muc} test cases đạt)")

    print("\n" + "=" * 80)
    print("                             BẢNG TỔNG KẾT ĐIỂM")
    print("=" * 80)
    print(f"  - Tổng số test cases thực thi : {tong_so_test}")
    print(f"  - Số test cases vượt qua (PASS): {tong_test_pass}")
    print(f"  - Số test cases thất bại (FAIL): {tong_so_test - tong_test_pass}")
    print(f"  - TỔNG ĐIỂM BÀI THI           : {tong_diem_dat_duoc:.2f} / {tong_diem_toi_da:.2f} ĐIỂM")

    # Đánh giá xếp loại
    if tong_diem_dat_duoc >= 9.0:
        xep_loai = "XUẤT SẮC (ĐẠT ĐIỂM TỐI ĐA)"
    elif tong_diem_dat_duoc >= 8.0:
        xep_loai = "GIỎI"
    elif tong_diem_dat_duoc >= 6.5:
        xep_loai = "KHÁ"
    elif tong_diem_dat_duoc >= 5.0:
        xep_loai = "TRUNG BÌNH"
    else:
        xep_loai = "CHƯA ĐẠT"

    print(f"  - ĐÁNH GIÁ XẾP LOẠI           : {xep_loai}")
    print("=" * 80)

    return 0 if (tong_so_test - tong_test_pass) == 0 else 1


if __name__ == "__main__":
    sys.exit(cham_diem())
