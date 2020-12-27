l = float(input("Podaj liczbę: "))

if l == 0:
    print("Liczba to 0.")
elif l > 0:
    print("Liczba jest dodatnia.")
elif l < 0:
    print("Liczba jest ujemna.")

if l % 2 != 0:
    print("Liczba jest podzielna przez dwa z resztą.")