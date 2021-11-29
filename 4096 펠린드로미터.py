while True:
    inp = int(input())
    rev = ''
    if inp == 0:
        quit()
    while True:
        s = 0
        for n in range(len(str(inp)) - 1, -1, -1):
            rev += str(inp)[n]
        if str(inp) == rev:
            print(s)
            break
        else:
            s += 1
            n += 1