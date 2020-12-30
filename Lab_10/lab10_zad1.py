a = '''Magia jest w opinii niektórych ucieleśnieniem Chaosu. Jest kluczem zdolnym otworzyć zakazane drzwi. Drzwi, 
    za którymi czai się koszmar, zgroza i niewyobrażalna okropność, za którymi czyhają wrogie, destrukcyjne 
    siły, moce czystego zła, mogące unicestwić nie tylko tego, kto drzwi te uchyli, ale i cały świat. A ponieważ 
    nie brakuje takich, którzy przy owych drzwiach manipulują, kiedyś ktoś popełni błąd, a wówczas zagłada świata 
    będzie przesądzona i nieuchronna. Magia jest zatem zemstą i orężem Chaosu. To, że po Koniunkcji Sfer ludzie 
    nauczyli posługiwać się magią, jest przekleństwem i zgubą świata. Zgubą ludzkości. I tak jest. Ci, którzy 
    uważają magię za Chaos, nie mylą się.'''

(print(a[:53].lower()))
(print(a[:53].swapcase()))
(print(a[107:134].capitalize()))

x = a[:53].replace("Magia","Wiedźmini")
b = x.replace("jest", "są")
c = b.replace("Chaosu", "zła")
print(c)

print(a[:99].lstrip("M"))
print(a[:99].rstrip("."))

lista = list(reversed(a[:5]))
print(lista)

ilość_a = lista.count("a")
ilość_i = lista.count("i")

print(f"W słowie magia są {ilość_a} litery 'a' i {ilość_i} litera 'i'")

słowo = a.find("Koniunkcji")
litera = a.find("d")
print(f"Słowo 'Koniunkcji' zaczyna się na {słowo} miejscu")
print(f"Pierwsza litera 'd' znajduje się na {litera} miejscu")

print(a.isalnum())
print(a[:5].isalnum())

print("----------------------")

print(a.startswith("Magia"))
print(a.startswith("przekleństwem"))

print("----------------------")

print(a.endswith("."))
print(a.endswith("się"))