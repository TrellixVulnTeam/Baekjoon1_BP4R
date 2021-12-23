import sys
V = int(sys.stdin.readline().strip())
E = int(sys.stdin.readline().strip())
lst = [[] for z in range(V + 1)]
for _ in range(E):
    n, m = map(int, sys.stdin.readline().strip().split())
    lst[n].append(m)
    lst[m].append(n)
answer = 0
# print(lst)
visited = []
not_visited = [1]
while not_visited:
    # print(not_visited)
    node = not_visited.pop()
    # print(node)
    if node in visited:
        continue
    else:
        not_visited.extend(lst[node])
        visited.append(node)
        answer += 1
# print(visited)
print(answer - 1)