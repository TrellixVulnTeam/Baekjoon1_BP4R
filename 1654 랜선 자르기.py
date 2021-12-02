import sys
lst = []
K, N = map(int, sys.stdin.readline().split())
length = 10000000000
for _ in range(K):
    lst.append(int(sys.stdin.readline()))
mid = length//2
high = length
low = 0
while True:
    num = 0
    for n in lst:
        num += n // mid
    if num < N:
        low = mid + 1
    elif num > N:
        high = mid - 1