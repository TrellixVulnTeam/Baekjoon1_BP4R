from collections import Counter

N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

d = Counter(lst)

di = {}

for k in d:
    if d[k] in di:
        di[d[k]].append(k)
    else:
        di[d[k]] = [k]

print(sorted(di[max(di.keys())])[-1], max(di.keys()))