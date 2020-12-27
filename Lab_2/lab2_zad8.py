a = int(input("Podaj pierwszą przyprostokątną: "))
b = int(input("Podaj drugą przyprostokątną: "))
c = int(input("Podaj przeciwprostokątną: "))

a = a**2
b = b**2

wynik = a + b

if wynik == c**2:
    print("Z podanych długości boków można utworzyć trójkąt prostokątny")
else:
    print("Z podanych długości boków nie można utworzyć trójkąt prostokątny")
