import random

n = int(input("Podaj długość ciągu: "))
x = int(input("Podaj dolną granicę ciągu: "))
z = int(input("Podaj górną granicę  ciągu: "))
tab = []
tab1 = []
for y in range(n):
    tab.append(random.randint(x, z))

for y in range(n):
    tab1.append(random.randint(x, z))

ntab = tab + tab1
unikalne = []
powtorki = []

for x in ntab:
    if x not in unikalne:
        unikalne.append(x)
        continue
    powtorki.append(x)

print(ntab)
print("Długość ciągu to {}, wszystkie liczby występują raz poza {}.".format(len(ntab), powtorki))
