from collections import deque
index = 0 
total = 1
name = input()
d = {}
for s in name:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
string = []
for key in d:
    while d[key] >= 2:
        string.insert(index, key)
        string.insert(len(name) - index, key)
        d[key] -= 2
        index += 1

if list(d.values()).count(1) <= 1:
    for e in d:
        if d[e] == 1:
            string.insert(index, e)
    print("".join(string))
else:
    print("I'm Sorry Hansoo")
    