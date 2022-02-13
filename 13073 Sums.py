import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s1 = [x for x in range(1, n + 1)]
    s2 = [y for y in range(1, 2 * n + 1, 2)]
    s3 = [z for z in range(2, 2 * n + 1, 2)]
    print(sum(s1), sum(s2), sum(s3))
   