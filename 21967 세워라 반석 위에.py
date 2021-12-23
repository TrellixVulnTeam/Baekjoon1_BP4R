import sys
def main():
    N = int(sys.stdin.readline().strip())
    lst = list(map(int, sys.stdin.readline().strip().split(" ")))
    answer = 1
    for n in range(0, N):
        temp = 1
        if n == N - 1:
            continue
        minimum = lst[n]
        maximum = lst[n]
        for m in range(n + 1, N):
            if lst[m] < minimum:
                minimum = lst[m]
            if lst[m] > maximum:
                maximum = lst[m]
        
            if maximum - minimum > 2:
                break
            temp += 1
        if temp > answer:
            answer = temp


    sys.stdout.write(answer)

if __name__ == '__main__':
    main()
