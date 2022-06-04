import sys
N = int(sys.stdin.readline().strip())
d = {}
for _ in range(N):
    book = sys.stdin.readline().strip()
    if book not in d:
        d[book] = 1
    else:
        d[book] += 1
c = {}
for e in d:
    if d[e] in c:
        c[d[e]].append(e)
    else:
        c[d[e]] = [e]


lst = c[max(c.keys())]

lst.sort()
print(lst[0])