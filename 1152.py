word = input().strip()
lst = word.split(" ")
if lst[0] == '':
    print(0)
else:
    print(len(lst))