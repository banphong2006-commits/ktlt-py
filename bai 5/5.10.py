# bubble_sort_module.py
# Hàm sắp xếp nổi bọt (Bubble Sort)

def bubbleSort(nlist):
    loop = len(nlist) - 1
    for i in range(loop):
        swapped = False
        for j in range(loop - i):
            # So sánh 2 phần tử liền kề
            if nlist[j] > nlist[j + 1]:
                # Hoán đổi chỗ
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True

        # Nếu không còn hoán đổi => mảng đã được sắp xếp
        if not swapped:
            break

    return nlist


# ==========================
# Chương trình chính
# ==========================
if __name__ == "__main__":
    # Nhập danh sách n phần tử
    n = int(input("Nhập số phần tử của danh sách: "))
    nlist = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        nlist.append(x)

    print("\nDanh sách ban đầu:", nlist)
    sorted_list = bubbleSort(nlist)
    print("Danh sách sau khi sắp xếp tăng dần:", sorted_list)
