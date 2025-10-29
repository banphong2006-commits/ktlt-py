
def sort_list(lst):
    """Hàm sắp xếp danh sách tăng dần"""
    return sorted(lst)

def find_max(lst):
    """Hàm tìm phần tử lớn nhất"""
    return max(lst)

def find_min(lst):
    """Hàm tìm phần tử nhỏ nhất"""
    return min(lst)

# --- Chương trình chính ---
n = int(input("Nhập số lượng phần tử: "))

lst = []
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

sorted_lst = sort_list(lst)
max_value = find_max(lst)
min_value = find_min(lst)

print("\nDanh sách ban đầu:", lst)
print("Danh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)
