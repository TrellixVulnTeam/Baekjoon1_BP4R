def gcd(a, b):
    if a == b or a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd(max(a, b) % min(a, b), min(a, b))


N = int(input())
lst = list(map(int, input().split()))
st = lst[0]
lst.pop(0)
for l in lst:
    print(str(st // gcd(st, l)) + '/' + str(l // gcd(st, l)))
