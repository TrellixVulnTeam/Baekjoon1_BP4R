import math

A, B, V = map(int, input().split())
h = A - B

print(math.ceil((V - B) / (A - B)))

