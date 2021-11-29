lst = []
lste = []
N = int(input())
if N == 1:
    print(1)
    quit()


def eraser(N, l, m):
    for n in range(1, N+1):
        l.append(n)
    while True:
        m = l[1::2]
        if len(m) == 1:
            return m[0]
        l = m


print(eraser(N, lst, lste))
