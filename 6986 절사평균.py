import sys
N, K = map(int, sys.stdin.readline().strip().split())
lst = []
for _ in range(N):
    lst.append(float(sys.stdin.readline().strip()))
lst.sort()
s = 0
for l in lst[K:N-K]:
    s += l
  
o = 0
for i in range(0, K):
    lst[i] = lst[K]
for j in range(N-K - 1, N):
    lst[j] = lst[N-K-1]
for li in lst:
    o += li
print(f"{s / (N - 2*K):.2f}")
print(f"{(o / N):.2f}")
