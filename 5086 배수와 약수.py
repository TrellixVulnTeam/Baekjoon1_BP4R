while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    if b % a == 0:
        print('factor')
        continue
    if a % b == 0:
        print('multiple')
        continue
    else:
        print('neither')
        continue

