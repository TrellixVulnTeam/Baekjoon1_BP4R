N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = 0
count = 0
while count < K:
    answer += lst[len(lst) - count - 1] - count
    count += 1

print(answer)