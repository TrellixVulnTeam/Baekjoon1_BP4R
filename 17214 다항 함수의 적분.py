expression = input()
if expression == '0':
    print('W')
    quit()
lst = expression.split("x")

if '+' in expression or '-' in expression and expression.index('-') != 0 or expression.count('-') >= 2:
    lst[0] = str(int(lst[0])//2)
    
    if lst[1] == '+1' or lst[1] == '-1':
        lst[1] = lst[1][:1]
    lst.insert(1, 'xx')
    lst.append('x')
    lst.append('+W')
    if lst[0] == '1':
        lst.pop(0)
    if lst[0] == '-1':
        lst.pop(0)
        lst.insert(0, '-')

else:
    if len(lst) < 2:
        if lst[0] == '1':
            lst.pop(0)
        elif lst[0] == '-1':
            lst.pop()
            lst.append('-')
        lst.append('x')
    else:
        lst[0] = str(int(lst[0])//2)
        if lst[0] == '1':
            lst.pop(0)
        if lst[0] == '-1':
            lst.pop(0)
            lst.insert(0, '-')
        lst.insert(1, 'xx')

    lst.append('+W')
    
print("".join(lst))