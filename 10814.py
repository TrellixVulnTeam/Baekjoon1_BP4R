N = int(input())
lst = []
for _ in range(0, N):
    age, name = input().split()
    lst.append((int(age), _, name))
sortedlst = sorted(lst)
for a, b, c in sortedlst:
    print(a, c)

