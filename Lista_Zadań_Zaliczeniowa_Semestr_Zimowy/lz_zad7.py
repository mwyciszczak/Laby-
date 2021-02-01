import datetime
from dateutil.easter import *

dni = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

def jutro(dzis):
    dzis += datetime.timedelta(days=1)
    return dzis

def wczoraj(dzis):
    dzis += datetime.timedelta(days=-1)
    return dzis

def wielkanoc(rok):
    return easter(rok)

def dzien_urodzin(dzis):
    rok = dzis.year
    miesiac = dzis.month
    dzien = dzis.day
    narodziny = datetime.date(rok, miesiac, dzien)
    indeks = narodziny.weekday()
    return dni[indeks]

def ustalanie_daty():
    while True:
        try:
            dzien = int(input("Proszę podaj dzień: "))
            break
        except:
            print("Proszę podaj dzień użwyając cyfr.")
    while True:
        try:
            miesiac = int(input("Proszę podaj miesiąc: "))
            break
        except:
            print("Proszę podaj miesiąc użwyając cyfr.")
    while True:
        try:
            rok = int(input("Proszę podaj rok: "))
            break
        except:
            print("Proszę podaj rok użwyając cyfr.")
    data = datetime.date(rok, miesiac, dzien)
    return data

def pytanie_rok():
    while True:
        try:
            rok = int(input("Proszę podaj rok: "))
            break
        except:
            print("Proszę podaj rok użwyając cyfr.")
    return rok

print("Witaj w kalendarzu.")
print("""
1.Jaki dzień będzie jutro
2.Jaki dzień był wczoraj
3.Kiedy będzie wielkanoc w danym roku
4.W jaki dzień tygodnia się urodziłeś/aś
5.Wyjście
""")


while True:
    wybor = input("Proszę wybierz opcję od '1' do '5'.")
    if wybor == "1":
        print(jutro(ustalanie_daty()))
        break
    elif wybor == "2":
        print(wczoraj(ustalanie_daty()))
        break
    elif wybor == "3":
        print(easter(pytanie_rok()))
        break
    elif wybor == "4":
        print(dzien_urodzin(ustalanie_daty()))
        break
    elif wybor == "5":
        exit()
    else:
        print("Proszę podaj wybór od '1' do '5'")
