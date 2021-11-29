def f(x): return x % 2 != 0 and x % 3 != 0

f(33)

f(17)

print(list(filter(f, range(2, 25))))
