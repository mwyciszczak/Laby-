mozliwe_zamiany = """
1.Bat Tajlandzki(THB) => Dolar Amerykański(USD)
2.Ngultrum bhutański(BTN) => Dolar Amerykański(USD)
3.Ugija mauretańska(MRO) => Dolar Amerykański(USD)
4.Bitcoin(BTC) => Dolar Amerykański(USD)
5.Etherum(ETH) => Dolar Amerykański(USD)
6.Doge Coin(DOGE) => Dolar Amerykański(USD)
"""

THB = 30
BTN = 72.82
MRO = 36.08
BTC = 0.000030
ETH = 0.00077
DOGE = 28.06

def thb_usd(ile, z_usd):
    if z_usd == True:
        return "{} USD to {} BHT".format(ile, round(ile * THB, 2))
    elif z_usd == False:
        return "{} BHT to {} USD".format(ile, round(ile / THB, 2))
    else:
        print("Wystąpił błąd")

def btn_usd(ile, z_usd):
    if z_usd == True:
        return "{} USD to {} BTN".format(ile, round(ile * BTN, 2))
    elif z_usd == False:
        return "{} BTN to {} USD".format(ile, round(ile / BTN, 2))
    else:
        print("Wystąpił błąd")

def mro_usd(ile, z_usd):
    if z_usd == True:
        return "{} USD to {} MRO".format(ile, round(ile * MRO, 2))
    elif z_usd == False:
        return "{} MRO to {} USD".format(ile, round(ile / MRO, 2))
    else:
        print("Wystąpił błąd")

def btc_usd(ile, z_usd):
    if z_usd == True:
        return "{} USD to {} BTC".format(ile, round(ile * BTC, 2))
    elif z_usd == False:
        return "{} BTC to {} USD".format(ile, round(ile / BTC, 2))
    else:
        print("Wystąpił błąd")

def eth_usd(ile, z_usd):
    if z_usd == True:
        return "{} USD to {} ETH".format(ile, round(ile * ETH, 2))
    elif z_usd == False:
        return "{} ETH to {} USD".format(ile, round(ile / ETH, 2))
    else:
        print("Wystąpił błąd")

def doge_usd(ile, z_usd):
    if z_usd == True:
        return "{} USD to {} DOGE".format(ile, round(ile * DOGE, 2))
    elif z_usd == False:
        return "{} DOGE to {} USD".format(ile, round(ile / DOGE, 2))
    else:
        print("Wystąpił błąd")


print("Witaj w kalkulatorze walut")
print("""
1.Kalkulator
2.Wyjście
""")
wybor_menu = input("Proszę wybierz opcję (1, 2): ")
if wybor_menu == "1":
    print(mozliwe_zamiany)
    while True:
        odwrotna = input("Czy chcesz dokonać konwersji z dolarów? ('y', 'n'): ")
        if odwrotna == "y":
            z_dolarow = True
            break
        elif odwrotna == "n":
            z_dolarow = False
            break
        else:
            print("Proszę wybierz odpowiedź 'y', 'n'.")
    while True:
        try:
            wartosc = float(input("Jaką ilość waluty chcesz skonwertować?: "))
            break
        except:
            print("Proszę podaj tą wartość przy użyciu cyfr.")
    while True:
        wybor = input("Proszę wybierz walutę do zamiany")
        if wybor == '1':
            print(thb_usd(wartosc, z_dolarow))
            break
        elif wybor == "2":
            print(btn_usd(wartosc, z_dolarow))
            break
        elif wybor == "3":
            print(mro_usd(wartosc, z_dolarow))
            break
        elif wybor == "4":
            print(btc_usd(wartosc, z_dolarow))
            break
        elif wybor == "5":
            print(etc_usd(wartosc, z_dolarow))
            break
        elif wybor == "6":
            print(doge_usd(wartosc, z_dolarow))
            break
        else:
            print("Proszę wybierz opcję od '1' do '6'.")


elif wybor_menu == "2":
    exit()
else:
    pass