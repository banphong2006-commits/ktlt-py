# Hàm cộng hai số
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Không thể chia cho 0!"
    return x / y


print("Chọn phép toán:")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")


choice = input("Nhập lựa chọn (1/2/3/4): ")


num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

if choice == '1':
    print("Kết quả:", num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print("Kết quả:", num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print("Kết quả:", num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print("Kết quả:", num1, "/", num2, "=", divide(num1, num2))
else:
    print("Lựa chọn không hợp lệ!")
