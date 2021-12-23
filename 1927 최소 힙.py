import sys
import heapq
heap = []
#answer = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        try:
            a = heapq.heappop(heap)
            print(a)
            # answer.append(a)
        except:
            print(0)
            # answer.append(0)
    else:
        heapq.heappush(heap, x)
# for b in answer:
#     print(b)