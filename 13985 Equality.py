expression = input()
lst = expression.split()
lst.pop(lst.index("+"))
lst.pop(lst.index('='))
if int(lst[0]) + int(lst[1]) == int(lst[2]):
    print("YES")
else:
    print("NO")