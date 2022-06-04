while True:
    b = False
    speed, weight, strength = map(float, input().split())
    if speed == 0 and weight == 0 and strength == 0:
        quit()
    if speed <= 4.5 and weight >= 150 and strength >= 200:
        print("Wide Receiver", end = ' ')
        b = True
    if speed <= 6.0 and weight >= 300 and strength >= 500:
        print("Lineman", end=  ' ')
        b = True
    if speed <= 5.0 and weight >= 200 and strength >= 300:
        print("Quarterback", end = ' ')
        b = True
    if not b :
        print("No positions", end= ' ')
    print()