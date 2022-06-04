N = int(input())
lst = [0, 1]
for n in range(2, N + 1):
    lst.append(lst[n - 2] + lst[n - 1])

print(lst[N])