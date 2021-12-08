t1 = int(input())
t2 = int(input())
lst = [t1, t2]
index = 1
while True:
    if lst[index - 1] - lst[index] >= 0: 
        lst.append(lst[index - 1] - lst[index])
        index += 1
    else:
        break
print(len(lst))