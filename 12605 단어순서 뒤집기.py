N = int(input())
for n in range(N):
    lst = input().split()
    print(f"Case #{n + 1}:", end=' ')
    for l in range(len(lst) -1, -1, -1):
        print(lst[l], end=' ')
    print()
