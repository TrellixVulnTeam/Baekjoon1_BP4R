lst = []
answer = []
count = 0
N, K = map(int, input().split())
if N == 1:
    print("<" + '1' + ">")
    quit()
for n in range(1, N + 1):
    lst.append(n)
while True:
    for n in lst:
        count += 1
        if count != 0 and count % K == 0:
            answer.append(n)
    while True:
        boolean = True
        for a in lst:
            if a in answer:
                lst.remove(a)
        for w in answer:
            if w in lst:
                boolean = False
        if boolean == True:
            break
                
    if len(lst) == 0:
        break    
print("<", end='')
for b in answer:
    if b == answer[-1]:
        print(b, end='')
    else:
        print(b, end=', ')
print(">")