# binary_search_module.py
# Hàm tìm kiếm nhị phân (Binary Search)

def binary_search(dlist, value):
    lowerBound = 0
    upperBound = len(dlist) - 1
    found = False

    while lowerBound <= upperBound and not found:
        midPoint = (lowerBound + upperBound) // 2  # chia lấy phần nguyên

        if dlist[midPoint] == value:
            found = True
        elif dlist[midPoint] < value:
            lowerBound = midPoint + 1
        else:
            upperBound = midPoint - 1

    return found


# ==========================
# Chương trình chính
# ==========================
if __name__ == "__main__":
    # Nhập danh sách n phần tử từ bàn phím
    n = int(input("Nhập số phần tử của danh sách (đã sắp xếp tăng dần): "))
    dlist = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        dlist.append(x)

    value = int(input("Nhập phần tử cần tìm: "))

    found = binary_search(dlist, value)

    if found:
        print(f"✅ Phần tử {value} được tìm thấy trong danh sách.")
    else:
        print(f"❌ Phần tử {value} không tồn tại trong danh sách.")
