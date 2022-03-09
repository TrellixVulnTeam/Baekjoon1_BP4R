N = int(input())
for _ in range(N):
    A, B = input().split()
    A = int(A, 2)
    B = int(B, 2)
    print(str(bin(A + B))[2:])