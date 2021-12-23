import sys
N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().strip().split()))
answer = lst[:]
d = {}
for k, v in enumerate(lst):
    d[k] = v
    for idx in range(k):
        if lst[idx] < v:
            answer[k] += d[idx]

print(max(answer))