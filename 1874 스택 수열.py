import sys
lst = []
answer = []
now = 1
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    while now <= num:
        lst.append(now)
        answer.append('+')
        now += 1
    if lst[-1] == num:
        lst.pop()
        answer.append('-')
    else:
        print("NO")
        quit()
for a in answer:
    print(a)

    
        
        
            
