N, K, I = map(int, input().split())
count = 0
lst = []
bracket = []
listcount = 0
for _ in range(1, N + 1):
    lst.append(_)
while True:
    if listcount % 2 == 0:
        if abs(lst.index(K) - lst.index(I)) == 1:
            break
        for n in range(0, len(lst), 2):
            if lst[n] == K or lst[n] == I:
                bracket.append

    