N = int(input())
for _ in range(N):
    gcount = 0
    bcount = 0
    hero = input()
    for h in hero:
        if h == 'g' or h =='G':
            gcount += 1
        elif h == 'b' or h == 'B':
            bcount += 1
    
    if gcount > bcount:
        print(f"{hero} is GOOD")
    elif gcount == bcount:
        print(f"{hero} is NEUTRAL")
    else:
        print(f"{hero} is A BADDY")