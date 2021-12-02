N = int(input())
count = 0
for n in range(1, N+1):
    if count % 2 == 0:
        print(N * '* ' , end='\n')
    else:
        print(' ' + N * '* ', end='\n')
    count += 1