N = int(input())
count = N - 1
second_count = 1
for n in range(N):
    print(' ' * count + '*' * (2 * (N - count) - 1))
    count -= 1
for a in range(N):
    print(' ' * second_count + '*' * (2 * (N - second_count) - 1))
    second_count += 1

    