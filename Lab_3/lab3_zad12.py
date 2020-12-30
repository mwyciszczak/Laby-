import random

orly = 0
reszki = 0

for x in range(50):
    wynik = random.randint(0, 1)
    if wynik == 0:
        orly += 1
    elif wynik == 1:
        reszki += 1

print("Wylosowano {} orłów i {} reszek".format(orly, reszki))