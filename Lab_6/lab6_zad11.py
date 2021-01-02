# 0 i 1 nie są liczbami pierwszymi więc je pomijam

n = int(input("Proszę podać cyfre: "))

pierwsze = []
lista = list(range(n+1))
for x in range(2, n+1):
    if lista[x]:
        pierwsze.append(x)
        for y in range(x*2, n+1, x):
            lista[y] = 0
print(pierwsze)

