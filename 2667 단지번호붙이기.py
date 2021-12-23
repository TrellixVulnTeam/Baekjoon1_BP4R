import sys
N = int(sys.stdin.readline().strip())
map = []
for _ in range(N):
    lst = []
    row = sys.stdin.readline().strip()
    for r in row:
        lst.append(r)
    map.append(lst)

