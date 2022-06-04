var = input()
if var[0] == var[0].upper() or var[0] == '_':
    print("Error!")
    quit()
cpp = False
java = False
lst = []
prev = 0
for i in range(0, len(var)):
    if var[i] == var[i].upper() and var[i] != "_":
        lst.append(var[prev: i])
        prev = i
        java = True
    elif i == len(var) - 1:
        lst.append(var[prev:])

    elif var[i] == '_':
        lst.append(var[prev:i])
        prev = i + 1
        cpp = True

        
if cpp and java:
    print("Error!")
elif cpp:
    for j in range(0, len(lst)):
        try:
            lst[j] = lst[j][0].upper() + lst[j][1:]
        except:
            lst[j] = lst[j][0].upper()
    print("".join(lst))
elif java:
    name = ""
    for k in range(0, len(lst) - 1):
        name += lst[k].lower()
        name += '_'
    name += lst[-1].lower()
    print(name)