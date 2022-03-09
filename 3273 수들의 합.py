N = int(input())
lst = list(map(int, input().split()))
target = int(input())
lst.sort()
i = 0
j = len(lst) - 1
answer = 0
while i < j:
    if lst[i] + lst[j] == target:
        answer += 1
        i += 1
    elif lst[i] + lst[j] > target:
        j -= 1
    elif lst[i] + lst[j] < target:
        i += 1
print(answer)