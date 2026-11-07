"""
Câu 4 (2.0 điểm):
Viết chương trình nhập thông tin của một chiếc máy tính và thực hiện các công việc sau:
a. Nhập thông tin gồm: Số hiệu máy tính, dung lượng bộ nhớ, dung lượng ổ cứng, hãng sản xuất, năm sản xuất. Lưu các thông tin này trong một từ điển.
b. Nhập số hiệu máy tính, nếu tồn tại máy tính có số hiệu cần tìm thì xóa máy tính này khỏi từ điển, ngược lại thông báo không có máy tính cần tìm.
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def them_may_tinh(danh_sach: dict, so_hieu: str, bo_nho: int, o_cung: int, hang_sx: str, nam_sx: int) -> dict:
    """Thêm một máy tính vào từ điển theo cấu trúc: [BoNho, OCung, HangSanXuat, NamSanXuat]."""
    danh_sach[str(so_hieu)] = [bo_nho, o_cung, hang_sx, nam_sx]
    return danh_sach


def xoa_may_tinh(danh_sach: dict, so_hieu: str) -> bool:
    """Xóa máy tính có số hiệu chỉ định khỏi từ điển. Trả về True nếu xóa thành công, False nếu không tìm thấy."""
    so_hieu_str = str(so_hieu)
    if so_hieu_str in danh_sach:
        del danh_sach[so_hieu_str]
        return True
    return False


def main():
    dict_may_tinh = {}
    try:
        n = int(input("Nhập số lượng máy tính:"))
    except ValueError:
        n = 0

    for i in range(n):
        print(f"\n--- Nhập thông tin máy tính thứ {i + 1} ---")
        so_hieu = input("Nhập số hiệu máy tính:")
        bo_nho = int(input("Nhập dung lượng bộ nhớ:"))
        o_cung = int(input("Nhập dung lượng ổ cứng:"))
        hang_sx = input("Nhập hãng sản xuất:")
        nam_sx = int(input("Nhập năm sản xuất:"))
        them_may_tinh(dict_may_tinh, so_hieu, bo_nho, o_cung, hang_sx, nam_sx)

    print("\nTừ điển máy tính hiện tại:")
    print(dict_may_tinh)

    # b. Nhập số hiệu và xóa nếu tồn tại
    x = input("\nNhập số hiệu máy tính cần tìm:")
    if xoa_may_tinh(dict_may_tinh, x):
        print(f"Máy tính có số hiệu {x} đã được xóa.")
    else:
        print("Không có số hiệu máy tính cần xóa.")

    print(dict_may_tinh)


if __name__ == "__main__":
    main()
