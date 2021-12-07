import sys
from collections import Counter
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    n = int(sys.stdin.readline())
    lst.append(n)
print(Counter(lst).most_common()[0][1])