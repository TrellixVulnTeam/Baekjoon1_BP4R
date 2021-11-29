from itertools import combinations
count = 0
N, S = map(int, input().split())
lst = list(map(int,input().split(" ")))
for n in range(1, N+1):
    comb = list(combinations(lst, n))
    for num in range(0, len(comb)):
        if sum(comb[num]) == S:
            count += 1
print(count)

