N = int(input())
lst = sorted(list(map(int, input().split(" "))))
M = int(input())
lst1 = list(map(int, input().split(" ")))


def bs(l, a):
    maximum = len(l) - 1
    minimum = 0
    while True:
        if a > l[maximum]:
            print(0)
            break
        if a < l[minimum]:
            print(0)
            break
        ind = (maximum + minimum)//2
        if l[ind] == a:
            print(1)
            break
        if minimum == maximum:
            print(0)
            break
        if l[ind] < a:
            minimum = ind + 1
        if l[ind] > a:
            maximum = ind - 1


for n in lst1:
    bs(lst, n)

