menu = {
    'Margherita': 18,
    'Pepperoni': 19,
    'Caprese': 19,
    'Roma': 20,
    'Quattro Formaggi': 23,
    'Diavola': 20,
    'Margherita Extra': 23,
    'Spaghetti Bolognese': 22,
    'Lasagne Pomidorowa': 25,
    'Foccacia': 15
}
for x in menu.keys():
    print(x)

for x in menu.values():
    print(x)

for x in menu.items():
    print(x)

menu.pop("Lasagne Pomidorowa")
menu.pop("Foccacia")

danie = input("Podaj nazwę dania: ")
cena = float(input("Podaj cenę dania: "))
menu[danie] = cena

print(menu)
