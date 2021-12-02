import sys
N, M, B = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 1000000000
height = 0 
for n in range(256, -1, -1):
    surplus = 0
    shortage = 0
    for l in lst:
        for s in l:
            if s < n:
                shortage += n - s
            if s > n:
                surplus += s - n
    if shortage > B + surplus:
        continue
    if surplus * 2 + shortage < answer:
        height = n
        answer = surplus * 2 + shortage
print(answer, height)
    