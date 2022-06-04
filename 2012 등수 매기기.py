import sys
N = int(sys.stdin.readline().strip())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))

lst.sort(reverse=True)
answer = 0
rank = N
for i in lst:
    answer += abs(N - i)
    N -= 1

print(answer)