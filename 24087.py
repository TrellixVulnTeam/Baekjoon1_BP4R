S = int(input())
A = int(input())
B = int(input())
check = 250
while A < S:
    A += B
    check += 100
print(check)