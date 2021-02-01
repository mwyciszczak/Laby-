def brutto_to_netto(stawka_brutto):
    skladka_emerytalna = stawka_brutto * 0.0976
    skladka_rentowa = stawka_brutto * 0.015
    skladka_chorobowe = stawka_brutto * 0.0245
    skladki = skladka_rentowa + skladka_chorobowe + skladka_emerytalna
    wynagrodzenie_zasadnicze = stawka_brutto - skladka_chorobowe - skladka_rentowa - skladka_emerytalna
    ubezpieczenie_zdrowotne = wynagrodzenie_zasadnicze * 0.09
    zus = wynagrodzenie_zasadnicze * 0.0775
    podstawa_opodatkowania = skladka_chorobowe + skladka_emerytalna + skladka_rentowa + ubezpieczenie_zdrowotne
    brutto_bez_podstawy = stawka_brutto - podstawa_opodatkowania
    kwota_zmniejszajaca_podatek = 43.76
    zaliczka_na_podatek = brutto_bez_podstawy * 0.17 - zus - kwota_zmniejszajaca_podatek
    stawka_netto = stawka_brutto - (skladki + ubezpieczenie_zdrowotne + zaliczka_na_podatek)
    return round(stawka_netto, 2)


print("Witaj w kalkulatorze brutto => netto")
print("""
1.Kalkulator
2.Wyjście
""")
while True:
    wybor_menu = input("Proszę wybierz opcję (1, 2): ")
    if wybor_menu == "1":
        while True:
            try:
                podana_brutto = float(input("Proszę podaj kwotę brutto: "))
                break
            except:
                print("Proszę podaj kwotę przy użyciu cyfr.")
        print("Kwota netto z podanej kwoty brutto to {}".format(brutto_to_netto(podana_brutto)))
        break
    elif wybor_menu == "2":
        exit()
    else:
        pass
