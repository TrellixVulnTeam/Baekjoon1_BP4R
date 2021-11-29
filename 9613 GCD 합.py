from itertools import combinations
N = int(input())


def gcf(a, b):
    if min(a, b) == 0 or a == b:
        g = max(a, b)
        return g
    aprime = max(a, b) % min(a, b)
    return gcf(min(a, b), aprime)


for _ in range(0, N):
    s = 0
    lst = list(map(int, input().split(" ")))[1:]
    for l in list(combinations(lst, 2)):
        s += gcf(l[0], l[1])
    print(s)