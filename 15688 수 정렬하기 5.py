import sys
N = int(sys.stdin.readline().strip())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))
for a in sorted(lst):
    print(a)