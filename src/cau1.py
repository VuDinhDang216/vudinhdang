"""
Câu 1 (2.0 điểm):
a. Kiểm tra giá trị n nếu ngoài đoạn [1;99] thì yêu cầu nhập lại.
b. Viết hàm con tính tổng tất cả các ước số của n.
c. Viết hàm con tính S = 1 + 2^2 + 3^3 + ... + n^n
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def kiem_tra_n(n: int) -> bool:
    """Kiểm tra xem n có thuộc đoạn [1; 99] hay không."""
    return 1 <= n <= 99


def TongUocSo(n: int) -> int:
    """Tính tổng tất cả các ước số của n."""
    if n <= 0:
        return 0
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong


def S(n: int) -> int:
    """Tính S = 1 + 2^2 + 3^3 + ... + n^n"""
    if n <= 0:
        return 0
    s = 0
    for i in range(1, n + 1):
        s = s + (i ** i)
    return s


def nhap_n() -> int:
    """Nhập n và kiểm tra giá trị trong đoạn [1; 99]."""
    n = int(input("Nhập giá trị 1<=n<=99: "))
    while not kiem_tra_n(n):
        n = int(input("Nhập lại giá trị 1<=n<=99: "))
    return n


def main():
    n = nhap_n()
    print("Tổng các ước số là: ", TongUocSo(n))
    print("S = ", S(n))


if __name__ == "__main__":
    main()
