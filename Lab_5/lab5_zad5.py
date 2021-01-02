sum = 0
sum1 = 0
pot = 10**6
i = 0
for x in range(0, 101):
    sum = sum + x**3

print(sum)

while True:
    sum1 = sum1 + i**3
    if sum1 > pot:
        break
    i += 1

print("Trzeba zsumować {} liczb naturalnych.".format(i))