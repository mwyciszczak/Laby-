#mini lotto wersja prosta
import random

tab = []
"""
while len(tab) < 5:
    liczba = random.randint(1, 42)
    if liczba not in tab:
        tab.append(liczba)

print(tab)"""

for x in range(0, 100000):
    liczba = random.randint(1, 42)
    if liczba not in tab:
        tab.append(liczba)
        print(x)
    if len(tab) == 5:
        break
print(tab)

#załączam rozwiązanie z pętlą for, aczkolwiek uważam, że do tego zadania pętla while pasuje bardziej