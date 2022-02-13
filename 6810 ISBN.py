s = 91
for _ in range(3):
    n = int(input())
    if _ == 0:
        s += n
    elif _ == 1:
        s += n * 3
    elif _ == 2:
        s += n
print(f"The 1-3-sum is {s}")