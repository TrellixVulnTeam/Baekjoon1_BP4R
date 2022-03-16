n = int(input())
answer = 4
for a in range(int(n**0.5), int((n//4)**0.5), -1):
    if a**2 == n:
        answer = 1
        break
    else:
        temp = n - a**2
        for b in range(int(temp**0.5), int((temp//3)**0.5), -1):
            if a**2 + b**2 == n:
                answer = min(answer, 2)
                continue
            else:
                temp = n - a**2 - b**2
                for c in range(int(temp**0.5), int((temp//2)**0.5), -1):
                    if n == a**2 + b**2 + c**2:
                        answer = min(answer, 3)
print(answer)