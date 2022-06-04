num = int(input())
cur = 1
answer = 0
while num > 0:
    if cur > num:
        cur = 1
    num -= cur
    cur += 1
    answer += 1
print(answer)