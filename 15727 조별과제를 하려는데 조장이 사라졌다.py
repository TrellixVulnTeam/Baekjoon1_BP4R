distance = int(input())
minute = 0 
while True:
    if distance > 5:
        minute += 1
        distance = distance - 5
    else:
        minute += 1
        break
print(minute)