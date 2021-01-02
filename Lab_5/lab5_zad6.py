import random

losowa = random.randint(1, 100)
i = 0

#print(losowa)
while i < 3:
    inp = int(input("Podaj liczbę: "))
    if inp > losowa:
        print("Podałeś za dużą wartość.")
    elif inp < losowa:
        print("Podałeś za małą wartość.")
    elif inp == losowa:
        print("Gratulacje")
        exit()
    i += 1
print("Haha przegrałeś!")
