N = int(input())
lst = sorted(list(map(int, input().split())))
i = 0
j = N - 1
answer = abs(lst[i] + lst[j])
A = lst[i]
B = lst[j]
while i < j:
    s = lst[i] + lst[j]
    if abs(s) < answer:
        answer = abs(s)
        A = lst[i]
        B = lst[j]
    if s < 0:
        i += 1
    elif s > 0:
        j -= 1
    else:
        break
print(A, B)
