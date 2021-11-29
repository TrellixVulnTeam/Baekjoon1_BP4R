N = int(input())
lst = list(map(int, input().split(" ")))
for n in range(1, lst.index(max(lst)) + 1):
    if lst[n] > lst[n-1]:
        continue
    else:
        print("NO")
        quit()
for m in range(lst.index(max(lst)) + 1, N):
    if lst[m] < lst[m-1]:
        continue
    else:
        print("NO")
        quit()
print("YES")