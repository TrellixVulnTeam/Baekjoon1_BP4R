N, M = map(int, input().split())
lst = [1, 1]
c = 2
for n in range(N):
    lst.append(lst[-1] * c)
    c += 1
print(lst[N] // (lst[M] * lst[N - M]))
