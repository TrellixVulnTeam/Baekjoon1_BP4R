import sys
N = int(sys.stdin.readline().strip())
s = 0
lst = list(map(int, sys.stdin.readline().strip().split()))
sums = []
for l in lst:
    s += l
    sums.append(s)
M = int(sys.stdin.readline().strip())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 1:
        print(sums[b-1])
    else:
        print(sums[b-1] - sums[a-2])