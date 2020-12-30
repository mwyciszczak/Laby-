import random

tab = []
"""
while len(tab) < 6:
    liczba = random.randint(1, 49)
    if liczba not in tab:
        tab.append(liczba)

print(tab)"""

for x in range(0, 100000):
    liczba = random.randint(1, 49)
    if liczba not in tab:
        tab.append(liczba)
        print(x)
    if len(tab) == 6:
        break
print(tab)

#załączam rozwiązanie z pętlą for, aczkolwiek uważam, że do tego zadania pętla while pasuje bardziej