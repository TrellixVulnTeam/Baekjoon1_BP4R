import sys
lst = []
K, N = map(int, sys.stdin.readline().split())
for _ in range(K):
    lst.append(int(sys.stdin.readline()))

length = max(lst)
high = length
low = 1

while low <= high:
    mid = (high + low) // 2
    # print(mid)
    num = 0
    for n in lst:
        num += n // mid
    if num >= N:
        low = mid + 1
    else:
        high = mid - 1

    # print(low, high)
print(high)
    
            
        
        