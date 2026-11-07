import unittest
from unittest.mock import patch
import io
import sys

from src.cau1 import kiem_tra_n, TongUocSo, S, nhap_n, main


class TestCau1(unittest.TestCase):
    def test_kiem_tra_n_valid(self):
        """Kiểm tra các giá trị hợp lệ trong đoạn [1, 99]."""
        self.assertTrue(kiem_tra_n(1))
        self.assertTrue(kiem_tra_n(50))
        self.assertTrue(kiem_tra_n(99))

    def test_kiem_tra_n_invalid(self):
        """Kiểm tra các giá trị ngoài đoạn [1, 99]."""
        self.assertFalse(kiem_tra_n(0))
        self.assertFalse(kiem_tra_n(-10))
        self.assertFalse(kiem_tra_n(100))
        self.assertFalse(kiem_tra_n(999))

    def test_tong_uoc_so_standard(self):
        """Kiểm tra tổng ước số: ví dụ n=12 có tổng ước 1+2+3+4+6+12=28."""
        self.assertEqual(TongUocSo(12), 28)
        self.assertEqual(TongUocSo(1), 1)
        self.assertEqual(TongUocSo(6), 12)  # 1 + 2 + 3 + 6 = 12
        self.assertEqual(TongUocSo(28), 56) # 1 + 2 + 4 + 7 + 14 + 28 = 56

    def test_tong_uoc_so_prime(self):
        """Số nguyên tố chỉ có 2 ước là 1 và chính nó."""
        self.assertEqual(TongUocSo(7), 8)   # 1 + 7
        self.assertEqual(TongUocSo(13), 14) # 1 + 13

    def test_tong_uoc_so_edge_cases(self):
        """Các trường hợp số <= 0."""
        self.assertEqual(TongUocSo(0), 0)
        self.assertEqual(TongUocSo(-5), 0)

    def test_tinh_s(self):
        """Kiểm tra tính S = 1 + 2^2 + ... + n^n."""
        self.assertEqual(S(1), 1)                      # 1^1 = 1
        self.assertEqual(S(2), 1 + 4)                  # 5
        self.assertEqual(S(3), 1 + 4 + 27)             # 32
        self.assertEqual(S(4), 1 + 4 + 27 + 256)        # 288
        self.assertEqual(S(0), 0)
        self.assertEqual(S(-2), 0)

    @patch('builtins.input', side_effect=['12'])
    def test_nhap_n_single_try(self, mock_input):
        """Nhập đúng ngay lần đầu."""
        self.assertEqual(nhap_n(), 12)

    @patch('builtins.input', side_effect=['0', '150', '25'])
    def test_nhap_n_retry(self, mock_input):
        """Nhập sai ngoài [1; 99] phải yêu cầu nhập lại đến khi hợp lệ."""
        self.assertEqual(nhap_n(), 25)
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['12'])
    def test_main_cau1(self, mock_input):
        """Chạy hàm main và kiểm tra nội dung output."""
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        try:
            sys.stdout = captured_output
            main()
            output = captured_output.getvalue()
            self.assertIn("Tổng các ước số là:  28", output)
            self.assertIn("S =", output)
        finally:
            sys.stdout = sys_stdout_backup


if __name__ == '__main__':
    unittest.main()
