x = int(input("Podaj ilość okien: "))
y = int(input("Podaj ilość drzwi: "))

def pokoj(okna, drzwi):
    pole = 2 * (3*5 + 3*2.5 + 5*2.5) - 3*5
    pow_okna = 1.765*1.435
    pow_drzwi = 0.7 * 1
    wynik = pole - (pow_okna * okna) - (pow_drzwi * drzwi)
    print("Ściany i sufit mają powierzchnię {} metrów kwadratowych.".format(round(wynik, 2)))
pokoj(x, y)