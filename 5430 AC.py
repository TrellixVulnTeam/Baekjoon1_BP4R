import sys
from collections import deque
t = int(sys.stdin.readline().strip())
for _ in range(t):
    b = True
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    if n == 0:
        if 'D' in p:
            print("error")
            continue
        else:
            print("[]")
            continue
    if n == 1:
        l = sys.stdin.readline().strip()
        deq = deque(list(map(int, l[1:-1])))
    
    else:
        l = sys.stdin.readline().strip()
        deq = deque(list(map(int, l[1:-1].split(","))))

    r = False
    for f in p:
        if f == 'R':
            r = not r
        elif f == 'D':
            if r:
                try:
                    deq.pop()
                except:
                    print("")
            else:
                try:
                    deq.popleft()
                except:
                    print("error")
                    break
    if r:
        deq.reverse()
    print(str(deq)[6:-1])
            
