N = int(input())
space = N - 2
for n in range(1, N + 1):
    if n == N:
        print(('*' + ' ')*N , end = '')
    else:
        print(space * ' ' + n * (' ' + '*'))
        space -= 1


