N = int(input())
lst = input().split(" ")
lst = sorted(lst)
M = int(input())
lst2 = input().split(" ")
for num in lst2:
    if num in lst:
        print("1")
    else:
        print("0")
