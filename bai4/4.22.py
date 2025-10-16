ket_qua = []
for i in range(1000, 3001):
    s = str(i)
    if all(int(ch) % 2 == 0 for ch in s):  
        ket_qua.append(s)

print(','.join(ket_qua))
