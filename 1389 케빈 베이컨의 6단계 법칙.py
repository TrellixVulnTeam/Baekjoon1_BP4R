import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

def KEVIN_BFS(V):
    count = 0
    not_visited = deque([V])
    visited = []
    distance = 0
    while not_visited:
        node = not_visited.popleft()
        if node not in visited:
            visited.append((node, distance))
            distance += 1
            not_visited.extend(graph[node])
    answer[V] = count

graph = [[] for x in range(N + 1)]
answer = {}
for _ in range(M):
    n, m = map(int, sys.stdin.readline().split())
    graph[n].append(m)
    graph[m].append(n)
for a in range(1, N + 1):
    KEVIN_BFS(a)
A = sorted(answer.items(), key=lambda x: x[1])
print(A)
