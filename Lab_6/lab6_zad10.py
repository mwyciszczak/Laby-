a = 0
b = 1
inp = int(input("Podaj cyfrę: "))
wynik = []
for x in range(inp):
    a += b
    b = a - b
    wynik.append(a)
print(wynik)

