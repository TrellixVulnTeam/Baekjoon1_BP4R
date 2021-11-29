N = int(input())
lst = []
for n in range(1, N + 1):
    string = '*' * n + ' ' * (2 * N - 2 * n) + '*' * n
    print(string)
    lst.append(string)
for i in range(len(lst) - 2, -1, -1):
    print(lst[i])
