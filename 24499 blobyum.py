N, K = map(int, input().split())
lst = list(map(int, input().split()))
maximum = sum(lst[0:K])
s = maximum
for n in range(1, len(lst)):
    if n + K - 1< len(lst):
        s = s - lst[n-1] + lst[n + K - 1]
        maximum = max(maximum, s)
        
    else:
        s = s - lst[n-1] + lst[n + K - 1 -len(lst)]
        maximum = max(maximum, s)
print(maximum)
