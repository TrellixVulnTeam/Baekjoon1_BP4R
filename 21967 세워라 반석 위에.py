import sys
from collections import deque
N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().strip().split()))
deq = deque([])
checker = [0 for n in range(11)]
answer = 0 

def check():
    a = 0
    b = 0
    for k in range(1, 11):
        if checker[k] > 0:
            a = k
            break
    for h in range(10, 0, -1):
        if checker[h] > 0:
            b = h
            break
    return b - a

for i in range(0, len(lst)):
    deq.append(lst[i])
    checker[lst[i]] += 1
    while check() > 2 and deq:
        checker[deq[0]] -= 1
        deq.popleft()
    answer = max(answer, len(deq))
    
    
print(answer)
