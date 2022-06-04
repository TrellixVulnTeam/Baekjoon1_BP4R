from itertools import permutations
n = int(input())
lst = [x for x in range(1, n + 1)]
answer = []
answer.append(list(permutations(lst, n)))
for l in answer:
    for li in l:
        for e in li:
            print(e, end = ' ')
        print()