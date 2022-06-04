lst = []
l = []
d = {}
for _ in range(10):
    lst.append(int(input()))
average = sum(lst)//10
for e in lst:
    if e in d:
        d[e] += 1
    else:
        d[e] = 1

di = {}
for k in d:
    if d[k] in di:
        di[d[k]].append(k)
    else:
        di[d[k]] = [k]

print(average)
print(di[max(di.keys())][0])