cif = 1

for i in range (1,1999):
    cif = cif + 10**i

tot=cif*1999

sommaCifre=0
for i in str(tot):
    sommaCifre = sommaCifre + int(i)

print(sommaCifre)