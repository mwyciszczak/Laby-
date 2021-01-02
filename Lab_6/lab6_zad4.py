inp = int(input("Podaj liczbę: "))
tab = []

for x in range(1, inp):
    if inp % x == 0:
        tab.append(x)
tab.append(inp)
print(tab)