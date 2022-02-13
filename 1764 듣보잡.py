import sys
N, M = map(int, sys.stdin.readline().strip().split())
not_heard = {}
not_seen = {}
answer = []
for n in range(N):
    name = sys.stdin.readline().strip()
    not_heard[name] = True
    
for m in range(M):
    other = sys.stdin.readline().strip()
    not_seen[other] = True
for person in not_heard:
    if not_seen.get(person, 0) != 0:
        answer.append(person)
answer.sort()
print(len(answer))
for a in answer:
    print(a)
    
