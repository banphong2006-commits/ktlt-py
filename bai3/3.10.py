import math

def Tinh(R):
    if R <= 0:
        print("Bán kính không hợp lệ! Vui lòng nhập số dương.")
    else:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R * R
        print("Chu vi hình tròn là:", round(chu_vi, 2))
        print("Diện tích hình tròn là:", round(dien_tich, 2))


try:
    R = float(input("Nhập bán kính R: "))
    Tinh(R)
except ValueError:
    print("Giá trị nhập vào không hợp lệ! Vui lòng nhập một số.")
