x = int(input())
for num in range(1,x+1):
    P = []
    m,n = input().split()
    for _ in n:
        P.append(_*int(m))
    word = ("").join(P)
    print(word)

