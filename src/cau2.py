"""
Câu 2 (2.0 điểm):
a. Đếm số ký tự chữ thường có trong chuỗi s.
b. Kiểm tra xem chuỗi s có đối xứng hay không?
c. Đổi tất cả các ký tự đầu tiên của mỗi từ thành chữ hoa.
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def dem_chu_thuong(s: str) -> int:
    """Đếm số ký tự chữ thường có trong chuỗi s."""
    dem = 0
    for i in s:
        if i.islower():
            dem += 1
    return dem


def DoiXung(s: str) -> bool:
    """Kiểm tra xem chuỗi s có đối xứng hay không."""
    return s == s[::-1]


def viet_hoa_dau_tu(s: str) -> str:
    """Đổi tất cả các ký tự đầu tiên của mỗi từ thành chữ hoa."""
    return s.title()


def main():
    s = input("Nhập chuỗi s: ")
    
    # a. Đếm ký tự thường
    dem = dem_chu_thuong(s)
    if dem == 0:
        print("Chuỗi không có ký tự chữ thường.")
    else:
        print("Số ký tự chữ thường trong chuỗi: ", dem)
    
    # b. Kiểm tra đối xứng
    if DoiXung(s):
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")
        
    # c. Viết hoa ký tự đầu
    s_title = viet_hoa_dau_tu(s)
    print("Chuỗi sau khi chuyển ký tự đầu tiên của mỗi từ thành chữ hoa:", s_title)


if __name__ == "__main__":
    main()
