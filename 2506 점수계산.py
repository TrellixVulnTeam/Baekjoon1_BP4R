N = int(input())
lst = list(map(int, input().split()))
score = 1
total = 0   
for l in lst:
    if l == 1:
        total += score
        score += 1
    else:
        score = 1
print(total)