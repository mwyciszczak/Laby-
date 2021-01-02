import sympy

x = int(input("Podaj liczbę: "))

if sympy.isprime(x) == True:
    print("To jest liczba pierwsza.")
else:
    print("To nie jest liczba pierwsza.")