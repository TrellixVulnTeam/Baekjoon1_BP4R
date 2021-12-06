from collections import deque
import sys

def BFS(V):
    not_visited = deque()
    visited = []
    not_visited.append(V)
    while not_visited:
        node = not_visited.popleft()
        if node not in visited:
            visited.append(node)
            not_visited.extend(graph[node])
    for v in visited:
        print(v, end= ' ')


def DFS(V):
    not_visited, visited = list(), list()
    not_visited.append(V)

    while not_visited:
        node = not_visited.pop()

        if node not in visited:
            visited.append(node)

            not_visited.extend(DFS_graph[node])
    for v in visited[:-1]:
        print(v, end= ' ')
    print(visited[-1])
    


if __name__ == '__main__':
    N, M, V = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range (N + 1)] 
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for g in graph:
        g.sort()
    DFS_graph = [reversed(sorted(x)) for x in graph]
    DFS(V)
    BFS(V)





    

    


