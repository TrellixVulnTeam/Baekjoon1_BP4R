import sys
N = int(sys.stdin.readline().strip())
for n in range(1, N + 1):
    answer = 0
    r, l, num = map(int, sys.stdin.readline().strip().split())
    lst = []
    for _ in range(num):
        lst.append(int(sys.stdin.readline().strip()))
    count = 0
    lst.sort()
    for l in lst:
        if l >= 0.5:
            count += 1
            answer += l
        else:
            answer += 1 - l
    if count < r:
        for c in range(0, r - count):
            answer -= 1 - lst[0]
            answer += lst[0]
    elif count > l:
        for c in range(0, r - )
        {:.2f}.format(round(answer, 2))