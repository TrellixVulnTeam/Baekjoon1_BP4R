lst = [x for x in input()]
time = 0
for n in lst:
    if n == 'A' or n == 'B' or n == 'C':
        time += 3
    if n == 'D' or n == 'E' or n == 'F':
        time += 4
    if n == 'G' or n == 'H' or n == 'I':
        time += 5
    if n == 'J' or n == 'K' or n == 'L':
        time += 6
    if n == 'M' or n == 'N' or n == 'O':
        time += 7
    if n == 'P' or n == 'Q' or n == 'R' or n == 'S':
        time += 8
    if n == 'T' or n == 'U' or n == 'V':
        time += 9
    if n == 'W' or n == 'X' or n == 'Y' or n == 'Z':
        time += 10
print(time)