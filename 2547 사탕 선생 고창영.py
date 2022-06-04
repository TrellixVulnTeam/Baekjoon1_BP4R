N = int(input())
for _ in range(N):
    boolean = False
    s = 0
    i = input()
    n = int(input())
    for num in range(n):
        s += int(input())
    if s % n == 0:
        boolean = True
    if boolean:
        print("YES")
    else:
        print("NO")