import sys
x = int(input())
for num in range(1,x+1):
    m,n= map(int, sys.stdin.readline().split())
    print(m+n)
