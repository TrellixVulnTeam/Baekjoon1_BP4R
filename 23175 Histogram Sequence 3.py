N = int(input())
lst = list(map(int, input().split()))
answer = []
index = 0
while index < len(lst):
    answer.append(lst[index])
    for c in range(lst[index]):
        index += 1

for a in answer:
    print(a, end= ' ')