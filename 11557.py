n = int(input())
for a in range(0, n):
    lst = []
    num = int(input())
    for b in range(0, num):
        c, alcohol = input().split()
        lst.append((int(alcohol), c))
    print(max(lst)[1])
