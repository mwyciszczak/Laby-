def koszt_pracodawcy(kwota_brutto):
    ubezpieczenie_emerytalne = kwota_brutto * 0.0976
    ubezpieczenie_rentowe = kwota_brutto * 0.065
    ubezpieczenie_wypadkowe = kwota_brutto * 0.0167
    fp = kwota_brutto * 0.0245
    fgsp = kwota_brutto * 0.01
    ubezpieczenia = ubezpieczenie_emerytalne + ubezpieczenie_rentowe + ubezpieczenie_wypadkowe + fp + fgsp
    koszty_całkowite = kwota_brutto + ubezpieczenia
    return round(koszty_całkowite, 2)

print("Witaj w kalkulatorze kosztów pracodawcy")
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
        print("Całkowity koszt zatrudnienia pracownika wyniesie {}".format(koszt_pracodawcy(podana_brutto)))
        break
    elif wybor_menu == "2":
        exit()
    else:
        pass