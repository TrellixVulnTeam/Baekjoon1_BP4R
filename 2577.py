x = int(input())
y = int(input())
z = int(input())
num = x*y*z
for n in range(0,10):
    count = 0
    for number in range(0, len(str(num))):
        if str(n) == str(num)[number]:
            count += 1
    print(count)
