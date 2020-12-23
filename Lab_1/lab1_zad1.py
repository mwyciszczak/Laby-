l1 = float(input("Podaj pierwsza liczbe: "))
l2 = float(input("Podaj druga liczbe: "))

if l2 != 0:
    print("Suma liczb to {}, ich różnica to {}. Ich iloczyn to {}, a iloraz to {}.".format(l1+l2, l1-l2, l1*l2, l1/l2))
else:
    print("Suma liczb to {}, ich różnica to {}. Ich iloczyn to {}.".format(l1+l2, l1-l2, l1*l2))