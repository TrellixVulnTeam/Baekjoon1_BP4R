N = int(input())
d = {}
maximum = 0
for _ in range(0,N):
    word = input()
    if maximum < len(word):
        maximum = len(word)
    if len(word) not in d:
        d[len(word)] = [word]
    elif len(word) in d and word in d[len(word)]:
        continue
    else:
        d[len(word)].append(word)
for k, v in sorted(d.items()):
    d[k] = sorted(v)
dsorted = sorted(d.items())
for x, y in dsorted:
    for n in y:
        print (n)
