while True:
    word = input()
    if word == "0":
        quit()
    rev = ''
    for n in range(len(word) -1, -1, -1):
        rev += word[n]

    if rev == word:
        print("yes")
    else:
        print("no")
