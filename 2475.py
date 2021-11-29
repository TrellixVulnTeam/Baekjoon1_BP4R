inp = input().split(" ")
count = 0
for n in inp:
    count += int(n)**2
print(count%10)