import sys
N = int(input())
lst = []
for _ in range(1, N+1):
    lst.append(int(sys.stdin.readline()))
for n in sorted(lst, reverse = True):
    print(n)