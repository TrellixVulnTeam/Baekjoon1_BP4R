N = int(input())
answer = [[1, 3], [1, 4], [3, 4]]
lst = []
for _ in range(N):
    f, s = map(int, input().split())
    lst.append(sorted((f, s)))
lst.sort()


if answer == lst:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")
    