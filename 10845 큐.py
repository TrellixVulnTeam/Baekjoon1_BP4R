import sys
N = int(input())
lst = []
for n in range(0, N):
    inp = sys.stdin.readline().strip().split(" ")
    if inp[0] == 'push':
        lst.append(inp[1])
        continue
    if inp[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
        continue
    if inp[0] == 'size':
        print(len(lst))
        continue
    if inp[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
        continue
    if inp[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
        continue
    if inp[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
            lst.pop(0)
            continue



