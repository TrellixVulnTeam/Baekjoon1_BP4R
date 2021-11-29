n = int(input())
if n <= 99:
    count = n
else:
    count = 99
    for num in range(100, n + 1):
        if int(str(num)[0])+int(str(num)[2]) == 2*int(str(num)[1]):
            count += 1
print(count)
