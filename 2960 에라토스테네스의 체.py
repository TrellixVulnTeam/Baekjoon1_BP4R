N, K = map(int, input().split())
lst = [n for n in range(2, N+1)]
dlst = []
while True:
    count = 0
    for num in lst:
        if count == 0:
            dlst.append(min(lst))
        count += 1
        if num > min(lst) and num % min(lst) == 0:
            dlst.append(num)
            lst.pop(lst.index(num))
    lst.pop(0)
    if len(lst) == 0:
        break

print(dlst[K-1])

