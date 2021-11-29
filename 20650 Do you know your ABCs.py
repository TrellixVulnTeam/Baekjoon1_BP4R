from itertools import combinations
lst = list(map(int, input().split(' ')))

lst = sorted(lst)
total_sum = lst[-1]
lst.pop(-1)

while True:
    answer = lst
    for l in list(combinations(lst, 3)):
        if sum(l) != total_sum:
            continue
        else:
            for j in list(combinations(l, 2)):
                if sum(j) not in answer:
                    continue
                else:
                    answer.pop(answer.index(sum(j)))
            for n in l:
                print(n, end = ' ')
    break



