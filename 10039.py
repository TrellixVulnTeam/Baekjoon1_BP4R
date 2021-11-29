count = 0
for n in range(0,5):
    inp = int(input())
    if inp <= 40:
        count += 40
    else:
        count += inp
print(count//5)