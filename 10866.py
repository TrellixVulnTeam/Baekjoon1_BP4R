N = int(input())
deque = []
for _ in range (0,N):
    inp = input().split(" ")
    if inp == ["push_back",]:
        deque.append(inp[1])
    if inp == [push_]