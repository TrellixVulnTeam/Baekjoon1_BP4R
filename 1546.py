x = int(input())
m = 0
score = input().split(" ")
for n in score:
    if int(n) > m:
        m = int(n)
    else:
        continue
lst = []
for num in score:
    lst.append(int(num)/m*100)
print(sum(lst)/x)


