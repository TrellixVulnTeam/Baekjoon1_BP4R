import sys
t = int(sys.stdin.readline())
for _ in range(t):
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort(reverse=True)
    print(lst[2])