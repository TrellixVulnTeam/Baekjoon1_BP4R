import sys
n, m = map(int, sys.stdin.readline().split())
number = 1
d = {}
for _ in range(n):
    pokemon = sys.stdin.readline().strip()
    d[number] = pokemon
    number += 1
nd = {}
for k, v in d.items():
    nd[v] = k

for t in range(m):
    prob = sys.stdin.readline().strip()
    if prob.isnumeric():
        print(d[int(prob)])
    else:
        print(nd[prob])
