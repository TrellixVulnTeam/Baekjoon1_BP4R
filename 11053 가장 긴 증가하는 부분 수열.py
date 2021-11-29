from itertools import combinations
N = int(input())
lst = list(map(int, input().split(" ")))
for n in range(N, 0, -1):
    for l in list(combinations(lst, n)):
        if sorted(l, reverse = True) == l:
            print(len(l))
