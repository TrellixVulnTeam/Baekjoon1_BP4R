import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
for _ in range(N):

    lst = list(map(int, input().split()))
    total = lst.pop(0)
    d = Counter(lst)
    di = {}
    for c in d:
        if d[c] in di:
            di[d[c]].append(c)
        else:
            di[d[c]] = [c]
    if len(di[max(di.keys())]) > 1:
        print("SYJKGW")
    else:
        if max(di.keys()) > total // 2:
            print(di[max(di.keys())][0])
        else:
            print("SYJKGW")
        