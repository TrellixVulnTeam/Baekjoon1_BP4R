N, K = map(int, input().split())
lst = []
count = 2
lst.append(1)
lst.append(1)
for _ in range(N):
    lst.append(lst[-1]*count)
    count += 1

print((lst[N] // (lst[K] * lst[N - K]))%10007)
