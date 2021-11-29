N = int(input())
for _ in range(0, N):
    lst = []
    count = 0
    inp = input()
    boolean = True
    for parenthesis in inp:
        count += 1
        if parenthesis == "(":
            lst.append("(")
        if parenthesis == ")":
            try:
                lst.pop()
            except IndexError:
                print("NO")
                boolean = False
                break
             
    if count == len(inp) and boolean == True:
        if len(lst) == 0:
                print("YES")
        else:
            print("NO")