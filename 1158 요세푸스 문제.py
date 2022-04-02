N, K = map(int, input().split())
lst = [n for n in range(1, N + 1)]

answer = []
index = 0

for i in range(N):
    index += K - 1
    if index >= len(lst):
        index = index % len(lst)

    answer.append(str(lst.pop(index)))
print("<", end= '')
for s in range(0, len(answer) - 1):
    print(answer[s], end= ', ')
print(answer[-1], end='')
print(">")

        