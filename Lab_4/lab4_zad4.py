#w moim wariancie liczymy ostatnie 0 do średniej, poniżej wariant bez liczenia 0

sum = 0
i = 0
while True:
    inp = float(input("Proszę podaj liczbę: "))
    sum = sum + inp
    i += 1
    if inp == 0:
        print(sum/i)
        break

"""sum = 0
i = 0
while True:
    inp = float(input("Proszę podaj liczbę: "))
    if inp == 0:
        print(sum / i)
        break
    sum = sum + inp
    i += 1
"""