def gcf(a, b):
    if min(a, b) == 0 or a == b:
        g = max(a, b)
        return g
    aprime = max(a, b) % min(a, b)
    return gcf(min(a, b), aprime)


def lcm(a, b):
    return print(a * b // gcf(a, b))


x, y = input().split()
x = int(x)
y = int(y)
print(gcf(x, y))
lcm(x, y)
