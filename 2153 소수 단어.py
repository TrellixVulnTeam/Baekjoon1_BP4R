word = input()
num = 1
d = {}

for s in 'abcdefghijklmnopqrstuvwxyz':
    d[s] = num
    num += 1
for S in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    d[S] = num
    num += 1
integer = 0
for w in word:
    integer += d[w]

if integer == 1:
    print("It is a prime word.")
else:
    for n in range(2, integer):
        if integer % n == 0:
            print("It is not a prime word.")
            quit()
    print("It is a prime word.")