T = int(input())
s300 = 0
s60 = 0
s10 = 0
s300 = T//300
s60 = T % 300 // 60
if T % 10 != 0:
    print(-1)
    quit()
else:
    s10 = T % 60 // 10
print(s300, s60, s10)