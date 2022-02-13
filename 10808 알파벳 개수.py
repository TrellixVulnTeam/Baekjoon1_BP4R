word = input()
d = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    d[c] = 0
for w in word:
    d[w] += 1
for v in d.values():
    print(v, end=' ')