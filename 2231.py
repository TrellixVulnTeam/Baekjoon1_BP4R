N = int(input())
maximum = []
for n in range(0, N + 1):
    s = 0
    for w in str(n):
        s += int(w)
    if n + s == N:
        maximum.append(n)
if len(maximum) == 0:
    print(0)
    quit()
print(min(maximum))
