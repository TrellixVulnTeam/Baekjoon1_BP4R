A, B = input().split()
answer = 0
for a in str(A):
    for b in str(B):
        answer += eval (a + "*" + b)
print(answer)