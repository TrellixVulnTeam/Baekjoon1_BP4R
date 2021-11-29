word = input()
upper = word.upper()
dict = {}
for x in upper:
    if x in dict:
        dict[x] += 1
    if x not in dict:
        dict[x] = 1

items = dict.items()
maximum = 0
maxcount = 0
maxlist = []
maxnum = []
count = 0
for k, v in items:
    if v > maximum:
        maximum = v
        maxlist = k,v
    else:
        continue
for k, v in items:
    if v == max(dict.values()):
        count += 1
if count > 1:
    print("?")
    quit()
print(maxlist[0])








