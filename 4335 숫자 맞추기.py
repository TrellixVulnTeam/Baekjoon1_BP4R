import sys
maximum = 10
minimum = 1
while True:
    guess = int(sys.stdin.readline().strip())
    boolean = True
    if guess == 0:
        quit()
    answer = sys.stdin.readline().strip()
    if answer == "too high":
        maximum = min(maximum, guess - 1)
    elif answer == "too low":
        minimum = max(minimum, guess + 1)
    elif answer == "right on":
        if minimum <= guess <= maximum:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        maximum = 10
        minimum = 1
