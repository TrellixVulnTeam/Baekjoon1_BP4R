import sys
N = int(input())
lst = [int(sys.stdin.readline()) for n in range(0,N)]
for num in sorted(lst):
    print(num)