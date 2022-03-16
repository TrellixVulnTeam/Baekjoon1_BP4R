import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    prime_lst = []
    for n in range(1, N):
        if N % n == 0:
            prime_lst.append(n)
    if sum(prime_lst) == N:
        print(f"{N} is a perfect number.")
    elif sum(prime_lst) > N:
        print(f"{N} is an abundant number.")
    elif sum(prime_lst) < N:
        print(f"{N} is a deficient number.")