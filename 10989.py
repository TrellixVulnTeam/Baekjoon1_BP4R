import sys
N = int(input())
d = [0 for x in range(1, 10001)]
for _ in range(0, N):
    inp = int(sys.stdin.readline())
    d[inp - 1] += 1
for n in d:
    if d[n] == 0:
        continue
    else:
        print(((str(n) + '\n')*d[n]).strip())






