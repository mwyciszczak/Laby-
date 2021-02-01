pytania = ["Czy python to język programowania?",
           "Czy każdy komputer posiada zasilacz?",
           "Czy 64 GB ramu w komputerze do dużo dla przeciętnego użytkownika?",
           "Czy pierwszym językiem programowania był Polski język LECH?",
           "Czy umiesz obsłużyć przeglądarkę internetową?(tak jest dobra i zła odpowiedź)",
           "Czy github jest potrzebny programistom?",
           "Czy 1 GB to więcej niż 1 Gb?",
           "Czy posiadanie ciemnego motywu w swoim IDE jest obowiązkowe?",
           "Czy każdy programista powinen mieć kota?",
           "Czy Windows jest lepszy od Linuxa?"]

odpowiedzi = [True, True, True, False, True, True, True, True, True, True, True]

def quiz():
    punkty = 0
    for x in range(len(pytania)):
        print(pytania[x])
        while True:
            wybor = input('Tak - "y"      Nie - "n"')
            if wybor == "y" or wybor == "Y":
                odpowiedz = True
                break
            elif wybor == "n" or wybor == "N":
                odpowiedz = False
                break
            else:
                print('Proszę użyj liter "y" i "n"')
        if odpowiedz == odpowiedzi[x]:
            punkty += 1
    print("Twój wynik to {} na {} punktów.".format(punkty, len(pytania)))


print("Witaj w quzie wiedzy informatycznej")
print("""
1.Quiz
2.Wyjście
""")
while True:
    wybor_menu = input("Proszę wybierz opcję (1, 2): ")
    if wybor_menu == "1":
        quiz()
        break
    elif wybor_menu == "2":
        exit()
    else:
        pass