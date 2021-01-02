ile = int(input("Podaj ilość liczb: "))
tab = []

for x in range(ile):
    inp = int(input("Podaj liczbę: "))
    if inp >= -6 and inp <= 6:
        print("Liczba należy do przedziału -6 i 6.")

