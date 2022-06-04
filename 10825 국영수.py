import sys
N = int(sys.stdin.readline().strip())
lst = []

for _ in range(N):
    lst.append(sys.stdin.readline().strip().split())

lst.sort(key =lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for l in lst:
    print(l[0])
