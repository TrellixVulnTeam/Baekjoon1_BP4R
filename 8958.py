n = int(input())
for _ in range (1,n+1):
    score = 1
    total = 0
    inp = input()
    lst = []
    for char in inp:
        lst.append(char)
    for a in lst:
        if a == 'O':
            total += score
            score += 1
        if a == 'X':
            score = 1
    print(total)
