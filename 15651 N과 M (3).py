from itertools import combinations
N, M = map(int, input().split())
lst = []
for x in range(1, N + 1):
    for m in range(M):
        lst.append(x)
for l in combinations(lst, M):
    for a in l:
        print(a, end= ' ')

    print()

