"""
Câu 5 (2.0 điểm):
Tạo lớp có tên MonHoc với các yêu cầu sau:
a. Lớp MonHoc có các thuộc tính và phương thức:
- Thuộc tính: MaMonHoc, TenMonHoc, SoTinChi, KhoaPhuTrach.
- Phương thức:
    o Khởi tạo __init__(): khởi tạo thông tin cho MaMonHoc, TenMonHoc, SoTinChi, KhoaPhuTrach.
    o thongtinmonhoc(): dùng để hiển thị thông tin của MaMonHoc, TenMonHoc, SoTinChi, KhoaPhuTrach.
b. Tạo 2 đối tượng (229008, "Cơ sở dữ liệu", 3, "Công nghệ thông tin") và (224604, "Tiếng Anh 1", 2, "Ngoại ngữ")
   và thực thi phương thức thongtinmonhoc(). In kết quả ra màn hình.
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MonHoc:
    def __init__(self, MaMonHoc, TenMonHoc, SoTinChi, KhoaPhuTrach):
        self.MaMonHoc = MaMonHoc
        self.TenMonHoc = TenMonHoc
        self.SoTinChi = SoTinChi
        self.KhoaPhuTrach = KhoaPhuTrach

    def thongtinmonhoc(self):
        print(f"Mã môn học: ", self.MaMonHoc)
        print(f"Tên môn học: ", self.TenMonHoc)
        print(f"Số tín chỉ: ", self.SoTinChi)
        print(f"Khoa phụ trách: ", self.KhoaPhuTrach)


def main():
    CSDL = MonHoc(229008, "Cơ sở dữ liệu", 3, "Công nghệ thông tin")
    TA1 = MonHoc(224604, "Tiếng Anh 1", 2, "Ngoại ngữ")
    
    print("=== Thông tin môn học 1 ===")
    CSDL.thongtinmonhoc()
    
    print("\n=== Thông tin môn học 2 ===")
    TA1.thongtinmonhoc()


if __name__ == "__main__":
    main()
