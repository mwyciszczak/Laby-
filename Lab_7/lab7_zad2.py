import random

tuple = ()

for x in range(50):
    losowa = (random.randint(0, 10), (random.randint(0, 10)))
    tuple = tuple + losowa

print("Licza 0 występuje {} razy.".format(tuple.count(0)))
print("Licza 1 występuje {} razy.".format(tuple.count(1)))
print("Licza 2 występuje {} razy.".format(tuple.count(2)))

print("Liczby parzyste:")
for x in tuple:
    if x % 2 == 0:
        print(x, end=" ")

print("\nLiczby nieparzyste:")
for x in tuple:
    if x % 2 != 0:
        print(x, end=" ")

#mogę dodać element do innej krotki i połączyć dwie krotki ze sobą