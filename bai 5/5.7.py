# sequential_search_module.py
# Hàm tìm kiếm tuyến tính (Sequential Search)

def Sequential_Search(dlist, item):
    pos = 0
    found = False

    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1

    return found, pos + 1 if found else -1


# ==========================
# Chương trình chính
# ==========================
if __name__ == "__main__":
    # Nhập danh sách n phần tử từ bàn phím
    n = int(input("Nhập số phần tử của danh sách: "))
    dlist = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        dlist.append(x)

    item = int(input("Nhập phần tử cần tìm: "))

    found, position = Sequential_Search(dlist, item)

    if found:
        print(f"✅ Phần tử {item} được tìm thấy tại vị trí {position}.")
    else:
        print(f"❌ Phần tử {item} không có trong danh sách.")
