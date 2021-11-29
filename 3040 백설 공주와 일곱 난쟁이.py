from itertools import combinations
lst = []
alst = []
for _ in range(0, 9):
    lst.append(int(input()))
for l in list(combinations(lst, 7)):
    if sum(l) == 100:
        lst = l

for n in lst:
    print(n)