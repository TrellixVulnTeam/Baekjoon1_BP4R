from itertools import combinations
n = int(input())
lst = input().split()
maximum = int(lst[0]) * int(lst[1])

for l in combinations(lst, 2):
    maximum = max(maximum, eval("*".join(l)))
for li in combinations(lst, 3):
    maximum = max(maximum, eval("*".join(li)))

print(maximum)

