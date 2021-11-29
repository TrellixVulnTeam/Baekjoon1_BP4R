import sys
N = int(input())
for _ in range(0, N):
    d = {}
    n = int(input())
    for num in range(0, n):
        inp = input().split(" ")
        d[inp[1]] = inp[0]
        print(d)