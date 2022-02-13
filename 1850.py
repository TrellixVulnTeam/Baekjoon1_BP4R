def gcd(a, b):
    if a == b or a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd(max(a, b) % min(a, b), min(a, b))

x, y = map(int, input().split())
for _ in range(gcd(x, y)):
    print("1", end='')