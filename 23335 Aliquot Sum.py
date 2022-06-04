T = int(input())
number_lst = list(map(int, input().split()))
for n in number_lst:
    if n == 2:
        print("abundant")
        continue
    
    s = 1
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            s += num
            if num != n//num:
                s += n // num
    if s > n:
            print("abundant")
    elif s == n:
        print("perfect")
    elif s < n:
        print("deficient")





    