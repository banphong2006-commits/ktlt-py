chuoi = input("Nhập chuỗi các từ tiếng Anh: ")
ds = chuoi.split()
ds.sort()
print("Các từ theo thứ tự từ điển:")
for w in ds:
    print(w)
