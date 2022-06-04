count = 1
lst = []
for _ in range(5):
    agent = input()
    if 'FBI' in agent:
        lst.append(count)
    count += 1
if len(lst) == 0:
    print("HE GOT AWAY!")
else:
    for l in lst:
        print(l, end = ' ')
    