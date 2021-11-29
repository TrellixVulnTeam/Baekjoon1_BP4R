x = int(input())
import math
for n in range(0,x):
    inp = input()
    inpsplit = inp.split(" ")
    fx = int(inpsplit[0])
    fy = int(inpsplit[1])
    fr = int(inpsplit[2])
    sx = int(inpsplit[3])
    sy = int(inpsplit[4])
    sr = int(inpsplit[5])
    distance = math.sqrt((fx - sx)**2 + (fy - sy)**2)
    if distance == 0 and fr == sr:
        print(-1)
        continue
    if abs(fr + sr) < distance or abs(fr - sr) > distance:
        print(0)
        continue
    if abs(fr + sr) == distance or abs(fr - sr) == distance:
        print(1)
        continue
    if abs(fr - sr) < distance < abs(fr + sr):
        print(2)
        continue





