import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    count = 0
    s = 0
    for n in range(N):
        C, G = map(float, sys.stdin.readline().strip().split())
        count += C
        s += G * C
    answer = s / count
    print(int(count), '%.1f' % answer)