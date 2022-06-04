N = int(input())
for _ in range(N):
    word = input()
    d = {}
    answer = 0
    count = 65
    for w in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        d[w] = count
        count += 1
    for k in d.keys():
        if k not in word:
            answer += d[k]
    print(answer)