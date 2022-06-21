from collections import Counter
s = ''
while True:
    try:
        word = input()
        s += word
    except:
        break

d = Counter(s)