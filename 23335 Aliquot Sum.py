T = int(input())
number_lst = list(map(int, input().split()))
for n in number_lst:
    if n != 1:
        s = 1
        boolean = True
        for num in range(2, int(n**0.5) + 1):
            if n % num == 0:
                s += num
                if num != n//num:
                    s += n // num
                if s > n:
                    print("abundant")
                    boolean = False
                    break
        if boolean:
            if s == n:
                print("perfect")
            elif s < n:
                print("deficient")
    print("perfect")