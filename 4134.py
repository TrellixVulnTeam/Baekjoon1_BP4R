import sys
import math
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(input())
    num = n
    while True:
        boolean = True
        for a in range(2, int(math.sqrt(num)) + 1):
            if num % a == 0:
                boolean = False
                break
        if boolean:
            print(num)
            break
        num += 1

                
                