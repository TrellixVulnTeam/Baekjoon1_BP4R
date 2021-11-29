N, K = input().split()
N = int(N)
K = int(K)
A = input().split()
lst = []
for n in A:
    lst.append(int(n))
print(int(sorted(lst)[K - 1]))