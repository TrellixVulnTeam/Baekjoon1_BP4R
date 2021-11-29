M = int(input())
N = int(input())
primesum = 0
minprime = 0
mincount = 0
for n in range(M, N+ 1):
    if n == 1:
        continue
    count = 0
    for num in range(1, n+ 1):
        if n%num == 0:
            count += 1
    if count <= 2:
        primesum += n
        if mincount == 0:
            mincount += 1
            minprime = n
if mincount == 0:
    print(-1)
    quit()
print(primesum)
print(minprime)


