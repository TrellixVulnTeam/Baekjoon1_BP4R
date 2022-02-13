t = int(input())
for _ in range(t):
    lst = sorted(list(map(int, input().split())))
    lst.pop()
    lst.pop(0)
    if max(lst) - min(lst) >= 4:
        print("KIN")
    else:
        print(sum(lst))