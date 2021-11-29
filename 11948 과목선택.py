from itertools import combinations
answer = []
count = 0
science = []
social = []
for _ in range(0, 4):
    science.append(int(input()))
for z in range(0, 2):
    social.append(int(input()))

for l in list(combinations(science, 3)):
    answer.append(sum(l))

count += max(answer) + max(social)

print(count)