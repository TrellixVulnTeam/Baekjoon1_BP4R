inp = input().split(" ")
A = int(inp[0])
B = int(inp[1])
C = int(inp[2])
if B>=C:
    print(-1)
else:
    print(A // (C-B) + 1)