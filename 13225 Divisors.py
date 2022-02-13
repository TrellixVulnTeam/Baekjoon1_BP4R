import sys
c = int(sys.stdin.readline().strip())
for _ in range(c):
    count = 0
    n = int(sys.stdin.readline().strip())
    for num in range(1, n + 1):
        if n % num == 0:
            count += 1
    print(n, count)