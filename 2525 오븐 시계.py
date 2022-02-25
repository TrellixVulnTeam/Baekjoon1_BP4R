H, M = map(int, input().split())
add = int(input())
H += (add + M) // 60
M = (add + M) % 60
print(H%24, M)