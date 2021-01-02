import random

lista_generowana = []
for i in range (10):
    lista_generowana.append(random.randint(0,100))
print("Lista wygenerowana:")
print(lista_generowana)

random.shuffle(lista_generowana)
print("lista wymieszana:")
print(lista_generowana)

lista_generowana.sort()
print("Lista posortowana:")
print(lista_generowana)