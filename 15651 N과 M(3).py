from itertools import combinations_with_replacement
lst = []
N, M = map(int, input().split())
for n in range(1, N+1):
    lst.append(str(n))

for l in list(combinations_with_replacement(lst, M)):
    for a in l:
        print(a, end = ' ')
    print('\n')
