N, M = map(int, input().split())
lst = []
for x in range(N):
    lst.append(list(map(int, input().split())))
answer = [0 for x in range(M)]
k = 0
for i in range(M):
    for j in range(N):
        answer[k] += lst[j][i]
    k += 1
print(max(answer))
