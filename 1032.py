x = int(input())
lst = []
for _ in range(1,x+1):
    dir = input()
    lst.append(dir)

length = len(lst[0])
com = []
comp = []
for d in lst:
    for n in range(0, len(d)):
        if len(com) < length:
            com.append(d[n])
        else:
            if com[n] != d[n]:
                com[n] = "?"
print(("").join(com))




