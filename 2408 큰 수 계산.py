N = int(input())
count = 0
lst = []
while True:
    if count == 2*N - 1:
        break
    inp = input()
    if inp == '/':
        lst.append('//')
    else:
        lst.append(inp)
    count += 1
print((eval("".join(lst))))