k = int(input())
com = 25 + k * 0.01
if com < 100:
    com = 100
elif com > 2000:
    com = 2000

print(format(com, ".2f"))