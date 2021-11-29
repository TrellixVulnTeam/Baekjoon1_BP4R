import math
import sys

def prime(M, N):
    answer_count = 0
    for n in range(M + 1, N+1):
        count = 0
        if n == 1:
            continue
        for num in range(2, int(math.sqrt(n)) + 1):
            if n%num == 0:
                count += 1
                break
        if count < 1:
            answer_count += 1
    return answer_count




while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break
    else:
        print(prime(N, 2*N))