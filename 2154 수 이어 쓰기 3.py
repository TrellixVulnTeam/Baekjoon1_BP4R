N = int(input())
w = ""
for n in range(1, N + 1):
    w += str(n)

print(w.index(str(N)) + 1)