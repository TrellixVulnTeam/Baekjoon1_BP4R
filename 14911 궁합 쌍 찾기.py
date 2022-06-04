lst = list(map(int, input().split()))
n = int(input())
answers = []

for i in range(0, len(lst)):
    for j in range(0, len(lst)):
        if i != j:
            if lst[i] + lst[j] == n:
                answers.append(sorted(tuple((lst[i], lst[j]))))

answers.sort()
l = []
count = 0
for a, b in answers:
    if (a, b) not in l:
        print(a, b)
        count += 1
    l.append((a, b))
print(count)