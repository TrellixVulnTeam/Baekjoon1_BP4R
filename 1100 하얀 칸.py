answer = 0
for n in range(0, 8):
    row = input()
    lst = list(row)
    if n % 2 == 0:
        for i in range(0, 8, 2):
            if lst[i] == 'F':
                answer += 1
    else:
        for j in range(1, 8, 2):
            if lst[j] == 'F':
                answer += 1
print(answer)