time = input().split(" ")
hr = int(time[0])
min = int(time[1])

if min >= 45:
    print (hr , min-45)

elif min < 45:
    if hr == 0:
        print (23 , 60 - (45-min))
    else:
        print(hr - 1, 60 - (45 - min))
