import sys
while True:
    N, M = map(int, sys.stdin.readline().strip().split())
    if (N, M) == (0, 0):
        quit()
    lst = []
    ans = [0 for x in range(N)]
    for m in range(M):
        lst.append(list(map(int, sys.stdin.readline().strip().split())))

    for i in range(0, M):
        for j in range(0, N):
            ans[j] += lst[i][j]

    print(max(ans))
