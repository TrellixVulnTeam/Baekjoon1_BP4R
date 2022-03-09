N, M = map(int, input().split())
lst =  list(map(int, input().split()))
count = 0
s = []
for l in lst:
    count += l
    s.append(count)