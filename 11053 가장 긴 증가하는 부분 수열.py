import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
answer = [1] * len(A)
for k, v in enumerate(A):
    for smaller in range(k):
        if A[smaller] < v:
            answer[k] = max(answer[k], 1 + answer[smaller])

print(max(answer))