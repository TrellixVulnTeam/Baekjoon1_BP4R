N = int(input())
for n in range(N):
    A = []

    s = int(input())
    for a in range(1, s):
        for b in range(1, s):
            if a + b == s and a < b:
                A.append((a, b))
    print(f"Pairs for {s}:", end= ' ')
    for l in range(0, len(A)):
        if l != len(A) - 1:
            print(A[l][0], A[l][1], end = ', ')
        else:
            print(A[l][0], A[l][1])

