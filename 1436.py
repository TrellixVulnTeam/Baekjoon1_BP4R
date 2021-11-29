N = int(input())
lst = []
n = 0
while True:
    if len(lst) == N:
        print(lst[-1])
        break
    if str(n).find('666') != -1:
        lst.append(n)
    n += 1