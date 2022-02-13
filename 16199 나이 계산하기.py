y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if y1 == y2:
    print(0)
    print(1)
    print(0)
    quit()
mann = y2 - y1
if m2 < m1 or m2 == m1 and d2 < d1:
    mann -= 1
sen = y2 - y1 + 1
yeon = y2 - y1
print(mann)
print(sen)
print(yeon)