import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    count = 0
    q, l = map(int, sys.stdin.readline().split())
    deq = deque(list(map(int, sys.stdin.readline().split())))
    while True:
        if deq[0] == max(deq):
            if l == 0:
                count += 1
                print(count)
                break
            deq.popleft()
            count += 1
            l -= 1
        else:
            if l == 0:
                deq.append(deq[0])
                deq.popleft()
                l = len(deq) - 1
            else:
                deq.append(deq[0])
                deq.popleft()
                l -= 1