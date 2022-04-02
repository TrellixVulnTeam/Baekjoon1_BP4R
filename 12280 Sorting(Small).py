import sys
T = int(sys.stdin.readline().strip())
for case in range(T):
    N = int(sys.stdin.readline().strip())
    lst = list(map(int, sys.stdin.readline().strip().split()))
    odd = [l for l in lst if l % 2 == 1]
    even = [li for li in lst if li % 2 == 0]
    answer = []
    odd.sort()
    even.sort(reverse=True)
    j = 0
    k = 0
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            answer.append(even[j])
            j += 1
        else:
            answer.append(odd[k])
            k += 1
    print(f"Case #{case + 1}:")
    for a in answer:
        print(a, end = ' ')
