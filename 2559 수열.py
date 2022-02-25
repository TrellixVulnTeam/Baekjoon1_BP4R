N, K = map(int, input().split())
lst = list(map(int, input().split()))
maximum = sum(lst[0:K])
s = maximum
for i in range(1, N - K + 1):
    s -= lst[i-1]
    s += lst[i + K - 1]
    maximum = max(maximum, s)
print(maximum)