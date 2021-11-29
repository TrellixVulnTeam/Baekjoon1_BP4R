while True:
    try:
        A,B = input().split()
        if int(A) + int(B) == 0:
            break
        print(int(A)+int(B))

    except:
        break