N = int(input())
lst = [1, 1]
for n in range(2, N):
    lst.append(lst[n-1] + lst[n-2])
print(lst[-1])
