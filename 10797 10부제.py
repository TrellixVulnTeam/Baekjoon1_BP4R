n = int(input())
lst = list(map(int, input().split()))
count = 0
for l in lst:
    if l == n:
        count += 1
print(count)