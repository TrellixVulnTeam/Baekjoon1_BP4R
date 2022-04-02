N = int(input())
lst = [0, 1]
for n in range(2, N + 1):
    lst.append((lst[n - 1] + lst[n - 2])%1000000007)
print(lst[N] % 1000000007)
