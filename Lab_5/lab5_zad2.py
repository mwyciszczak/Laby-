import statistics

n = int(input("Podaj dolną granicę zakresu: "))
x = int(input("Podaj górną granicę zakresu: "))
i = 0
sum = 0
max = 0
tab = []

for x in range(n, x):
    if n == 0 or x == 0:
        break
    print(x)
    sum = sum + x
    max = x
    tab.append(x)
    if i == 5:
        break
    i += 1

print("Minimum to {}, maksimum to {}.".format(tab[0], tab[5]))
print("Średnia to {}, a mediana to {}.".format(statistics.mean(tab), statistics.median(tab)))
