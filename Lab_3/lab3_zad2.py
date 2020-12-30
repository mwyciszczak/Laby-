x = int(input("Podaj górny zakres: "))

for x in range(x, 0, -1):
    if x % 6 == 0 and x % 9 == 0:
        print(x)