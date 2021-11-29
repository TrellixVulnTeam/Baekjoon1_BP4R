word = input()
d = ()
for w in sorted(word):
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
