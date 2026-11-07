import unittest
from unittest.mock import patch
import io
import sys

from src.cau3 import loc_duong_chan, dem_phan_tu, nhap_danh_sach, main


class TestCau3(unittest.TestCase):
    def test_loc_duong_chan_mixed(self):
        """Lọc các số dương chẵn trong danh sách hỗn hợp."""
        data = [-4, -2, 0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(loc_duong_chan(data), [2, 4, 6])

    def test_loc_duong_chan_none(self):
        """Khi danh sách không có số dương chẵn nào."""
        data = [-1, -3, -4, 0, 1, 3, 5]
        self.assertEqual(loc_duong_chan(data), [])
        self.assertEqual(loc_duong_chan([]), [])

    def test_dem_phan_tu(self):
        """Đếm số lần xuất hiện của phần tử k."""
        data = [1, 2, 3, 2, 4, 2, 5]
        self.assertEqual(dem_phan_tu(data, 2), 3)
        self.assertEqual(dem_phan_tu(data, 1), 1)
        self.assertEqual(dem_phan_tu(data, 99), 0)
        self.assertEqual(dem_phan_tu([], 5), 0)

    @patch('builtins.input', side_effect=['10', '15', '-4', '0'])
    def test_nhap_danh_sach(self, mock_input):
        """Nhập số nguyên dừng khi nhập 0."""
        result = nhap_danh_sach()
        self.assertEqual(result, [10, 15, -4])

    @patch('builtins.input', side_effect=['2', '4', '7', '0', '4'])
    def test_main_has_even_and_found_k(self, mock_input):
        """Test luồng main khi có số dương chẵn và k tìm thấy."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
            out = captured.getvalue()
            self.assertIn("Danh sách vừa nhập: [2, 4, 7]", out)
            self.assertIn("Các số dương chẵn có trong danh sách: [2, 4]", out)
            self.assertIn("4 xuất hiện 1 lần", out)
        finally:
            sys.stdout = old_stdout

    @patch('builtins.input', side_effect=['1', '3', '-2', '0', '5'])
    def test_main_no_even_and_not_found_k(self, mock_input):
        """Test luồng main khi không có số dương chẵn và k không có."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
            out = captured.getvalue()
            self.assertIn("Không có số dương chẵn trong danh sách.", out)
            self.assertIn("5 không có trong danh sách", out)
        finally:
            sys.stdout = old_stdout


if __name__ == '__main__':
    unittest.main()
