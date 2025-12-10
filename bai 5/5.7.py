import numpy as np

# Khai báo kiểu dữ liệu cho mảng cấu trúc (structured array)
data_type = [
    ('name', 'S15'),   # tên sinh viên (string, tối đa 15 ký tự)
    ('class', int),    # lớp (kiểu int)
    ('height', float)  # chiều cao (float)
]

# Dữ liệu sinh viên
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

# Tạo mảng structured array
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

# Sắp xếp theo chiều cao
print("\nSort by height:")
print(np.sort(students, order='height'))
