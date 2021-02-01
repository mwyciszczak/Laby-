#Źródło https://forum.pclab.pl/topic/637329-rzeczywista-pojemno%C5%9B%C4%87-dysku-jak-obliczamy/

czemu = """Pojemność dysków widziana w "sklepie" (wielkość marketingowa) i w "komputerze" (wielkość fizyczna) 
od zawsze była różna.
Wiąże się to z tym, że:
-system dziesiątkowy używany przez producentów dysków twardych: 1KB = 1000 bajtów
-system dwójkowy używany przez system operacyjny oraz BIOS 1KB = 1024 bajtów

"""

def pojemnosc(gb, czy_tb):
    if czy_tb == True:
        gb = gb * 1000
    gb = gb * 1000000000
    pojemnosc_rzeczywista = gb / 1024 / 1024 / 1024
    return round(pojemnosc_rzeczywista, 2)

print("Witaj w kalkulatorze rzeczywistej pojemności dysków")
print("""
1.Kalkulator
2.Czemu jesteśmy oszukiwani
3.Wyjście
""")
while True:
    wybor_menu = input("Proszę wybierz opcję (1, 2, 3): ")
    if wybor_menu == "1":
        while True:
            try:
                wielkosc_dysku = float(input("Proszę podaj wielkość dysku w GB: "))
                break
            except:
                print("Proszę podaj wielkość przy użyciu cyfr.")
        while True:
            tb = input("Czy podałeś/aś wielkość dysku w TB zamiast GB, mimo prośby? (y, n): ")
            if tb == "y":
                dzban = True
                break
            elif tb == "n":
                dzban = False
                break
            else:
                print("Proszę podaj odpowiedź używając liter 'y' lub 'n' ")
        print("Rzeczywista pojemność dysku to {}".format(pojemnosc(wielkosc_dysku, dzban)))
        break
    elif wybor_menu == "2":
        print(czemu)
    elif wybor_menu == "3":
        exit()
    else:
        pass