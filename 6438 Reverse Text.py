t = int(input())
for _ in range(t):
    sentence = input()
    lst = []
    answer = []
    for s in sentence:
        lst.append(s)
    for n in range(len(lst) - 1, -1, -1):
        answer.append(lst[n])
    print("".join(answer))