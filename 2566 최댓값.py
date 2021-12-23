lst = []
maximum = 0
maximum_x = 0
maximum_y = 0
for x in range(9):
    l = list(map(int, input().split()))
    lst.append(l)
for i in range(9):
    for j in range(9):
        if lst[i][j] > maximum:
            maximum = lst[i][j]
            maximum_x = j + 1
            maximum_y = i + 1
            
print(maximum)
print(maximum_y, maximum_x)