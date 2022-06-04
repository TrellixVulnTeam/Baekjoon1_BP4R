import math
N = int(input())
for _ in range(N):
    c = []
    a, b = map(int, input().split())
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            if i != a // i:
                c.append(a//i)
                c.append(i)
            else:
                c.append(i)
    if sum(c) == b:
        print("yes")
    else:
        print("no")
        