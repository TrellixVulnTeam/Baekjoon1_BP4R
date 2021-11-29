a,b = input().split()
reva = ''
revb = ''
for n in range(2,-1,-1):
    reva += a[n]
    revb += b[n]
print(max(int(reva), int(revb)))

