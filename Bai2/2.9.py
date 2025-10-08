s = input("Nhập chuỗi: ")
char_count = {}

for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("Kết quả:", char_count)
