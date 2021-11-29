N = int(input())
lst = []
l = []
for _ in range(0,N):
    x, y = input().split()
    lst.append((int(x),int(y)))

for k,v in lst:
    l.append((v, k))
sortedl = sorted(l)

for k,v in sortedl:
    print(v,k)
