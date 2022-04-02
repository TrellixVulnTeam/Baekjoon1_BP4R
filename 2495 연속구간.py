def solve(l):
    current = int(l[0])
    length = 1
    answer = 1
    for i in range(1, len(l)):
        if int(l[i]) == current:
            length += 1
        else:
            current = int(l[i])
            answer = max(length, answer)
            length = 1
    return answer

            
one = input()
two = input()
three = input()
print(solve(one))
print(solve(two))
print(solve(three))