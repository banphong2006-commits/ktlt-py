n = int(input("Nhập n: "))
for i in range(1, n):
    tong_uoc = sum(j for j in range(1, i) if i % j == 0)
    if tong_uoc > i:
        print(i)
