exp = input()
lst = []
maximum = 0
for w in exp:
    lst.append(w)
for n in range(len(exp)):
    for num in range(n + 1, len(exp)):
        try:
            