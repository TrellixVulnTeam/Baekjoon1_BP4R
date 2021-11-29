n = int(input())
lst = [int(num) for num in input().split(" ")]

def gcd(a, b):
    if min(a, b) == 0 or a == b:
        return max(a, b)
    return gcd(min(a, b), max(a, b) % min(a, b))


g = gcd(lst[0], lst[1])

if len(lst) == 2:
    for number in range(1, g + 1):
        if gcd(lst[0], lst[1])% number == 0:
            print(number)
else:
    for nu in range(1, gcd(g, lst[2]) + 1):
        if gcd(gcd(lst[0], lst[1]), lst[2])% nu == 0:
            print(nu)


