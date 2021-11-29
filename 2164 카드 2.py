from collections import deque
deq = deque()
N = int(input())
if N == 1:
    print(1)
    quit()
for n in range(1, N + 1):
    deq.append(n)
while True:
    deq.popleft()
    deq.append(deq[0])
    deq.popleft()
    if len(deq) == 1:
        break
print(deq[0])
