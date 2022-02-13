import sys
N, M = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
sums = []
s = 0
for l in lst:
    s += l
    sums.append(s)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 1:
        print(sums[b-1])
    else:
        print(sums[b-1]-sums[a-2])