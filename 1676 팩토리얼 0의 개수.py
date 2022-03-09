N = int(input())
count = 0
while N != 0:
    i = N // 5
    N = i
    count += i
print(count)