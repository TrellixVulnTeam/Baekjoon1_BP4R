N = int(input())
for n in range(N):
    b = True
    word = input().lower()
    for l in range(len(word)):
        if word[l] != word[len(word) - 1 - l]:
            b = False
    if b:
        print("Yes")
    else:
        print("No")

