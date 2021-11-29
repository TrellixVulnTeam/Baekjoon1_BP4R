k = int(input())
lst = []
code = input()
answer = ''
for a in code:
    lst.append(a)

for n in range(0, len(lst), k):
    answer += lst[n]

print(answer)