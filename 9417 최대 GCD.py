from itertools import combinations

def gcd(a, b):
    if min(a, b) == 0 or a == b:
        return max(a, b)
    return gcd(min(a, b), max(a, b)% min(a, b))


N = int(input())
for _ in range(0, N):
    maximum = 0
    lst = list(map(int, input().split(" ")))
    for l in list(combinations(lst, 2)):
        gcd(l[0], l[1])
        if maximum == 0:
            maximum = gcd(l[0], l[1])
        elif maximum < gcd(l[0], l[1]):
            maximum = gcd(l[0], l[1])
    print(maximum)