import sys
T = int(input())
for _ in range(0, T):
    a, b = map(int, sys.stdin.readline().split())
    if pow(a,b, 10) == 0:
        print(10)
        continue
    else:
        print(pow(a,b,10))