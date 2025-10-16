ds = input("Nhập danh sách: ").split()
ds.remove('123')  

print("Danh sách sau khi xóa '123':")
for ch in ds:
    print(ch)
