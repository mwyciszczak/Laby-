ostatnia = 0
sum = 0

while True:
    podana = float(input("Podaj liczbę: "))
    sum = sum + podana
    if podana == ostatnia:
        break
    ostatnia = podana

print("Koniec, suma to {}".format(sum))