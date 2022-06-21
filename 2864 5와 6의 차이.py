A, B = input().split()
maxA = A
minA = A
maxB = B
minB = B
minA = A.replace('6', '5')
maxA = A.replace('5', '6')
minB = B.replace('6', '5')
maxB  = B.replace('5', '6')

print(int(minA) + int(minB), end = ' ')
print(int(maxA) + int(maxB))
