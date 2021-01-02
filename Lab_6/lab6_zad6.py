import random

n = int(input("Podaj długość ciągu: "))
y = int(input("Podaj dolną granicę ciągu: "))
z = int(input("Podaj górną granicę  ciągu: "))

tab = []
unikalne = []

for x in range(n):
    tab.append(random.randint(y, z))

tab = list(dict.fromkeys(tab))
print("Unikalne elementy listy to {}, a jej długość to {}".format(sorted(tab), len(tab)))