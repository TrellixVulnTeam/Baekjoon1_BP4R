def f(n):
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return 4
    else:
        return f(n - 3) + f(n - 2) + f(n - 1)

N = int(input())
for _ in range(N):
    a = int(input())
    print(f(a))

