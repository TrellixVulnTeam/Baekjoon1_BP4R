import sys
cands = set((n for n in range(1, 10001)))
delete = []
def d(n):
    s = 0
    for c in str(n):
        s += int(c)
    nu = n + s
    delete.append(nu)
for number in range(1, 10001):
    d(number)
for a in cands:
    if a not in set(delete):
        sys.stdout.write(str(a) + '\n')
