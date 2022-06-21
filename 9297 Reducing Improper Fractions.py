N = int(input())
for n in range(N):
    A, B = map(int, input().split())
    if A // B == 0:
        print(f"Case {n + 1}: {A%B}/{B}")
    elif A % B == 0:
        print(f"Case {n + 1}: {A//B}")
    elif A // B == 0 and A % B == 0:
        print(f"Case {n+1}: 0")
    else:
        print(f"Case {n+1}: {A//B} {A%B}/{B}")
    
