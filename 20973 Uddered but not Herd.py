alphabet = input()
word = input()
d = {}
c = 0
count = 1
for a in alphabet:
    d[a] = c
    c += 1
for n in range(1, len(word)):
    if d[word[n]] <= d[word[n - 1]]:
        count += 1
print(count)
    