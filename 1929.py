def prime(M, N, l):
    import math
    for n in range(M, N+1):
        count = 0
        if n == 1:
            continue
        for num in range(2, int(math.sqrt(n)) + 1):
            if n%num == 0:
                count += 1
                break
        if count < 1:
            l.append(n)


    for a in l:
        print(a)


M, N = map(int, input().split())
lst = []

prime(M, N, lst)


