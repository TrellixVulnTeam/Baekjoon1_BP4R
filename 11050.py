N, K = input().split()
Nfac = 0
Kfac = 0
NminKfac = 0
for n in range(1, int(N) + 1):
    if Nfac == 0:
        Nfac += n
    else:
        Nfac = Nfac*n
for k in range(1, int(K) + 1):
    if Kfac == 0:
        Kfac += k
    else:
        Kfac = Kfac * k


for num in range(1,int(N) - int(K) + 1):
    if NminKfac == 0:
        NminKfac += num
    else:
        NminKfac = NminKfac * num
if Kfac == 0 or NminKfac == 0:
    print(1)
    quit()
print(Nfac//(Kfac*NminKfac))