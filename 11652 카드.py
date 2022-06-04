import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))

d = Counter(lst)

di = {}
for k in d:
    if d[k] in di:
        di[d[k]].append(k)
    else:
        di[d[k]] = [k]

print(min(di[max(di.keys())]))