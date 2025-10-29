# all_in_one.py
# Chứa: mymath (hàm), ví dụ datetime, ví dụ numpy

# --- mymath (định nghĩa dưới dạng hàm, không cần class) ---
def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    if not values:
        return 0.0
    total = 0.0
    for v in values:
        total += v
    return float(total) / len(values)


# --- ví dụ dùng mymath ---
values = [2, 4, 6, 8, 10]

print('Squares:')
for v in values:
    print(square(v))

print('Cubes:')
for v in values:
    print(cube(v))

print('Average:', average(values))


# --- datetime example ---
import datetime as dt

fmt = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', fmt)

print('\nDatetime example:')
print('Day:', t1.day)
print('Month:', t1.month)
print('Minute:', t1.minute)
print('Second:', t1.second)

t2 = dt.datetime.now()
diff = t2 - t1
print('How many days difference?', diff.days)


# --- numpy example ---
# Lưu ý: cần cài numpy trước: pip install numpy
try:
    import numpy as np
    x = np.arange(12, 38)  # 12..37
    print('\nNumpy array from 12 to 37:')
    print(x)
except ImportError:
    print('\nNumpy is not installed. Install with: pip install numpy')
