N = int(input())
lst = []
d = {}
for _ in range(N):
    name = input()
    lst.append(name)
    if name[0] not in d:
        d[name[0]] = 1
    else:
        d[name[0]] += 1
answer = []
for e in d:
    if d[e] >= 5:
        answer.append(e)

answer.sort()
if len(answer) == 0:
    print("PREDAJA")
else:
    print("".join(answer)) 
