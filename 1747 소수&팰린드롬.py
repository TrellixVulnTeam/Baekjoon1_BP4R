import math

N = int(input())
if N == 1:
    print(2)
    quit()
lst = [True] * 1003002
for i in range(2, int(math.sqrt(1003002)) + 1):
    if lst[i] == True:
        for j in range(2*i, 1003002, i):
            lst[j] = False
for k in range(N, len(lst)):
    if lst[k] == True and "".join(reversed(str(k))) == str(k):
        print(k)
        break