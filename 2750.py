lst = []
N = int(input())
for _ in range (0,N):
    inp = int(input())
    lst.append(inp)
for n in sorted(lst):
    print(n)