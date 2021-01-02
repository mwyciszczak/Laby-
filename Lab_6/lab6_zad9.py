ile = int(input("Podaj ile liczb chcesz wpisac: "))
tab = []

for x in range(ile):
    inp = int(input("Podaj liczbę: "))
    tab.append(inp)

tab = sorted(tab)
print(tab)
najwieksza = tab[-1]
i = 0
for x in tab:
    if x == najwieksza:
        i += 1
print("Największa z liczb tego ciągu to {} i występuje ona {} razy.".format(najwieksza, i))