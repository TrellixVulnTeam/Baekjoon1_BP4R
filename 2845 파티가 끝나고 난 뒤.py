N, A = map(int, input().split())
lst = list(map(int, input().split(" ")))
for n in lst:
    print(n - N * A, end = ' ')