from itertools import combinations
N, M = map(int, input().split())
lst = []
for n in range(1, N+1):
    lst.append(str(n))
for l in list(combinations(lst, M)):
    print(" ".join(l))