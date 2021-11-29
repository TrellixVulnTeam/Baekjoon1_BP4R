while True:
    inp = int(input())
    lst = []
    string = ''
    if inp == -1:
        break

    for n in range(1, inp):
        if inp % n == 0:
            lst.append(n)
    if sum(lst) == inp:
        string += str(inp) + ' = '
        for i in range(0, len(lst) - 1):
            string += str(lst[i]) + ' + '
        string += str(lst[-1])
        print(string)

    else:
        print (str(inp) + ' is NOT perfect.')

