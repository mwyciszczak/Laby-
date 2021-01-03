dict = {}

ile = int(input("Podaj ile maili chcesz dopisać do słownika"))

plik = open("adresy.txt", "wt")

for x in range(ile):
    imie = input("Podaj imię użytkownika: ")
    mail = input("Podaj mail użytkownika: ")
    dict[imie] = mail

dopliku = str(dict)
plik.write(dopliku)
#w ten sposób możemy przetrzymywać adresy mailowe w pliku txt i wykorzystać je w innym skrypcie który by te maile wysyłał