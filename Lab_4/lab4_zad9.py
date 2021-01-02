sum = 0
ostatnia = 0

while True:
    podana = float(input("Podaj liczbę: "))
    sum = sum + podana
    if abs(podana - ostatnia) < 5:
        break
    ostatnia = podana

print("Koniec, suma to {}".format(sum))