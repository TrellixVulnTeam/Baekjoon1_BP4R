import sys
N = int(sys.stdin.readline().strip())
X = []
Y = []
ans = 0
a = 0
b = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    X.append(x)
    Y.append(y)
# x > 0, y > 0

for i in range(0, len(X)):
    if X[i] > 0 and Y[i] > 0:
        a += x[i]
        b += y[i]
    else:
        if X[i] > 0 and Y[i] < 0:
            if abs(X[i]) > abs(Y[i]):
                a += X[i]
                b += Y[i]
        if X[i] < 0 and Y[i] > 0:
            if abs(Y[i]) > abs(X[i]):
                a += X[i]
                b += Y[i]
