inp = []
for x in range (9):
    inp.append(int(input()))
print(max(inp))
print(inp.index(max(inp)) + 1)