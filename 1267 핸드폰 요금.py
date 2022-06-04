N = int(input())
lst = list(map(int, input().split()))
y = 0
m = 0
for l in lst:
    y += ((l)// 30 + 1) * 10
    m += ((l)// 60 + 1) * 15
if y < m:
    print("Y", y)
elif y == m:
    print("Y M", y)
else:
    print("M", m)

