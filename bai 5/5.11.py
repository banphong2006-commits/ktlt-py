import numpy as np

# Dữ liệu đầu vào
data = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Khai báo kiểu dữ liệu có cấu trúc
dt = np.dtype([
    ('name', 'U10'),   # U10: chuỗi Unicode dài tối đa 10 ký tự
    ('class', 'i4'),   # i4: số nguyên 4 byte
    ('height', 'f4')   # f4: số thực 4 byte
])

# Tạo mảng có cấu trúc
students = np.array(data, dtype=dt)

# Sắp xếp theo 'class', sau đó theo 'height'
sorted_students = np.sort(students, order=['class', 'height'])

# In kết quả
print("Kết quả sắp xếp:")
for s in sorted_students:
    print(s)
