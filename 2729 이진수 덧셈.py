N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    print(bin(A + B))