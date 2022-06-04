def gcd(a, b):
    if a == 0 or b == 0 or a == b:
        return max(a, b)
    else:
        return gcd(min(a, b), max(a, b) % min(a, b))


exp = input()
lst = exp.split(":")
a = lst[0]
b = lst[1]
num = gcd(int(a), int(b))
print(f"{int(a)//num}:{int(b)//num}")