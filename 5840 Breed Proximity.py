import sys
N, K = map(int, sys.stdin.readline().strip().split())
prox = []
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))

answer = -1
lst = list(enumerate(lst))

d = {}
lst.sort(key=lambda x: x[1], reverse = True)
for l in lst:
    if l[1] in d:
        d[l[1]].append(l[0])
    else:
        d[l[1]] = [l[0]]

for k in d:
    for i in range(1, len(d[k])):
        if abs(d[k][i] - d[k][i-1]) <= K:
            answer = k
            print(answer)
            quit()

print(answer)





