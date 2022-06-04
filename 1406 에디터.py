import sys
from collections import deque
word = input()
lst = list(word)
cursor = len(lst)
N = int(sys.stdin.readline().strip())
for n in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd[0] == "P":
        lst.insert(cursor, cmd[-1])
        cursor += 1
    if cmd[0] == "L":
        if cursor != 0:
            cursor -= 1
    if cmd[0] == "D":
        if cursor != len(lst):
            cursor += 1