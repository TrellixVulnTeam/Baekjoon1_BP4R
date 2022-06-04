A = input()
B = input()
count = 0
for a in set(A):
    num = A.count(a) - B.count(a)
    if num > 0:
        count += num
for b in set(B):
    n = B.count(b) - A.count(b)
    if n > 0:
        count += n
print(count)