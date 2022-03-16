N = int(input())
M = int(input())
lst = sorted(list(map(int, input().split())))
i = 0
j = len(lst) - 1
answer = 0
while i < j:
    if lst[i] + lst[j] == M:
        answer += 1
        i += 1
    elif lst[i] + lst[j] > M:
        j -= 1
    elif lst[i] + lst[j] < M:
        i += 1
print(answer)