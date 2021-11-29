word = input()
if "".join(reversed(word)) == word:
    print(1)
else:
    print(0)