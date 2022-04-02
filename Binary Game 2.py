n = int(input())
lst = []
answer = ''
for num in range(0, n + 1):
    lst.append(bin(num)[2:])
for a in lst:
    for b in a:
        answer += b
print(answer)