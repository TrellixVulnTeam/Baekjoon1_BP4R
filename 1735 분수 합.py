def gcd(a, b):
    if a == b or a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd(max(a, b) % min(a, b), min(a, b))

A, B = map(int, input().split())
C, D = map(int, input().split())


numerator = A * D + C * B
denominator = B * D
num = gcd(numerator, denominator)
print(numerator // num, denominator // num)