import sys
N, M = map(int, sys.stdin.readline().strip().split())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))

lst.sort()
i = 0
j = len(lst) - 1
minimum = abs(lst[j] - lst[i])

while i <= j:
    if abs(lst[j] - lst[i]) < minimum and abs(lst[j] - lst[i]) >= M:
        