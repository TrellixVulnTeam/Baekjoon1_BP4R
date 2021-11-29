N = int(input())
if N == 1:
    quit()
count = 0
m = 2
while True:
    if m > N:
        quit()
    if N%m == 0:
        N = N / m
        print(m)
    else:
        if count == 0:
            m += 1
            count += 1
        else:
            m += 2

            
