import re

def kiem_tra_mat_khau(password):
    
    if len(password) < 6 or len(password) > 12:
        return False

    
    if not re.search("[a-z]", password):
        return False

    
    if not re.search("[A-Z]", password):
        return False

    
    if not re.search("[0-9]", password):
        return False

    
    if not re.search("[$#@]", password):
        return False

    return True



chuoi = input("Nhập mật khẩu (cách nhau bằng dấu phẩy): ").split(",")
hop_le = []

for mk in chuoi:
    if kiem_tra_mat_khau(mk.strip()):
        hop_le.append(mk.strip())

print("Mật khẩu hợp lệ:", ", ".join(hop_le))
