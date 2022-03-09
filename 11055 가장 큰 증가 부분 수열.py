import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
s = A[:]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            s[i] = max(s[i], s[i] + A[i])
print(max(s))