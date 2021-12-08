N = int(input())
lst = list(map(int, input().split()))
odd = 0
even = 0
answer = 0
for l in lst:
    if l % 2 == 0:
        even += 1
    else:
        odd += 1
if even == odd:
    print(even + odd)
    quit()
elif even > odd:
    print(2 * odd + 1)
    quit()
elif odd > even:
    odd += even*2
    while odd >= 0:
        if answer % 2 == 0:
            odd -= 2
            answer += 1
            if odd == 2:
                break
            elif odd == 1:
                answer += 1
                break
        else:
            odd -= 1
            answer += 1
            if odd == 2:
                answer += 1
                break
            if odd == 1:
                answer -= 1
                break
print(answer)

            

   