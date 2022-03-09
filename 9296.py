t = int(input())
for _ in range(t):
    l = int(input())
    answer = input()
    key = input()
    count = 0
    for i in range(0, l):
        if answer[i] != key[i]:
            count += 1
    print(f"Case {_+1}: {count}")