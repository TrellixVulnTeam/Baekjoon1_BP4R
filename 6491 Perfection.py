lst = list(map(int, input().split()))
for l in lst:
    factors = []
    if l == 0:
        quit()
    else:
        for n in range(1, l):
            if l%n == 0:
                factors.append(n)
        
        if sum(factors) < l:
            print((5 - len(str(l)))*' '+ str(l)+ " DEFICIENT")
        elif sum(factors) == l:
            print((5 - len(str(l)))*' '+str(l)+ " PERFECT")
        else: 
            print((5 - len(str(l)))*' '+str(l) + " ABUNDANT")