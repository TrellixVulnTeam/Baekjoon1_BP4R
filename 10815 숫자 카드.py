N = int(input())
cards = set(map(int, input().split(" ")))
M = int(input())
lst = list(map(int, input().split(" ")))

for n in lst:
    if n in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
