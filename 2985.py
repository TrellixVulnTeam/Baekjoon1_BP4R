A, B, C = map(int, input().split())
lst = [str(A)]
if A + B == C:
    lst.append('+')
    lst.append(str(B))
    lst.append('=')
    lst.append(str(C))
    print("".join(lst))
    quit()
if A - B == C:
    lst.append('-')
    lst.append(str(B))
    lst.append('=')
    lst.append(str(C))
    print("".join(lst))
    quit()
if A * B == C:
    lst.append('*')
    lst.append(str(B))
    lst.append('=')
    lst.append(str(C))
    print("".join(lst))
    quit()
if A // B == C:
    lst.append('/')
    lst.append(str(B))
    lst.append('=')
    lst.append(str(C))
    print("".join(lst))
    quit()
if A == B + C:
    lst.append('=')
    lst.append(str(B))
    lst.append('+')
    lst.append(str(C))
    print("".join(lst))
    quit()
if A == B - C:
    lst.append('=')
    lst.append(str(B))
    lst.append('-')
    lst.append(str(C))
    print("".join(lst))
    quit()
if A == B * C:
    lst.append('=')
    lst.append(str(B))
    lst.append('*')
    lst.append(str(C))
    print("".join(lst))
    quit()
if A == B // C:
    lst.append('=')
    lst.append(str(B))
    lst.append('/')
    lst.append(str(C))
    print("".join(lst))
    quit()
