ylst = []
xlst = []
for _ in range(0, 3):
    x, y = map(int, input().split())
    xlst.append(x)
    ylst.append(y)

d = {}
c = {}
for n in xlst:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
for num in ylst:
    if num in c:
        c[num] += 1
    else:
        c[num] = 1
for k in d:
    if d[k] == 1:
        print(k, end = ' ')
for key in c:
    if c[key] == 1:
        print(key)
