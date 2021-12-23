import sys
N = int(sys.stdin.readline())
years = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
d = {}
for _ in range(N):
    phrase = sys.stdin.readline().strip().split()
    d[phrase[-1]] = 0
    if phrase[3] == 'previous':
        for j in range(years.index(phrase[]))