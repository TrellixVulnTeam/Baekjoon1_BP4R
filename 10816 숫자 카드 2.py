n = int(input())
cards = list(map(int, input().split(" ")))
N = int(input())
lst = list(map(int, input().split(" ")))

d = {}
for num in cards:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1
keys = list(d.keys())
keys = sorted(keys)


def bs(l, a, d):
    maximum = len(l) - 1
    minimum = 0
    while True:
        if a > l[maximum]:
            print('0' ,end = ' ')
            break
        if a < l[minimum]:
            print('0', end= ' ')
            break
        ind = (maximum + minimum)//2
        if l[ind] == a:
            print(d[a], end = ' ')
            break
        if minimum == maximum:
            print('0', end=' ')
            break
        if l[ind] < a:
            minimum = ind + 1
        if l[ind] > a:
            maximum = ind - 1


for number in lst:
    bs(keys, number, d)
