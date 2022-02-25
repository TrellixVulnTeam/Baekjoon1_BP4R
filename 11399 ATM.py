N = int(input())
lst = sorted(list(map(int, input().split())))
separate = lst[::]
answer = 0
s = 0
for i in range(0, len(lst) - 1):
    answer += lst[i]
    s += separate[i]
    lst[i+1] += s
answer += lst[-1]
print(answer)