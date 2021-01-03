import webbrowser

baza = {"admin": "admin",
        "aa": "haa",
        "bb": "hbb",
        "cc": "hcc",
        "dd": "hdd",
        "ee": "hee",
}

login = input("Podaj login: ")
haslo = input("Podaj haslo: ")

if login in baza.keys() and haslo == baza[login]:
    if login == "admin" and haslo == "admin":
        webbrowser.open_new_tab("strona_admina.html")
    else:
        webbrowser.open_new_tab("strona_inna.html")
else:
    print("Brak dostępu")