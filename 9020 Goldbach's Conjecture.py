import sys
N = int(sys.stdin.readline().strip())
bools = [True for x in range(10004)]
bools[0] = False
bools[1] = False
for i in range(2, int(10004**0.5)):
    if bools[i] == True:
        for j in range(i + i, 10004, i):
            bools[j] = False
for _ in range(N):
    t = int(sys.stdin.readline().strip())
    minimum = 10000000
    A = 0
    B = 0
    mid = t // 2
    for m in range(mid, 0, -1):
        a = m
        b = t - a
        if bools[a] == True and bools[b] == True:
            if abs(a - b) < minimum:
                minimum = abs(a - b)
                A = min(a, b)
                B = max(a, b)      
    print(A, B)
