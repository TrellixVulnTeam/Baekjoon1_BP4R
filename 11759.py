s, a, b = input().split()
acount = 0
bcount = 0
s_new = int(s)
a_new = int(a)
b_new = int(b)
while True:
    if s_new % a_new == 0:
        break
    if s_new < 0:
        print("Impossible")
        quit()
    s_new -= b_new
    bcount += 1

print (s_new // a_new , bcount)
