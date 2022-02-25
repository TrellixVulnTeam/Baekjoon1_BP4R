n = int(input())
naturals = []
answer = 0 
for natural in range(n):
    if natural ** 2 <= n:
        naturals.append(natural)
