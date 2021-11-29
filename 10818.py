x = int(input())
lst = input().split(" ")
list = []
for n in lst:
    list.append(int(n))
print(min(list), max(list))