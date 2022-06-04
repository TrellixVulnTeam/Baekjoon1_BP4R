N, M = map(int, input().split())
lst = list(map(int, input().split()))
answer = []
for l in lst:
    for j in range(l, N + 1, l):
        answer.append(j)

print(sum(list(set(answer))))


