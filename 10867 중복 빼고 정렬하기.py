n = int(input())
lst = (list(map(int, input().split(" "))))
for num in sorted(set(lst)):
    print(num)