import unittest
from unittest.mock import patch
import io
import sys

from src.cau4 import them_may_tinh, xoa_may_tinh, main


class TestCau4(unittest.TestCase):
    def test_them_may_tinh(self):
        """Thêm thông tin máy tính vào từ điển theo cấu trúc [BoNho, OCung, HangSanXuat, NamSanXuat]."""
        d = {}
        them_may_tinh(d, "PC01", 16, 512, "Dell", 2023)
        self.assertIn("PC01", d)
        self.assertEqual(d["PC01"], [16, 512, "Dell", 2023])

        # Thêm máy tính thứ 2
        them_may_tinh(d, "PC02", 32, 1024, "Asus", 2024)
        self.assertEqual(len(d), 2)
        self.assertEqual(d["PC02"], [32, 1024, "Asus", 2024])

    def test_xoa_may_tinh_thanh_cong(self):
        """Xóa máy tính tồn tại trong từ điển."""
        d = {"PC01": [16, 512, "Dell", 2023], "PC02": [8, 256, "HP", 2021]}
        res = xoa_may_tinh(d, "PC01")
        self.assertTrue(res)
        self.assertNotIn("PC01", d)
        self.assertEqual(len(d), 1)

    def test_xoa_may_tinh_khong_ton_tai(self):
        """Xóa máy tính không tồn tại trong từ điển."""
        d = {"PC01": [16, 512, "Dell", 2023]}
        res = xoa_may_tinh(d, "PC999")
        self.assertFalse(res)
        self.assertIn("PC01", d)
        self.assertEqual(len(d), 1)

    @patch('builtins.input', side_effect=['1', 'PC01', '16', '512', 'Dell', '2023', 'PC01'])
    def test_main_delete_success(self, mock_input):
        """Test luồng main khi nhập 1 máy tính và xóa thành công."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
            out = captured.getvalue()
            self.assertIn("Máy tính có số hiệu PC01 đã được xóa.", out)
        finally:
            sys.stdout = old_stdout

    @patch('builtins.input', side_effect=['1', 'PC01', '16', '512', 'Dell', '2023', 'PC99'])
    def test_main_delete_fail(self, mock_input):
        """Test luồng main khi tìm máy tính không tồn tại để xóa."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
            out = captured.getvalue()
            self.assertIn("Không có số hiệu máy tính cần xóa.", out)
        finally:
            sys.stdout = old_stdout


if __name__ == '__main__':
    unittest.main()
