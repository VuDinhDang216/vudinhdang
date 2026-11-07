"""
Câu 3 (2.0 điểm):
Tạo một danh sách rỗng, viết chương trình xử lý danh sách với các chức năng sau:
a. Nhập các phần tử số nguyên vào danh sách, dừng khi người dùng nhập 0. In danh sách vừa nhập.
b. In ra màn hình các số dương chẵn có trong danh sách.
c. Đếm số lần xuất hiện của phần tử k có trong danh sách (với k nhập vào từ bàn phím).
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def loc_duong_chan(lst: list) -> list:
    """Lọc và trả về các số dương chẵn trong danh sách."""
    duong_chan = []
    for i in lst:
        if i > 0 and i % 2 == 0:
            duong_chan.append(i)
    return duong_chan


def dem_phan_tu(lst: list, k: int) -> int:
    """Đếm số lần xuất hiện của phần tử k trong danh sách."""
    return lst.count(k)


def nhap_danh_sach() -> list:
    """Nhập các phần tử số nguyên vào danh sách, dừng khi nhập 0."""
    ds = []
    while True:
        x = int(input("Nhập danh sách: "))
        if x == 0:
            break
        ds.append(x)
    return ds


def main():
    # a. Nhập danh sách dừng khi nhập 0
    ds = nhap_danh_sach()
    print("Danh sách vừa nhập:", ds)

    # b. In các số dương chẵn
    duong_chan = loc_duong_chan(ds)
    if duong_chan:
        print("Các số dương chẵn có trong danh sách:", duong_chan)
    else:
        print("Không có số dương chẵn trong danh sách.")

    # c. Đếm số lần xuất hiện của k
    k = int(input("Nhap k:"))
    dem = dem_phan_tu(ds, k)
    if dem == 0:
        print(f"{k} không có trong danh sách")
    else:
        print(f"{k} xuất hiện {dem} lần")


if __name__ == "__main__":
    main()
