N = int(input())
A, B = map(int, input().split())
A = A // 2

if A + B <= N:
    print(A + B)
else:
    print(N)