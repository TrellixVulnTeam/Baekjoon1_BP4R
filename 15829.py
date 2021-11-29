N = int(input())
word = input()
count = 0
a = 1
for w in word:
    count += ((ord(w) - ord('a')+1)*(a))
    count = count%1234567891
    a = (a*31)% 1234567891
print(count)


