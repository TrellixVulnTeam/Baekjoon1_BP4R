N = int(input())
threecount = 0
fivecount = 0
while True:
    if N % 5 == 0:
        break
    if N < 0:
        print(-1)
        quit()
    N -= 3
    threecount += 1
fivecount += (N//5)
print(fivecount + threecount)


