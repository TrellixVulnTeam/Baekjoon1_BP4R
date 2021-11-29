N = int(input())
for _ in range(0, N):
    lstA = []
    lstB = []
    A, B = input().split()
    for i in A:
        lstA.append(ord(i))
    for j in B:
        lstB.append(ord(j))
    if sum(lstA) == sum(lstB):
        print(A + ' & ' + B + ' are anagrams.')
    if sum(lstA) != sum(lstB):
        print(A + ' & ' + B + ' are NOT anagrams.')
        
