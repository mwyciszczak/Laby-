import random

tab = []
for x in range(10):
    tab.append(random.randint(1, 20))

print("Element 1 to {}, 4 to {}, 7 to {}, a ostatni 9 to {}".format(tab[0], tab[3], tab[6], tab[8]))