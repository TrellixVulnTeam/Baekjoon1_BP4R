N, M = map(int, input().split())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
A = set(A)
B = set(B)
print(len(A - B))
for n in sorted(A - B):
    print(n, end = ' ')