import random

tab = []
"""
while len(tab) < 20:
    liczba = random.randint(1, 80)
    if liczba not in tab:
        tab.append(liczba)

print(tab)"""

for x in range(0, 100000):
    liczba = random.randint(1, 80)
    if liczba not in tab:
        tab.append(liczba)
        print(x)
    if len(tab) == 20:
        break
print(tab)

#załączam rozwiązanie z pętlą for, aczkolwiek uważam, że do tego zadania pętla while pasuje bardziej