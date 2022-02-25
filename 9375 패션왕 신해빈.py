import sys
from itertools import combinations
N = int(sys.stdin.readline().strip())
for _ in range(0, N):
    answer = 1
    d = {}
    n = int(sys.stdin.readline().strip())
    for num in range(0, n):
        inp = sys.stdin.readline().strip().split(" ")
        if inp[1] in d:
            d[inp[1]].append(inp[0])
        else:
            d[inp[1]] = [inp[0]]
    for v in d.values():
        answer *= len(v) + 1
    print(answer - 1)
