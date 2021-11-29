x = input()
inp = input().split(" ")
count = 0
for n in inp:
    factors = []
    if int(n) == 1:
        continue
    for num in range(1,int(n)+1):
        if int(n)%num == 0:
            factors.append(num)
    if len(factors) <= 2:
        count += 1
    else:
        continue
print(count)





