A = int(input())
B = int(input())
C = int(input())
if A + B + C != 180:
    print("Error")
    quit()
elif A == B == C == 60:
    print("Equilateral")
elif A == B or B == C or A == C:
    print("Isosceles")
else:
    print("Scalene")