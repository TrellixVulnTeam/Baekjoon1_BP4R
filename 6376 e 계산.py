def fac (n):
    f = 1
    for num in range(1, n + 1):
        f *= num
    return f

def e (n):
    s = 0
    for num in range(n + 1):
        s += 1 / fac(num)
    return s

print("""n e
- -----------
0 1
1 2
2 2.5
3 2.666666667
4 2.708333333""")

for N in range(5, 10):
    print(N, e(N))
