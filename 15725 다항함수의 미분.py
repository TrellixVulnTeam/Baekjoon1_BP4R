expression = input()
lst = expression.split('x')
if 'x' not in expression:
    print(0)
    quit()
if expression[0] == 'x':
    print(1)
    quit()
if expression[0:2] == '-x':
    print(-1)
    quit()
print(lst[0])