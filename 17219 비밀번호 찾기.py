import sys
pw = {}
N, M = map(int, sys.stdin.readline().strip().split())
for _ in range(N):
    site, password = sys.stdin.readline().strip().split()
    pw[site] = password
for m in range(M):
    s = sys.stdin.readline().strip()
    print(pw[s])