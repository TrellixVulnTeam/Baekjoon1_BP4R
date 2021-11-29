S = input()
alphabets = []
for n in 'abcdefghijklmnopqrstuvwxyz':
    alphabets.append(n)
lst = []
for w in alphabets:
    if w in S:
        lst.append(str(S.index(w)))
    else:
        lst.append(str(-1))
print((" ").join(lst))