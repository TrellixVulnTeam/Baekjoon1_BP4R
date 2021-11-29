x = int(input())
for _ in range(1, x+1):
    count = 0
    c = 0
    mean = 0
    lst = input().split(" ")
    for n in lst[1:]:
        c += int(n)
        mean = c / int(lst[0])
    for n in lst[1:]:
        if int(n) > mean:
            count += 1


    per = count/int(lst[0]) * 100
    index = str(per).index(".")
    if per*10000%10 >= 5:
        per += 0.001
    if per*10000%10 == 0:
        print(str(per)[0:index + 4] + "00%")
    else:
        print(str(per)[0:index + 4] + "%")


