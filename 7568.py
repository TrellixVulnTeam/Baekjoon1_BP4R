N = int(input())
leaderboard = []
lst = []
for n in range(0,N):
    x, y = input().split()
    lst.append((int(x), int(y)))
for w in range(0,N):
    A = lst[w]
    leaderboard.append(1)
    for n in range(0,N):
        if A[0] < lst[n][0] and A[1] < lst[n][1]:
            leaderboard[w] += 1
        else:
            continue
l = []
for num in leaderboard:
    l.append(str(num))
print(" ".join(l))