import sys

N = int(sys.stdin.readline().strip())
lst = []
answer = 1
for _ in range(N):
    A, B = map(int, sys.stdin.readline().strip().split())
    lst.append((A, B))

lst.sort(key= lambda x: x[1])
current = lst[0][1]

for l in lst:
    if l[0] >= current:
        answer += 1
        current = l[1]

print(answer)