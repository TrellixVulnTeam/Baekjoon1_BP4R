N = int(input())
A = list(map(int, input().split()))
lst = []
other = []
for i in range(len(A) - 1, -1, -1): 
    while len(other) > 0 and other[-1] <= A[i]:
        other.pop()
        
    if len(other) == 0:
        lst.append(-1)
    else:
        lst.append(other[-1])
    other.append(A[i])
for l in range(len(A) - 1, -1, -1):
    print(lst[l], end = ' ')