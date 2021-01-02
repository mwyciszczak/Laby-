sum = 0
i = 0
while True:
    inp = float(input("Prosze podaj liczbę: "))
    sum = sum + inp
    i += 1
    if sum > 100 or sum / i == 66:
        break