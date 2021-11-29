import sys
N = int(input())
lst = []
lst = [int(sys.stdin.readline()) for n in range(0,N)]
mean = round(sum(lst)/N)

slst = sorted(lst)
median = slst[(N//2)]

d = {}
for num in lst:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
f = {}
for key, value in d.items():
    if value not in f:
        f[value] = [key]
    else:
        f[value].append(key)
if len(f[max(f.keys())]) > 1:
    mode = sorted(f[max(f.keys())])[1]
else:
    mode = f[max(f.keys())][0]

rnge = max(lst) - min(lst)

print(mean)
print(median)
print(mode)
print(rnge)
