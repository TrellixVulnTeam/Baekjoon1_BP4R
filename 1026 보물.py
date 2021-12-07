import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
count = 0
while B:
    count += max(B) * min(A)
    B.pop(B.index(max(B)))
    A.pop(A.index(min(A)))
print(count)
