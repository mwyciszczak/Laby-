liczba = input("Podaj liczbę: ")
tab = []
stara = tab

for x in liczba:
    tab.append(x)

tab = tab[::-1]

for x in tab:
    print(x, end="")

if tab == stara:
    print("", end="\n")
    print("Liczba jest palindromem.")


