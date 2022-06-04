P, K = map(int, input().split())
for k in range(2, K + 1):
    if P % k == 0:
        print("BAD " + str(k))
        quit()

print("GOOD")