while True:
    try:
        boolean = True
        A, B = input().split()
        index = 0
        for a in A:
            if a not in B[index:len(B)]:
                boolean = False
            for n in range(index, len(B)):
                if a == B[n]:
                    index = n + 1
                    break

                                   
        if boolean:
            print("Yes")
        else:
            print("No")
    except:
        quit()    
        