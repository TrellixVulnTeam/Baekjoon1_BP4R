from itertools import permutations
import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    word = input()
    lst = list(word)
    for l in sorted(list(set(list(permutations(lst, len(lst)))))):
        print("".join(l))