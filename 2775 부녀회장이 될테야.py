import sys
N = int(input())
for _ in range(0, N):
    floors = []
    lst = []
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    for num in range(1, n+1):
        lst.append(num)
    floors.append(lst)
    for a in range(1, k + 1):
        otherlst = []
        for x in range(0, n):
            otherlst.append(sum(floors[a-1][0:x+1]))
        floors.append(otherlst)
    print(floors[k][n - 1])