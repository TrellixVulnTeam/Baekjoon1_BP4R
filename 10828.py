import sys
N = int(input())
lst = []
for _ in range(0, N):
    inp = sys.stdin.readline().strip().split()
    if inp[0] == 'push':
        lst.append(int(inp[1]))
    if inp[0] == 'pop':
        if len(lst) != 0:
            print(lst[-1])
            lst.pop(-1)
        else:
            print(-1)
    if inp[0] == 'size':
        print(len(lst))
    if inp[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    if inp[0] == 'top':
        if len(lst) != 0:
            print(lst[-1])
        else:
            print(-1)
