n = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = 0
for i in range(0, n):
    for j in range(0, n):
        answer += abs(lst[i] - lst[j])
    
print(answer)