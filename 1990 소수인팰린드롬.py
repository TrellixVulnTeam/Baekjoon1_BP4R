import sys

M, N = map(int, sys.stdin.readline().split())
lst = [True for n in range(0, N + 1)]

m = int(pow(N, 0.5))

for i in range(2, m + 1):
    if lst[i] == True:
        for j in range(2*i, N, i):
            lst[j] = False

prime_lst = (x for x in range(M, N + 1) if lst[x] == True)


for a in prime_lst:
    if "".join(reversed(str(a))) == str(a):
        sys.stdout.write(str(a) + '\n')
print(-1)

