import sys
N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
d = {}
count = 0
for n in sorted([x for x in set(lst)]):
    d[n] = count
    count += 1
for num in lst:
    print(d[num], end = ' ')

