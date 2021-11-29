N = int(input())
s = 1
add = 0
count = 0
while True:
    s += add
    add += 6
    count += 1
    if N <= s:
        print(count)
        break
