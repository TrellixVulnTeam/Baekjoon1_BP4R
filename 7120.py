word = input()
lst = []
if len(word) == 1:
    print(word)
    quit()
for n in range(1, len(word)):
    if n == 1:
        lst.append(word[0])
    if word[n] != word[n-1]:
        lst.append(word[n])
    else:
        continue
print("".join(lst))
