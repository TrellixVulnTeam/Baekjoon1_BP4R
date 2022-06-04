N = int(input())
answer = 0
for n in range(N):
    word = input()
    lst = []
    for w in word:
        if len(lst) == 0:
            lst.append(w)
        elif w == lst[-1]:
            lst.pop()
        else:
            lst.append(w)

    if len(lst) == 0:
        answer += 1

print(answer)
    

