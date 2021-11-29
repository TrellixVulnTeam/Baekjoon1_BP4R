from collections import deque
import sys
deq = deque()
N = int(input())
for n in range(0, N):
    inp = sys.stdin.readline().strip().split(" ")
    if inp[0] == 'push':
        deq.append(inp[1])
    if inp[0] == 'pop':
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)
    if inp[0] == 'size':
        print(len(deq))
    if inp[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    if inp[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    if inp[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])