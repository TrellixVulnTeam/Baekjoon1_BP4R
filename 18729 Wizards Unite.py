z = int(input())
for _ in range(z):
    answer = 0
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    for box in lst[0: n - k]:
        answer += box
    if answer >= lst[-1]:
        answer = answer
    else:
        answer = lst[-1]
    print(answer)
