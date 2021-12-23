while True:
    line = input()
    answer = 0
    if line == '#':
        quit()
    lst = line.split()
    for i in range(0, len(lst)):
        lst[i] = lst[i].lower()
    for j in range(1, len(lst)):
        answer += lst[j].count(lst[0])
    print(lst[0], answer)