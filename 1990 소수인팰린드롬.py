import sys
N, M = map(int, sys.stdin.readline().strip().split())
if M > 10000000:
    M = 10000000
palindromes = []
answer = []
for num in range(N, M + 1):
    if str(num) == str(num)[::-1]:
        palindromes.append(num)
for palindrome in palindromes:
    boolean = True
    for i in range(2, int(pow(palindrome, 0.5)) + 1):
        if palindrome % i == 0:
            boolean = False
            break
    if boolean:
        answer.append(palindrome)
for a in answer:
    print(a)
print(-1)