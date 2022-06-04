a, b, c = input().split()
lst = [a, b, c]
index = 0
if lst.count('1') == 3:
    print("*")
    quit()
elif lst.count('1') == 2:
    index = lst.index('0')
elif lst.count('0') == 2:
    index = lst.index('1')
else:
    print("*")
    quit()

if index == 0:
    print("A")
elif index == 1:
    print("B")
else:
    print("C")