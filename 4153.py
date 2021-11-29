while True:
    sides = input().split(" ")
    if sides[0] == '0':
        quit()
    nsides = []
    for n in sides:
        nsides.append(int(n))
    sortedsides = sorted(nsides, reverse = True)

    if sortedsides[0]**2 == sortedsides[1]**2 + sortedsides[2]**2:
        print("right")
    else:
        print("wrong")
