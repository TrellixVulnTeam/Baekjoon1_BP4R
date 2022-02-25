import sys
lst = []
while True:
    sentence = sys.stdin.readline().strip()
    if sentence == '#':
        break
    count = 0
    for s in sentence.lower():
        if s == 'a' or s == 'e' or s =='i' or s == 'o' or s =='u':
            count += 1
    lst.append(count)
for l in lst:
    print(l)
