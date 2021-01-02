import random

def _6liczb():
    global liczby
    liczby = []
    while len(liczby) < 6:
        wylosowana = random.randint(1, 50)
        if wylosowana not in liczby:
            liczby.append(wylosowana)

def losowanie():
    global trafienia
    trafienia = []
    czy_losowe = input("Czy chcesz wpisywac liczby ręcznie? (Y-Tak, N-Nie)")
    if czy_losowe == "Y" or czy_losowe == "y":
        for x in range(6):
            inp = int(input("Podaj liczbę z zakresu 1-49: "))
            trafienia.append(inp)
    else:
        while len(trafienia) < 6:
            wylosowana = random.randint(1, 50)
            if wylosowana not in trafienia:
                trafienia.append(wylosowana)

ile_losowan = int(input("Podaj ilość losowań: "))

for x in range(ile_losowan):
    _6liczb()
    losowanie()

    trafienia = set(trafienia)
    liczby = set(liczby)
    wspólne = trafienia | liczby

    if len(wspólne) == 6:
        print("Trafiłeś 6, wygrywasz 10000000 zł")
    elif len(wspólne) == 7:
        print("Trafiłeś 5, wygrywasz 5300 zł.")
    elif len(wspólne) == 8:
        print("Trafiłeś 4, wygrywasz 170 zł.")
    elif len(wspólne) == 9:
        print("Trafiłeś 3, wygrywasz 45 zł.")
    elif len(wspólne) == 10:
        print("Trafiłeś 2, nie wygrywasz nic.")
    elif len(wspólne) == 11:
        print("Trafiłeś 1, nie wygrywasz nic.")
    elif len(wspólne) == 12:
        print("Nie trafiłeś nic.")

