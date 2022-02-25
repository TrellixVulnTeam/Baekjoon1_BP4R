A = 100
B = 100
N = int(input())
for _ in range(N):
    one, two = map(int, input().split())
    if two > one:
        A -= two
    elif one > two:
        B -= one

print(A)
print(B)