T = int(input())
for _ in range(T):
    n = int(input())
    total = 0
    add = 1
    for num in range(0, n):
        total += add
        add += 1
    print(total)