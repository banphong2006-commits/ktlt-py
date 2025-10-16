ds = input("Nhập dãy từ: ").split()
maxlen = max(len(w) for w in ds)
for w in ds:
    if len(w) == maxlen:
        print(w)
