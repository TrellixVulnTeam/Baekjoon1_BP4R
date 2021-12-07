import sys
t = int(sys.stdin.readline())
lst = [n for n in range(1, 51)]
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    for l in lst:
        if l != a + b:
            print(l)
            break
