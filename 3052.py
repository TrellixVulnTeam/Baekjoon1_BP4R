lst = []
for n in range(1,11):
    inp = int(input())
    lst.append(inp%42)

print(len(set(lst)))