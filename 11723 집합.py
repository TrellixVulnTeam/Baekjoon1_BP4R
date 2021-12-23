import sys
t = int(sys.stdin.readline().strip())
lst = [0] * 21
for _ in range(t):
    line = sys.stdin.readline().strip()
    try:
        inp, x = line.split()
        if inp == 'add':
            lst[int(x)] = 1
        if inp == 'remove':
            lst[int(x)] = 0
        if inp == 'check':
            if lst[int(x)] == 1:
                print(1)
            else:
                print(0)
        if inp == 'toggle':
            if lst[int(x)] == 0:
                lst[int(x)] = 1
            else:
                lst[int(x)] = 0
    except:
        if line == 'all':
            lst = [1] * 21
        if line == 'empty':
            lst = [0] * 21
