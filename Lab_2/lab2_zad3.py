l1 = float(input("Podaj pierwszą liczbę: "))
l2 = float(input("Podaj drugą liczbę: "))
l3 = float(input("Podaj trzecią liczbę: "))
tab = []

tab.append(l1)
tab.append(l2)
tab.append(l3)
tab = sorted(tab)

print("Liczby w kolejności rosnącej to odpowiednio {}, {}, {}.".format(tab[0], tab[1], tab[2]))
if l1 == l2 == l3:
    print("Wszystkie liczby są takie same.")
elif l1 == l2:
    print("Pierwsza liczba i druga liczba są identyczne.")
elif l1 == l3:
    print("Pierwsza liczba i trzecia liczba są identyczne.")
elif l2 == l3:
    print("Druga liczba i trzecia liczba są identyczne.")