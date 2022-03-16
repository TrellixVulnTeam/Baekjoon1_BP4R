N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = []
count = 0
for n in lst:
    count += n
    lst2.append(count)
maximum = lst2[K - 1] 
for num in range(0, N-K):
    maximum = max(maximum, lst2[num + K] - lst2[num])

print(maximum)