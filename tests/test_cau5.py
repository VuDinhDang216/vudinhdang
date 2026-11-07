import unittest
import io
import sys

from src.cau5 import MonHoc, main


class TestCau5(unittest.TestCase):
    def test_khoi_tao_mon_hoc_csdl(self):
        """Khởi tạo đối tượng môn Cơ sở dữ liệu và kiểm tra thuộc tính."""
        mh = MonHoc(229008, "Cơ sở dữ liệu", 3, "Công nghệ thông tin")
        self.assertEqual(mh.MaMonHoc, 229008)
        self.assertEqual(mh.TenMonHoc, "Cơ sở dữ liệu")
        self.assertEqual(mh.SoTinChi, 3)
        self.assertEqual(mh.KhoaPhuTrach, "Công nghệ thông tin")

    def test_khoi_tao_mon_hoc_ta1(self):
        """Khởi tạo đối tượng môn Tiếng Anh 1 và kiểm tra thuộc tính."""
        mh = MonHoc(224604, "Tiếng Anh 1", 2, "Ngoại ngữ")
        self.assertEqual(mh.MaMonHoc, 224604)
        self.assertEqual(mh.TenMonHoc, "Tiếng Anh 1")
        self.assertEqual(mh.SoTinChi, 2)
        self.assertEqual(mh.KhoaPhuTrach, "Ngoại ngữ")

    def test_phuong_thuc_thongtinmonhoc(self):
        """Kiểm tra xuất thông tin từ phương thức thongtinmonhoc."""
        mh = MonHoc(229008, "Cơ sở dữ liệu", 3, "Công nghệ thông tin")
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            mh.thongtinmonhoc()
            out = captured.getvalue()
            self.assertIn("Mã môn học:  229008", out)
            self.assertIn("Tên môn học:  Cơ sở dữ liệu", out)
            self.assertIn("Số tín chỉ:  3", out)
            self.assertIn("Khoa phụ trách:  Công nghệ thông tin", out)
        finally:
            sys.stdout = old_stdout

    def test_main_cau5(self):
        """Kiểm tra thực thi hàm main hiển thị cả 2 môn học."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
            out = captured.getvalue()
            self.assertIn("229008", out)
            self.assertIn("Cơ sở dữ liệu", out)
            self.assertIn("224604", out)
            self.assertIn("Tiếng Anh 1", out)
        finally:
            sys.stdout = old_stdout


if __name__ == '__main__':
    unittest.main()
