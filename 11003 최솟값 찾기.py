import sys
from collections import deque
N, L = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
deq = deque()
for n in range(0, N):
    while deq and deq[-1][0] > lst[n]:
        deq.pop()
    while deq and deq[0][1] < n - L + 1:
        deq.popleft()
    deq.append((lst[n], n)) 
    print(deq[0][0], end = ' ')