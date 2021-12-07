import sys
N, K = map(int ,sys.stdin.readline().split())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
count = 0
total = 0
for n in range(N - 1, -1, -1):
    while K - total >= lst[n]:
        count += 1
        total += lst[n]
print(count)

# use division and modulo for faster operation