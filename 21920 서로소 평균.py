N = int(input())
lst = list(map(int, input().split()))
X = int(input())

def gcd(a, b):
    if a == 0 or b == 0 or a == b:
        return max(a, b)
    else:
        return gcd(min(a, b), max(a, b) % min(a, b))

other = []
for l in lst:
    if gcd(X, l) == 1:
        other.append(l)
print(sum(other) / len(other))