while True:
    lst = []
    b = True
    string = input()
    if string == '.':
        break
    for s in string:
        if s == '(' or s == '[':
            lst.append(s)
        if s == ')':
            try:
                if lst[-1] == '[':
                    b = False
                    break
                
                lst.pop()
            except IndexError:
                b = False
        if s == ']':
            try:
                if lst[-1] == '(':
                    b = False
                    break
                lst.pop()
            except IndexError:
                b = False 
    if b == True and len(lst) == 0:
        print("yes")
    else:
        print("no")
