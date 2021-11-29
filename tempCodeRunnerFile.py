N = int(input())
if N == 1:
    print(1)
    quit()

for m in range(2, int(pow(10000000, 0.5) + 1)):
    while True:
        if N%m == 0:
            N = N // m
            print(m)
        else:
            break