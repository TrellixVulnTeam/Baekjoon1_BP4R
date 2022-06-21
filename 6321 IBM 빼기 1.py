N = int(input())
for n in range(N):
    word = input()
    ret = ""
    for w in word:
        if w == 'Z':
            ret += 'A'
        else:
            ret += chr(ord(w) + 1)
    
    print(f"String #{n + 1}")
    print(ret)
    if n + 1 != N:
        print()