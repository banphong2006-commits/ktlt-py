
class mymath:
    @staticmethod
    def square(n):
        return n * n

    @staticmethod
    def cube(n):
        return n * n * n

    @staticmethod
    def average(values):
        nvals = len(values)
        total = 0.0
        for v in values:
            total += v
        return float(total) / nvals



values = [2, 4, 6, 8, 10]

print('Squares:')
for v in values:
    print(mymath.square(v))

print('Cubes:')
for v in values:
    print(mymath.cube(v))

print('Average:', mymath.average(values))


mt = mymath 

print("\nDùng mt:")
print(mt.square(2))
print(mt.square(3))
