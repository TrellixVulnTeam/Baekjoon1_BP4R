N, M = map(int, input().split())
lst = []
l = []
for _ in range(N):
    l = list(map(int, input().split()))
    for a in l:
        lst.append(a)
lst.sort()
for element in lst:
    print(element, end= ' ')