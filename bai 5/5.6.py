
lst = []

n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Tìm giá trị lớn nhất và nhỏ nhất
max_value = max(lst)
min_value = min(lst)

# Tìm vị trí (index) của chúng
max_index = lst.index(max_value)
min_index = lst.index(min_value)

# In kết quả
print("\nDanh sách:", lst)
print(f"Phần tử lớn nhất: {max_value} ở vị trí {max_index}")
print(f"Phần tử nhỏ nhất: {min_value} ở vị trí {min_index}")
