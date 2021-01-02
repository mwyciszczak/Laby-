inp = float(input("Podaj liczbę: "))
i = 1
sum = 0

while i < inp:
    if inp % i == 0:
        sum = sum + i
    i += 1

if inp == 0:
    print("Liczba nie jest doskonała.")
elif sum == inp:
    print("Liczba jest doskonała.")
else:
    print("Liczba nie jest doskonała.")