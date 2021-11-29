import sys
N = int(input())
homo = False
hetero = False
d = {}
for n in range(0, N):
    inp = sys.stdin.readline().strip().split(" ")
    if inp[0] == 'insert':
        if inp[1] not in d:
            d[inp[1]] = 1
        else:
            d[inp[1]] += 1

    if inp[0] == 'delete':
        if inp[1] in d:
            if d[inp[1]] > 1:
                d[inp[1]] -= 1
            else:
                d.pop(inp[1], None)
    if len(d.keys()) > 1:
        hetero = True
    else:
        hetero = False
    if len(d) != 0:
        if max(d.values()) > 1:
            homo = True
        else:
            homo = False

    if hetero == True and homo == True:
        print('both')
    if hetero == True and homo == False:
        print('hetero')
    if homo == True and hetero == False:
        print('homo')
    if hetero == False and homo == False:
        print('neither')


