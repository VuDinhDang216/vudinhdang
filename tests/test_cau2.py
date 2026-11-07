import unittest
from unittest.mock import patch
import io
import sys

from src.cau2 import dem_chu_thuong, DoiXung, viet_hoa_dau_tu, main


class TestCau2(unittest.TestCase):
    def test_dem_chu_thuong(self):
        """Kiểm tra đếm ký tự chữ thường."""
        self.assertEqual(dem_chu_thuong("python"), 6)
        self.assertEqual(dem_chu_thuong("PYTHON"), 0)
        self.assertEqual(dem_chu_thuong("Python 3.10!"), 5) # y, t, h, o, n
        self.assertEqual(dem_chu_thuong(""), 0)
        self.assertEqual(dem_chu_thuong("123456@#$"), 0)

    def test_doi_xung(self):
        """Kiểm tra tính đối xứng của chuỗi."""
        self.assertTrue(DoiXung("radar"))
        self.assertTrue(DoiXung("madam"))
        self.assertTrue(DoiXung("12321"))
        self.assertTrue(DoiXung("a"))
        self.assertTrue(DoiXung(""))
        
        self.assertFalse(DoiXung("python"))
        self.assertFalse(DoiXung("hello"))
        self.assertFalse(DoiXung("Radar")) # Phân biệt hoa thường

    def test_viet_hoa_dau_tu(self):
        """Kiểm tra chuyển ký tự đầu mỗi từ thành chữ hoa."""
        self.assertEqual(viet_hoa_dau_tu("lap trinh python"), "Lap Trinh Python")
        self.assertEqual(viet_hoa_dau_tu("hello world"), "Hello World")
        self.assertEqual(viet_hoa_dau_tu("PYTHON"), "Python")
        self.assertEqual(viet_hoa_dau_tu(""), "")

    @patch('builtins.input', side_effect=['madam'])
    def test_main_palindrome_with_lowercase(self, mock_input):
        """Test main với chuỗi đối xứng và có ký tự thường."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
            out = captured.getvalue()
            self.assertIn("Số ký tự chữ thường trong chuỗi:  5", out)
            self.assertIn("Chuỗi đối xứng.", out)
            self.assertIn("Madam", out)
        finally:
            sys.stdout = old_stdout

    @patch('builtins.input', side_effect=['12321'])
    def test_main_no_lowercase(self, mock_input):
        """Test main khi không có ký tự thường nào."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
            out = captured.getvalue()
            self.assertIn("Chuỗi không có ký tự chữ thường.", out)
            self.assertIn("Chuỗi đối xứng.", out)
        finally:
            sys.stdout = old_stdout

    @patch('builtins.input', side_effect=['Python'])
    def test_main_non_palindrome(self, mock_input):
        """Test main khi chuỗi không đối xứng."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
            out = captured.getvalue()
            self.assertIn("Chuỗi không đối xứng.", out)
        finally:
            sys.stdout = old_stdout


if __name__ == '__main__':
    unittest.main()
