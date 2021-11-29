N = int(input())
count = 1 
space = N - 1
if N == 1:
    print("*")
    quit()
print(' '* space + "*")
for _ in range(N - 1):
    space -= 1
    print(space * ' '+ "*" + ' '*count + "*")
    count += 2