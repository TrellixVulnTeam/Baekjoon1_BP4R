N = int(input())
lst = list(map(float, input().split(" ")))

answer = len(lst)

def get_average(l):
    return sum(l)/len(l)

for n in range(0, N - 1):
    for num in range(n + 2, N + 1):
        if get_average(lst[n:num]) in lst[n:num]:
            answer += 1
            continue

print(answer)