A, B = map(int, input().split())
count = 1
lst = []
while len(lst) <= B:
    for _ in range(count):
        lst.append(count)
    count += 1
print(sum(lst[A-1:B]))
