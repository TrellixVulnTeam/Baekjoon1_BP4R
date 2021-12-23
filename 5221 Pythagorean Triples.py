import sys
from itertools import combinations
t = int(sys.stdin.readline().strip())
for _ in range(t):
    answer = ''
    lst = []
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    numbers.pop(0)
    for l in list(combinations(numbers, 3)):
        if pow([0], 2) + pow(l[1], 2) == pow(l[2], 2):
            lst.append(set(l))
    print(lst)
