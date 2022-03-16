while True:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        quit()
    else:
        while sum(lst) != max(lst):
            minimum = 1000
            index = 0
            for i in range(0, 4):
                if lst[i] > 0 and lst[i] < minimum:
                    minimum = lst[i]
                    index = i
            for j in range(0, 4):
                if j == index:
                    continue
                lst[j] = max(0, lst[j] - minimum)
        
        print(max(lst))