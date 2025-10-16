chuoi = input("Nhập chuỗi: ")
moi = ''
for ch in chuoi:
    if not ch.isalpha():  
        moi += ch
print("Chuỗi mới:", moi)
