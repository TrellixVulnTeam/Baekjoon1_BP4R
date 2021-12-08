N = int(input())
d = {}
answer = 0
heights = list(map(int, input().split()))
limits = list(map(int, input().split()))
heights.sort(reverse=True)
limits.sort(reverse=True)
for h in heights:
    temp = N
    for l in limits:
        if h > l:
            temp -= 1
    d[h] = temp
minus = 1
answer += d[heights[0]]
for height in range(1, N):
    answer = answer * (d[heights[height]] - minus)
    minus += 1
print(answer)



