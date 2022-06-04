N = int(input())
answer = 0
for n in range(1, N + 1): 
    for s in str(n):
        if s == '3' or s == '6' or s == '9':
            answer += 1
print(answer)