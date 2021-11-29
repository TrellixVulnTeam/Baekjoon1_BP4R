import sys
def gcd(a, b):
    if min(a, b) == 0 or a == b:
        return max(a,b)
    return gcd(min(a, b),max(a,b)%min(a,b))
a, b = map(int, sys.stdin.readline().split())
print(a*b // gcd(a, b))