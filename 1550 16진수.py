N = input()
number = 0
index = len(N) - 1
for n in N:
    if n == 'A':
        number += 10* 16**index
        index -= 1
        continue
    if n == 'B':
        number += 11 * 16**index
        index -= 1
        continue
    if n == 'C':
        number += 12 * 16**index
        index -= 1
        continue
    if n == 'D':
        number += 13 * 16**index
        index -= 1
        continue
    if n == 'E':
        number += 14 * 16**index
        index -= 1
        continue
    if n == 'F':
        number += 15 * 16**index
        index -= 1
        continue
    else:
        number += int(n) * 16 ** index
        index -= 1
        continue

print(int(number))