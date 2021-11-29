n = int(input())
count = 0
if n < 10:
    n = '0' + str(n)
    num = ''
    while True:
        if count == 0:
            num = n[1] + n[1]
            count += 1
            if num == n:
                print(count)
                break
        else:
            add = str(int(num[0]) + int(num[1]))[-1]
            num = num[-1] + add
            count += 1
            if num == n:
                print(count)
                break
else:
    n = str(n)
    num = ''
    while True:
        if count == 0:
            num = n[1] + str(int(n[0]) + int(n[1]))[-1]
            count += 1
            if num == n:
                print(count)
                break
        else:
            add = str(int(num[0]) + int(num[1]))[-1]
            num = num[-1] + add
            count += 1
            if num == n:
                print(count)
                break










