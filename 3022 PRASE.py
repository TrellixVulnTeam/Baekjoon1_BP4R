N = int(input())

d = {}
warnings = 0

for _ in range(N):
    kid = input()
    if kid in d:

        if d[kid] * 2 > sum(d.values()):
            warnings += 1
        d[kid] += 1
    else:
        d[kid] = 1
print(warnings)