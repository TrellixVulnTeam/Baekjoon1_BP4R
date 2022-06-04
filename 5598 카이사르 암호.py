word = input()
lst = []
for w in word:
    if w == 'A':
        lst.append('X')
    elif w == 'B':
        lst.append('Y')
    elif w == 'C':
        lst.append('Z')
    else:
        lst.append(chr(ord(w) - 3))
print("".join(lst))