word = input()
lst = []
index = 0
while index < len(word):
    lst.append(word[index:])
    index += 1
lst.sort()
for l in lst:
    print(l)

