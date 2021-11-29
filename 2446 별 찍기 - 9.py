N = int(input())
lst = []
for n in range(0, N):
    string = ' ' * n + '*' * (N * 2 - (2 * n + 1))
    lst.append(string)
    print(string)
    
for l in range(len(lst) - 2, -1, -1):
    print(lst[l])