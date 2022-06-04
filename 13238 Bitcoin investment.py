N = int(input())
lst = list(map(int, input().split()))
i = 0
answer = 0
for l in lst:
    for j in range(i, len(lst)):
        answer = max(answer, lst[j] - l)
    i += 1
print(answer)

