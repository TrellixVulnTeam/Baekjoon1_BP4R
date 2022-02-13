x = int(input())
count = 1
s = 2

while x > count:
    x -= count
    count += 1
    s += 1
if s % 2 == 0:
    print(f"{s-x}/{x}")
else:
    print(f"{x}/{s-x}")

