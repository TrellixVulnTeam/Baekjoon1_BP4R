import sys
N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split(" ")))
maximum = 1000000000
minimum = 0
while True:
    check = 0
    ocheck = 0
    mid = (maximum + minimum) // 2
    for t in trees:
        if t - mid > 0:
            check += t - mid
        if t - mid > 1:
            ocheck += t - mid - 1
        else:
            continue
    if check > M:
        minimum = mid + 1
    elif check < M:
        maximum = mid - 1
    if check == M:
        print(mid)
        break
    if check >= M and ocheck < M:
        print(mid)
        break
    
    
    