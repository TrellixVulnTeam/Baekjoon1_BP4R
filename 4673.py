def d(n):
    for x in str(n):
        new = n + int(x)
    while True:
        d(new)
    if new > 10000:
        False

d(27)



#if d(n) is not in the list of the complete set of d(n), append it to a list

