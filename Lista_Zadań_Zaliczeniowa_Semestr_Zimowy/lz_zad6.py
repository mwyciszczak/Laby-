import pytemp as t

def czy_wrze(temp_cel):
    if t.pytemp(temp_cel, "c", "f") <= 32:
        return "Woda jest zamarznięta i ma {} stopni Fahrenheita.".format(round(t.pytemp(temp_cel, "c", "f"), 2))
    elif t.pytemp(temp_cel, "c", "f") >= 212:
        return "Woda wrze i ma {} stopni Fahrenheita.".format(round(t.pytemp(temp_cel, "c", "f"), 2))
    else:
        return"Woda jest spokojna i ma {} stopni Fahrenheita.".format(round(t.pytemp(temp_cel, "c", "f"), 2))

def kelwin_fahrenheit(temp_kel):
    return "{} stopni kelwina to {} stopni fahrenheita.".format(temp_kel, t.pytemp(temp_kel, "k", "f"), 2)

def fahrenheit_kelwin(temp_fahr):
    return "{} stopni fahrenheita to {} stopni kelwina.".format(temp_fahr, t.pytemp(temp_fahr, "f", "k"), 2)

def kelwin_celsjusz(temp_kel):
    return "{} stopni kelwina to {} stopni celsjusza.".format(temp_kel, t.pytemp(temp_kel, "k", "c"), 2)

def celsjusz_kelwin(temp_cel):
    return "{} stopni celsjusza to {} stopni kelwina.".format(temp_cel, t.pytemp(temp_cel, "c", "k"), 2)

def celsjusz_rankin(temp_cel):
    rank = round((temp_cel + 273.15) * (9/5), 2)
    return "{} stopni celsjusza to {} stopni w skali Rankine'a".format(temp_cel, rank)

def rankin_celsjusz(temp_rank):
    cel = round((temp_rank - 491.67) * (5 / 9), 2)
    return "{} stopni w skali Rankine'a to {} stopni celsjusza".format(temp_rank, cel)



print("Witaj w kalkulatorze temperatur")
print("""
1.Czy woda wrze?
2.Przeliczenia temperatur
3.Wyjście
""")
while True:
    wybor_menu = input("Proszę wybierz opcję (1, 2, 3): ")
    if wybor_menu == "1":
        while True:
            try:
                podana_temperatura = float(input("Proszę podaj temperaturę w stopniach celsjusza: "))
                break
            except:
                print("Proszę podaj wielkość używając cyfr.")
        print(czy_wrze(podana_temperatura))
        break
    elif wybor_menu == "2":
        print("Jakiej konwersji chcesz dokonać?")
        print("""
1.Kelwin => Fahrenheit
2.Fahrenheit => Kelwin
3.Kelwin => Celsjusz
4.Celsjusz => Kelwin
5.Celsjusz => Stopień Rankina
6.Stopień Rankina => Celsjusz
        """)
        bylo = 0
        while True:
            if bylo == 0:
                while True:
                        try:
                            temp = float(input("Proszę podaj temperaturę w wybranej jednostce"))
                            bylo += 1
                            break
                        except:
                            print("Proszę podaj temperaturę używając cyfr.")
            wybor = input("Proszę podaj której konwersji chcesz dokonać: ")
            if wybor == "1":
                print(kelwin_fahrenheit(temp))
                break
            elif wybor == "2":
                print(fahrenheit_kelwin(temp))
                break
            elif wybor == "3":
                print(kelwin_celsjusz(temp))
                break
            elif wybor == "4":
                print(celsjusz_kelwin(temp))
                break
            elif wybor == "5":
                print(celsjusz_rankin(temp))
                break
            elif wybor == "6":
                print(rankin_celsjusz(temp))
                break
            else:
                print("Proszę wybierz opcję od '1' do '4'")

        break
    elif wybor_menu == "3":
        exit()
    else:
        pass