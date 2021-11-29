num = int(input())
lst = []
lst.append(1)
lst.append(1)
for n in range(2, num):
    lst.append(lst[n-1] + lst[n-2])
print(lst[num - 1])