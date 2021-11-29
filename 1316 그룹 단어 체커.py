N = int(input())
answer = 0 
for _ in range(0, N):
    big = True
    d = {}
    string = input()
    for k, v in list(enumerate(string)):
        if v not in d:
            d[v] = [k]
        else:
            d[v].append(k)
    for l in d.values():
        small = True

        for a in range(0, len(l)):
            try:
                if l[a] + 1 != l[a + 1]:
                    big = False
                    break
            except:
                continue
    if big == True:
        answer += 1

print(answer)