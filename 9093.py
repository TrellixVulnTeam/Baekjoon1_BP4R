x = int(input())
for _ in range(x):
    inp = input().split()
    for word in inp:
        lst = []
        for i in range(len(word) -1, -1, -1):
            reversed = ''
            reversed += word[i]
            lst.append(reversed)


