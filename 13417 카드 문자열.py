from collections import deque
import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    lst = sys.stdin.readline().strip().split()
    deq = deque()
    for l in lst:
        if len(deq) == 0:
            deq.append(l)
        else:
            if l <= deq[0]:
                deq.appendleft(l)
            else:
                deq.append(l)
    print("".join(deq))