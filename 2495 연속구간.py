def solve(l):
    current = l[0]
    length = 1
    answer = 1
    for i in range(1, len(l)):
        if l[i] == current:
            length += 1
        else:
            current = l[i]
            maximum = max(length, answer)
            length = 0

            



one = input()
two = input()
three = input()
print(solve(one))
print(solve(two))
print(solve(three))