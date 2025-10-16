tong = 0
print("Nhập nhật ký giao dịch (ví dụ: D 300 hoặc W 200). Gõ trống để kết thúc:")

while True:
    du_lieu = input()
    if not du_lieu:   
        break
    lenh, so_tien = du_lieu.split()
    so_tien = int(so_tien)

    if lenh == 'D':        
        tong += so_tien
    elif lenh == 'W':      
        tong -= so_tien

print("Số tiền còn lại trong tài khoản là:", tong)
