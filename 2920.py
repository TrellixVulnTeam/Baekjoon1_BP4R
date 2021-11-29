whole = input().split(" ")
acount = 0
dcount = 0
for n in whole:

    try:
        if int(whole[whole.index(n)]) + 1 == int(whole[whole.index(n)+1]):
            acount += 1
        if int(whole[whole.index(n)]) - 1 == int(whole[whole.index(n)+1]):
            dcount += 1
        else:
            continue

    except IndexError:
        break

if acount == 7:
    print('ascending')
elif dcount == 7:
    print('descending')
else:
    print('mixed')
