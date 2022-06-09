N, M = map(int, input().split())
lst = []
for n in range(N):
    line = input()
    ap = []
    for l in range(len(line) - 1, -1, -1):
        ap.append(line[l])
    lst.append(ap)
for l in lst:
    print("".join(l))
