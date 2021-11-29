N = int(input())
A = list(map(int, input().split(" ")))
B = sorted(A, reverse=True)
P = []
lst = []
for n in range(0, N):
    P.append(0)
for aspect in A:
    lst.append((aspect, A.index(aspect)))
print(sorted(lst))
print(B)



