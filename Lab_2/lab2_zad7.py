import math

a = 5
b = 23
c = 9

d = (b ** 2) - (4 * a * c)

x1 = (-b - math.isqrt(d)) / (2 * a)
x2 = (-b + math.isqrt(d)) / (2 * a)

print('Rozwiązania to {} i {}'.format(x1, x2))
