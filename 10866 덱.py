import sys
N = int(input())
lst = []
for n in range(0, N):
    inp = sys.stdin.readline().strip().split(" ")
    if inp[0] == 'push_front':
        lst.insert(0, inp[1])
        continue
    if inp[0] == 'push_back':
        lst.append(inp[1])
        continue
    if inp[0] == 'size':
        print(len(lst))
        continue
    if inp[0] == 'pop_front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
            lst.pop(0)
        continue
    if inp[0] == 'pop_back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
            lst.pop(-1)
        continue
    if inp[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
            continue
    if inp[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    if inp[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])