n, m = input().split()
n = int(n)
m = int(m)
cards = input().split(" ")
maximum = 0
for a in range(0, int(n)):
    lst = [int(cards[a])]
    for b in range(0, int(n)):
        if b != 0 and b - 1 != a:
            lst.pop()
        if b == a:
            continue
        lst.append(int(cards[b]))
        for c in range(0, int(n)):
            if c == a or c == b:
                continue
            lst.append(int(cards[c]))
            if maximum == 0 and sum(lst) <= m:
                maximum = sum(lst)
            if m - maximum > m - sum(lst) and sum(lst) <= m:
                maximum = sum(lst)
            lst.pop()
print(maximum)