n = int(input("Nhập n: "))
a, b = 0, 1
fib = []
while a < n:
    fib.append(a)
    a, b = b, a + b
print("Dãy Fibonacci nhỏ hơn", n, "là:")
print(fib)
