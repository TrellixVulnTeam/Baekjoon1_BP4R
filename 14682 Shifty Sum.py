N = int(input())
num = int(input())
answer = int(N)
for n in range(num):
    answer += int(N) * pow(10, n + 1)
print(answer)