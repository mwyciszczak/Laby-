#dopiero po skończonym zadaniu zrozumiałem, że lista miała zostać uzupełniona ręcznie, ale to rozwiązanie też działa
import random
tab = []

for x in range(10):
    tab.append(random.randint(0, 59))

tab.append(2)
tab.append(4)
tab.append(6)


i = 0
for x in tab:
    if x % 2 != 0:
        tab.remove(x)
        i += 1
    if i >= 2:
        break

indeks = 0
for x in tab:
    if x % 2 != 0:
        tab.pop(indeks)
        break
    indeks += 1

tab[4] = 3
tab[9] = 33
print(tab)