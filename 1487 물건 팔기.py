N = int(input())
lst = []
answer = 0
max_price = 0
for n in range(N):
    lst.append(tuple(map(int, input().split())))
lst.sort(key = lambda x: x[0], reverse=True)
for num in range(1000000, -1, -1):
    s = 0
    price = lst[num][0]
    for l in lst:
        if l[0] >= price:
            s += price - l[1]
    if s >= answer:
        answer = max(answer, s)
        max_price = price

print(max_price)