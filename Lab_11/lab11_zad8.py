import random

liczba = random.randint(0, 100)
sum = 0

for x in range(liczba):
    sum = sum + x**2
    print(sum, end=" ")