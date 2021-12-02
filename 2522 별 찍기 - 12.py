N = int(input())
space = N
for n in range(1, N + 1):
    print(' '*(space - n) + '*' * n)
for num in range(N - 1, 0, -1):
    print(' ' * (space - num) + '*' * num)