n = int(input())
lst = []
for n in range(n):
    inp = input()
    inpsplit = inp.split(" ")
    A = int(inpsplit[0])
    B = int(inpsplit[1])
    lst.append((A,B))
l = []
tup = (x for x in lst)
sortedtup = sorted(tup)
for pair in sortedtup:
    print(pair[0], pair[1])










