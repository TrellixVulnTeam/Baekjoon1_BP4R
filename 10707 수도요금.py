A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
X = A * P
Y = 0
if P >= C:
    Y += D * (P - C) + B
else:
    Y = B
print(min(X, Y))