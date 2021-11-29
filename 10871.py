inp = input().split(" ")
N = inp[0]
X = int(inp[1])
lst = input().split(" ")
l = []
for n in lst:
    if int(n) < X:
        l.append(n)
print((" ").join(l))