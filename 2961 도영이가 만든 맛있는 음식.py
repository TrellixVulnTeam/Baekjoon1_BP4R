from itertools import combinations
N = int(input())
minimum = 0
lst = []
for n in range(0, N):
    lst.append((list(map(int, input().split()))))
for num in range(1, N + 1):
    for l in list(combinations(lst, num)):
        slst = []
        blst = []
        for a in range(0, num):
            slst.append(l[a][0])
            blst.append(l[a][1])
        if len(slst) == 1 and slst[0] == blst[0]:
            print(0)
            quit()
        sigma = abs(eval("*".join(list(map(str, slst)))) - sum(blst))
        if minimum == 0:
            minimum = sigma
        else:
            if minimum > sigma:
                minimum = sigma
print(minimum)
