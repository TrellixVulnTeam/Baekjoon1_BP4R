N = input()
st = (n for n in N)

sortedst = sorted(st, reverse = True)
print("".join(sortedst))