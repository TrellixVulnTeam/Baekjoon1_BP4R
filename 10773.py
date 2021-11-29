k = int(input())
lst = []
for n in range(0, k):
    inp = int(input())
    if inp == 0:
        lst.pop()
    else:
        lst.append(inp)
print(sum(lst))
