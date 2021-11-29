T, A, S, B = map(int, input().split())
count = 0
lst = map(int, input().split(" "))
for n in range(S, B+1):
    count += len(list(combinations(lst, n)))
print(count % 1000000)