N = int(input())
lst = list(map(int, input().split()))
answer = []
dict = {}
count = 0
for _ in range(N):
    lst.append(0)
    answer.append(0)
for i in range(N):
    if lst[i] in dict:
        dict[lst[i]].append(i)
    else:
        dict[lst[i]] = [i]
for n in range(1, max(lst) + 1):
    if n in dict:
        while dict[n]:
            index = dict[n].pop(0)
            answer[index] = count
            count += 1
for a in answer:
    print(a, end=' ')




