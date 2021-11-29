T = int(input())
for t in range(0, T):
    maximum = 0
    n = int(input())
    lst = list(map(int, input().split()))
    for index in range(0, len(lst)):
        for i in range(index+1, len(lst)+1):
            sigma = sum(lst[index:i])
            if maximum == 0:
                maximum = sigma
            elif maximum < sigma:
                maximum = sigma
    print(maximum)
