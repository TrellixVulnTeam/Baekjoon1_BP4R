import sys
t = int(sys.stdin.readline().strip())
d = {1: 11, 2: 5, 3: 3}

def combination()

for _ in range(t):
    answer = 0
    n = int(sys.stdin.readline().strip())
    for i in range(0, 11):
        for j in range(0, 11):
            for k in range(0, 11):
                how = 0
                s = 0
                for var in [i, j, k]:
                    if var > 0:
                        how += 1
                if i * 1 + j * 2 + k * 3 == n:
                    
    print(answer)
