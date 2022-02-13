N = int(input())
s = 0
inc = 1
answer = 0
while s < N:
    s += inc
    inc += 1
    answer += 1
if s == N:
    print(answer)
else:
    print(answer - 1)
    