imie = input("Proszę podać imię: ")
nazwisko = input("Proszę podać nazwisko: ")
nr_telefonu = input("Proszę podać numer telefonu: ")
nr_buta = input("Proszę podać rozmiar buta: ")

boolean_imie = imie.isalpha()
boolean_nazwisko = nazwisko.isalpha()
boolean_nr_telefonu = nr_telefonu.isdecimal()
boolean_nr_buta = nr_buta.isdecimal()

print("Imię zawiera tylko litery: ", boolean_imie)
print("Nazwisko zawiera tylko litery: ", boolean_nazwisko)
print("Numer telefonu zawiera tylko cyfry: ", boolean_nr_telefonu)
print("Numer buta zawiera tylko cyfry: ", boolean_nr_buta)

if imie[0].isupper() == False:
    imie = imie[:0] + imie[0].upper() + imie[1:]

else:
    pass

if nazwisko[0].isupper() == False:
    nazwisko = nazwisko[:0] + nazwisko[0].upper() + nazwisko[1:]

else:
    pass

if boolean_nr_telefonu == False:

    indeks = 0

    for x in nr_telefonu:
        if (x.isnumeric()) == True:
            indeks+= 1
        else:
            nr_telefonu = nr_telefonu[:indeks] + nr_telefonu[indeks+1:]
            pass

if boolean_nr_buta == False:

    indeks = 0

    for x in nr_buta:
        if (x.isnumeric()) == True:
            indeks+= 1
        else:
            nr_buta = nr_buta[:indeks] + nr_buta[indeks+1:]
            pass

długość = len(imie)

if imie == "Kuba" or imie == "Kosma" or imie == "Dyzma" or imie == "Barnaba" or imie == "Bonawentura":
    print("Użytkownik jest płci męskiej")

elif imie[długość-1] == "a" or imie == "Nel":
    print("Użytkownik jest płci żeńskiej")

else:
    print("Użytkownik jest płci męskiej")

#print(nr_telefonu)
#print(imie)