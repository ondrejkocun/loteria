import random
vstup=input('Zadaj 6 cisel')
vstup=vstup.split(' ')
vyzrebovane=[]*6
spravne=0
volaco=[]
hocico=[]
pocitadlo=[]*7
subor=open('loteria_1.txt','r')

for i in range(1,7):
    vyzrebovane.append(random.randint(1,49))
for i in vstup:
    if int(i) in vyzrebovane:
        spravne+=1
for riadok in subor:
    hocico.append(riadok.strip())
for i in range(7):
    pocitadlo=0
    volaco=hocico[i].split(' ')
    for x in range(6):
        if int(volaco[x]) in vyzrebovane:
            pocitadlo[i]
            print('hrac',i+1,'trafil',pocitadlo[i])

print('Vyzrebovane cisla',vyzrebovane)
print('Trafil si ',spravne)
print('ostatni netrafili nic')
