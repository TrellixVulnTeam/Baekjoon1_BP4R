N = int(input())

lst = [[0 for x in range(0, 100)] for y in range(0, 100)]

for num in range(0, N):
    side, up = map(int, input().split())
    for b in range(up, up + 10):
        for a in range(side, side + 10):
            lst[b][a] = 1

count = 0
for l in lst:
    for o in l:
        if o == 1:
            count += 1

print(count)



