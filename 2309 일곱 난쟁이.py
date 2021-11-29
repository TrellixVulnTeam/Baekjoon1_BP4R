from itertools import combinations
lst = []
answer = []
for _ in range(0,9):
    lst.append(int(input()))
for l in combinations(lst, 7):
    if sum(l) == 100:
        answer.append(l)
        break
for n in sorted(answer[0]):
    print(n)
